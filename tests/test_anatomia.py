"""Tests for modos/2-anatomia: what was left out, the Spanish texts, and that an example still builds.

    python3 -m unittest discover -s tests -v
"""
import os
import shutil
import subprocess
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MODE = os.path.join(os.path.dirname(HERE), "skills", "skills-secretas", "modos", "2-anatomia")


def read(*parts):
    with open(os.path.join(MODE, *parts), encoding="utf-8") as fh:
        return fh.read()


class Package(unittest.TestCase):
    def test_gallery_publishing_is_left_out(self):
        for gone in ("scripts/publish.mjs", "scripts/session.mjs", "scripts/fingerprint.mjs", "references/publish.md"):
            self.assertFalse(os.path.exists(os.path.join(MODE, gone)), gone)

    def test_examples_ship_as_sources_only(self):
        examples = os.path.join(MODE, "examples")
        built = [f for _, _, files in os.walk(examples) for f in files if f.endswith((".html", ".pdf"))]
        self.assertEqual(built, [])
        for name in ("dial-indicator", "desk-computer", "arcade-cabinet", "raptor-engine", "ripple-tank",
                     "turning-dial", "push-button"):
            self.assertTrue(os.path.isfile(os.path.join(examples, name, "build.mjs")), name)

    def test_every_kit_file_the_mode_names_is_there(self):
        text = read("MODO.md")
        for rel in ("kit/iso-kit.ts", "kit/iso-kit.mjs", "kit/iso.css", "kit/react/draw.tsx", "kit/react/live.tsx",
                    "kit/lathe.mjs", "kit/tube.mjs", "kit/audit.mjs", "kit/gl.mjs", "kit/turn.mjs",
                    "kit/turn-build.mjs", "kit/turn-audit.mjs", "kit/pdf-button.mjs", "scripts/capture.mjs",
                    "scripts/drive.mjs", "scripts/lines.mjs", "scripts/inline-kit.mjs", "scripts/turn-check.mjs",
                    "scripts/turn-bench.mjs", "scripts/print.mjs", "scripts/print-sheet.mjs"):
            self.assertIn("`%s`" % rel, text)
            self.assertTrue(os.path.isfile(os.path.join(MODE, rel)), rel)
        for ref in ("craft", "kit", "motion", "react", "verify", "webgl", "walkthrough", "3d", "print"):
            self.assertTrue(os.path.isfile(os.path.join(MODE, "references", ref + ".md")), ref)


class Spanish(unittest.TestCase):
    def test_print_sheets_are_in_spanish(self):
        sheet = read("scripts", "print-sheet.mjs")
        for english in ('"How it works"', "<h2>How it works", ">Parts<", ">Specification<", ">Not to scale<",
                        "<h2>Assemblies</h2>", "<span>Anatomy</span>", 'lang="en"'):
            self.assertNotIn(english, sheet)
        for spanish in ('"Cómo funciona"', "<h2>Cómo funciona", ">Piezas<", ">Especificaciones<", ">Sin escala<",
                        "<h2>Conjuntos</h2>", "<span>Anatomía</span>", 'lang="es"'):
            self.assertIn(spanish, sheet)

    def test_pages_and_pdf_button_are_in_spanish(self):
        for name in ("iso-kit.mjs", "iso-kit.ts"):
            kit = read("kit", name)
            self.assertIn('width = 650, lang = "es" }', kit, name)
            self.assertIn('<html lang="${escape(lang)}">', kit, name)
        self.assertIn('"Abrir el PDF para imprimir"', read("kit", "pdf-button.mjs"))


@unittest.skipUnless(shutil.which("node"), "hace falta Node.js")
class Build(unittest.TestCase):
    def test_the_smallest_example_builds_from_a_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = os.path.join(tmp, "2-anatomia")
            shutil.copytree(MODE, copy)
            build = os.path.join(copy, "examples", "dial-indicator", "build.mjs")
            r = subprocess.run(["node", build], capture_output=True, text=True, timeout=300, cwd=tmp)
            self.assertEqual(r.returncode, 0, r.stderr[-800:])
            page = os.path.join(copy, "examples", "dial-indicator", "dial-indicator.html")
            with open(page, encoding="utf-8") as fh:
                html = fh.read()
            self.assertTrue(html.startswith('<!doctype html><html lang="es">'))
            self.assertIn("<svg", html)

    def test_the_page_language_can_change(self):
        kit = os.path.join(MODE, "kit", "iso-kit.mjs").replace("\\", "/")
        script = ("import(%r).then(k => console.log(k.pageHtml({ title: 't', body: '', lang: 'en' }).slice(0, 40)))"
                  % ("file://" + kit))
        r = subprocess.run(["node", "-e", script], capture_output=True, text=True, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('<html lang="en">', r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
