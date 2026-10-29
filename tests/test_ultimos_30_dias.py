"""Tests for the changes to the last30days engine in modos/5-ultimos-30-dias. Standard library only.

The engine needs Python 3.12 or newer, so these tests skip on older versions.

    python3 -m unittest discover -s tests -v
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MODE = os.path.join(os.path.dirname(HERE), "skills", "skills-secretas", "modos", "5-ultimos-30-dias")
SCRIPTS = os.path.join(MODE, "scripts")
NEW_ENOUGH = sys.version_info >= (3, 12)

if NEW_ENOUGH:
    sys.dont_write_bytecode = True   # keep the skill folder clean
    sys.path.insert(0, SCRIPTS)
    from lib import env, html_render, library, render  # noqa: E402

SPANISH = """🌐 Últimos 30 días · last30days v3.31.0 · 2026-10-29

Lo que aprendí:

**Claude Code se volvió la herramienta del mes** - la gente comparte flujos de trabajo con agentes.

PATRONES CLAVE de la investigación:
1. Los agentes en segundo plano - según r/ClaudeAI

---
Ya estoy al día con Claude Code. Algunas cosas en las que te puedo ayudar:
- Comparar Claude Code contra Cursor
Tengo todos los links de los 12 hilos de Reddit que revisé. Solo pídemelos.
"""


@unittest.skipUnless(NEW_ENOUGH, "el motor necesita Python 3.12 o más reciente")
class SpanishLabels(unittest.TestCase):
    def test_both_languages_are_prose_labels(self):
        sources = [source for source, _ in html_render.PROSE_LABELS]
        for label in ("What I learned:", "KEY PATTERNS from the research:", "Lo que aprendí:",
                      "PATRONES CLAVE de la investigación:"):
            self.assertIn(label, sources)
        md = html_render._promote_prose_labels(SPANISH)
        self.assertIn("## Lo que aprendí\n", md)
        self.assertIn("## Patrones clave de la investigación\n", md)

    def test_spanish_and_english_invitations_are_stripped(self):
        self.assertNotIn("Solo pídemelos", html_render._strip_invitation(SPANISH))
        english = "Body\n\n---\nI'm now an expert on X. Some things I can help with:\n- a\nI have all the links. Just ask.\n"
        self.assertNotIn("Just ask", html_render._strip_invitation(english))

    def test_footer_is_found_in_both_languages(self):
        for header in ("✅ All agents reported back!", "✅ ¡Todos los agentes respondieron!"):
            footer = "```text\n---\n%s\n├─ 🟠 Reddit: 12 hilos\n└─ 🟡 HN: 3 historias\n---\n```\n" % header
            self.assertIsNotNone(html_render.FENCED_ENGINE_FOOTER_PATTERN.search(footer), header)

    def test_library_summary_reads_the_spanish_heading(self):
        for heading in ("What I learned", "Lo que aprendí"):
            content = "# Tema\n\n## %s\n\nLa gente habla de agentes.\n\n## Otra\n" % heading
            self.assertEqual(library._markdown_summary(content), "La gente habla de agentes.")

    def test_html_pages_are_in_spanish(self):
        index = html_render.render_library_index([])
        self.assertIn("Todavía no hay resúmenes guardados", index)
        self.assertNotIn("No saved briefs yet", index)


@unittest.skipUnless(NEW_ENOUGH, "el motor necesita Python 3.12 o más reciente")
class Safety(unittest.TestCase):
    def test_browser_cookies_are_off_by_default(self):
        for config in ({}, {"FROM_BROWSER": "chrome", "BROWSER_CONSENT": "true"}, {"AGENTCOOKIE": "on"}):
            self.assertFalse(env.x_policy(config).cookie_discovery, config)

    def test_only_a_bird_pin_turns_them_back_on(self):
        self.assertTrue(env.x_policy({"LAST30DAYS_X_BACKEND": "bird"}).cookie_discovery)

    def test_the_rest_of_the_x_policy_is_the_original(self):
        self.assertFalse(env.x_policy({}).official_only)
        self.assertEqual(env.x_policy({}).auto_chain, ("bird", "xai", "xurl", "xquik"))
        self.assertTrue(env.x_policy({"LAST30DAYS_HOST": "grok-bot"}).official_only)

    def test_no_cookie_read_runs_without_discovery(self):
        config = {"FROM_BROWSER": "chrome", "BROWSER_CONSENT": "true"}
        env._discover_and_apply_x_credentials(config)
        self.assertNotIn("AUTH_TOKEN", config)


@unittest.skipUnless(NEW_ENOUGH, "el motor necesita Python 3.12 o más reciente")
class Engine(unittest.TestCase):
    def test_version_comes_from_the_mode(self):
        with open(os.path.join(MODE, "VERSION"), encoding="utf-8") as fh:
            self.assertEqual(render._skill_version(), fh.read().strip())
        self.assertEqual(render._skill_version(), "3.31.0")

    def test_engine_starts(self):
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "last30days.py"), "--help"],
                           capture_output=True, text=True, timeout=120,
                           env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        self.assertEqual(r.returncode, 0, r.stderr[-500:])

    def test_basic_setup_writes_no_cookie_consent_and_speaks_spanish(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "setup_basico.py")],
                               capture_output=True, text=True, timeout=60,
                               env=dict(os.environ, LAST30DAYS_CONFIG_DIR=tmp, PYTHONDONTWRITEBYTECODE="1"))
            self.assertEqual(r.returncode, 0, r.stderr)
            with open(os.path.join(tmp, ".env"), encoding="utf-8") as fh:
                saved = fh.read().split()
            self.assertEqual(sorted(saved), ["BROWSER_CONSENT=false", "SETUP_COMPLETE=true"])
            self.assertIn("sin cookies del navegador y sin instalar nada", r.stdout)
            self.assertIn("Ya funcionan sin key: Reddit, Hacker News, Polymarket, GitHub y la web.", r.stdout)

    def test_files_left_out_of_the_package(self):
        for gone in ("assets", "agents", os.path.join("scripts", "box_chrome_login.py"),
                     os.path.join("scripts", "setup-keychain.sh")):
            self.assertFalse(os.path.exists(os.path.join(MODE, gone)), gone)

    def test_stale_clone_redirect_is_off(self):
        with open(os.path.join(MODE, "references", "runtime.md"), encoding="utf-8") as fh:
            runtime = fh.read()
        self.assertIn("NOT USED IN SKILLS-SECRETAS", runtime)
        self.assertNotIn("plugins/cache/last30days-skill", runtime)


if __name__ == "__main__":
    unittest.main(verbosity=2)
