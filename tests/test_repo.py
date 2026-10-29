"""Tests for the package: manifests, the entry SKILL.md, modes, licenses and links. Standard library only.

    python3 -m unittest discover -s tests -v
"""
import json
import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SKILL = os.path.join(REPO, "skills", "skills-secretas")
NAME = "skills-secretas"
URL = "https://github.com/aldushmedia/" + NAME
MODES = ["1-jefe-de-equipo", "2-anatomia", "3-profe", "4-psicologia-marketing", "5-ultimos-30-dias"]
AUTHORS = {"chief-of-staff": "Matt Pocock", "teach": "Matt Pocock", "anatomy": "Ryan",
           "marketing-psychology": "Corey Haines", "last30days": "Matt Van Horn"}
ALDUSH = "Copyright (c) 2026 Aldush Media (traducción y adaptación al español)"


def read(*parts):
    with open(os.path.join(REPO, *parts), encoding="utf-8") as fh:
        return fh.read()


def every_file():
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for name in files:
            path = os.path.join(root, name)
            with open(path, encoding="utf-8", errors="ignore") as fh:
                yield os.path.relpath(path, REPO), fh.read()


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else None


def description(fm):
    block = fm.split("description: >-\n", 1)[1]
    return " ".join(line.strip() for line in block.splitlines() if line.startswith("  "))


class Package(unittest.TestCase):
    def test_plugin_and_marketplace(self):
        plugin = json.loads(read(".claude-plugin", "plugin.json"))
        self.assertEqual(plugin["name"], NAME)
        self.assertEqual((plugin["homepage"], plugin["repository"]), (URL, URL))
        self.assertEqual(plugin["author"]["name"], "Aldush Media")
        market = json.loads(read(".claude-plugin", "marketplace.json"))
        self.assertEqual(market["name"], NAME)
        self.assertEqual(market["plugins"][0]["name"], NAME)
        self.assertEqual(market["plugins"][0]["homepage"], URL)

    def test_install_commands(self):
        for doc in (read("README.md"), read("skills", NAME, "INSTALAR.md"), read("skills", NAME, "COMO_USAR.md")):
            self.assertIn("/plugin marketplace add aldushmedia/" + NAME, doc)
            self.assertIn("/plugin install %s@%s" % (NAME, NAME), doc)
        for line in ("git clone %s.git" % URL, "cp -r skills-secretas/skills/skills-secretas ~/.claude/skills/"):
            self.assertIn(line, read("README.md"))
        self.assertIn("explícame cómo funciona un reel viral, interactivo", read("skills", NAME, "INSTALAR.md"))

    def test_license_keeps_every_original_and_adds_aldush_media(self):
        lines = read("LICENSE").rstrip("\n").split("\n")
        self.assertEqual(lines[0], "MIT License")
        for author in set(AUTHORS.values()):
            self.assertTrue(any(l.startswith("Copyright (c) 202") and l.endswith(author) for l in lines), author)
        self.assertEqual(lines[-1], ALDUSH)

    def test_each_original_license_is_kept(self):
        for skill, author in AUTHORS.items():
            text = read("skills", NAME, "licencias", skill + ".txt")
            self.assertTrue(text.startswith("MIT License\n\nCopyright (c) 202"), skill)
            self.assertIn(author, text.split("\n")[2], skill)
            self.assertIn("The above copyright notice and this permission notice shall be included", text)
        self.assertTrue(os.path.isfile(os.path.join(SKILL, "modos", MODES[4], "scripts", "lib", "vendor",
                                                    "bird-search", "LICENSE")))

    def test_credits_list_every_original_with_its_commit(self):
        credits = read("skills", NAME, "CREDITOS.md")
        for repo in ("mattpocock/skills", "wheresryan22/anatomy", "coreyhaines31/marketingskills",
                     "mvanhorn/last30days-skill"):
            self.assertIn("https://github.com/" + repo, credits)
        self.assertEqual(len(re.findall(r"`[0-9a-f]{40}`", credits)), 5)
        for skill in AUTHORS:
            self.assertIn("licencias/%s.txt" % skill, credits)

    def test_no_em_dashes_anywhere(self):
        bad = [rel for rel, text in every_file() if chr(0x2014) in text]
        self.assertEqual(bad, [])


class EntrySkill(unittest.TestCase):
    def setUp(self):
        self.text = read("skills", NAME, "SKILL.md")
        self.fm = frontmatter(self.text)

    def test_frontmatter(self):
        self.assertIsNotNone(self.fm)
        self.assertRegex(self.fm, r"(?m)^name: skills-secretas$")
        self.assertRegex(NAME, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        desc = description(self.fm)
        self.assertLessEqual(len(desc), 1024)
        for phrase in ("explícame cómo funciona", "enséñame", "qué se dijo de", "aplica psicología a mi oferta",
                       "encárgate de esta meta", "chief of staff", "teach me", "last30days", "interactive explainer",
                       "persuasion"):
            self.assertIn(phrase, desc)

    def test_points_to_one_mode_file_each(self):
        for mode in MODES:
            self.assertIn("(modos/%s/MODO.md)" % mode, self.text)
            self.assertTrue(os.path.isfile(os.path.join(SKILL, "modos", mode, "MODO.md")), mode)
        self.assertIn("lee **solo** su `MODO.md`", self.text)

    def test_credits_footer(self):
        footer = self.text.rstrip().rsplit("---", 1)[1]
        self.assertIn("Adaptación al español: Aldush ([@aldushmedia](https://github.com/aldushmedia))", footer)
        self.assertIn("Basada en el trabajo de:", footer)
        self.assertIn("Ver [CREDITOS.md](CREDITOS.md)", footer)
        for author in set(AUTHORS.values()):
            self.assertIn("[%s](https://github.com/" % author, footer)

    def test_only_one_skill_file(self):
        found = [rel for rel, _ in every_file() if os.path.basename(rel) == "SKILL.md"]
        self.assertEqual(found, [os.path.join("skills", NAME, "SKILL.md")])
        for mode in MODES:
            self.assertIsNone(frontmatter(read("skills", NAME, "modos", mode, "MODO.md")), mode)


class Modes(unittest.TestCase):
    def test_relative_links_resolve(self):
        bad = []
        for rel, text in every_file():
            if not rel.endswith(".md"):
                continue
            for url in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
                if re.match(r"[a-z]+://|mailto:|#", url) or "{" in url or url == "url":
                    continue
                target = os.path.join(REPO, os.path.dirname(rel), url.split("#")[0])
                if not os.path.exists(target):
                    bad.append((rel, url))
        self.assertEqual(bad, [])

    def test_no_old_commands_or_install_paths(self):
        old = re.compile(r"skills/last30days|\.claude/skills/(last30days|anatomy|teach)|/chief-of-staff\b|`/teach\b"
                         r"|(?<![\w./~$}-])/last30days(?![\w./-])")
        bad = []
        for rel, text in every_file():
            if not rel.endswith((".md", ".json")) or "vendor" in rel.split(os.sep):
                continue
            if os.path.basename(rel) in ("CAMBIOS.md", "CREDITOS.md"):
                continue   # these two describe the originals on purpose
            text = text.replace("Donde digan `/last30days`", "")   # the mapping note in mode 5
            if old.search(text):
                bad.append(rel)
        self.assertEqual(bad, [])

    def test_engine_messages_name_the_new_command(self):
        lib = os.path.join("skills", NAME, "modos", MODES[4], "scripts", "lib")
        for name, snippet in (("pipeline.py", "command=f'/skills-secretas 30dias "),
                              ("doctor.py", "run `/skills-secretas 30dias <topic>` first"),
                              ("render.py", "rerun `/skills-secretas 30dias {report.topic}`"),
                              ("html_render.py", 'html.escape(f"/skills-secretas 30dias {display_topic}")'),
                              ("prescriptions.py", '"python3 skills/skills-secretas/modos/5-ultimos-30-dias/scripts/last30days.py"')):
            self.assertIn(snippet, read(lib, name), name)

    def test_every_marketing_principle_is_kept(self):
        original = ["First Principles", "Jobs to Be Done", "Circle of Competence", "Inversion", "Occam's Razor",
                    "Pareto Principle (80/20 Rule)", "Local vs. Global Optima", "Theory of Constraints",
                    "Opportunity Cost", "Law of Diminishing Returns", "Second-Order Thinking", "Map ≠ Territory",
                    "Probabilistic Thinking", "Barbell Strategy", "Fundamental Attribution Error",
                    "Mere Exposure Effect", "Availability Heuristic", "Confirmation Bias", "The Lindy Effect",
                    "Mimetic Desire", "Sunk Cost Fallacy", "Endowment Effect", "IKEA Effect", "Zero-Price Effect",
                    "Hyperbolic Discounting / Present Bias", "Status-Quo Bias", "Default Effect",
                    "Paradox of Choice", "Goal-Gradient Effect", "Peak-End Rule", "Zeigarnik Effect",
                    "Pratfall Effect", "Curse of Knowledge", "Mental Accounting", "Regret Aversion",
                    "Bandwagon Effect / Social Proof", "Reciprocity Principle", "Commitment & Consistency",
                    "Authority Bias", "Liking / Similarity Bias", "Unity Principle", "Scarcity / Urgency Heuristic",
                    "Foot-in-the-Door Technique", "Door-in-the-Face Technique", "Loss Aversion / Prospect Theory",
                    "Anchoring Effect", "Decoy Effect", "Framing Effect", "Contrast Effect",
                    "Charm Pricing / Left-Digit Effect", "Rounded-Price (Fluency) Effect", "Rule of 100",
                    "Price Relativity / Good-Better-Best", "Mental Accounting (Pricing)", "Hick's Law",
                    "AIDA Funnel", "Rule of 7", "Nudge Theory / Choice Architecture", "BJ Fogg Behavior Model",
                    "EAST Framework", "COM-B Model", "Activation Energy", "North Star Metric", "The Cobra Effect",
                    "Feedback Loops", "Compounding", "Network Effects", "Flywheel Effect", "Switching Costs",
                    "Exploration vs. Exploitation", "Critical Mass / Tipping Point", "Survivorship Bias"]
        self.assertEqual(len(original), 72)
        headings = re.findall(r"^### (.+)$", read("skills", NAME, "modos", MODES[3], "MODO.md"), re.M)
        self.assertEqual(len(headings), 72)
        for name in original:
            self.assertTrue(any(h.endswith("(%s)" % name) for h in headings), name)

    def test_teach_formats_are_there(self):
        for name in ("MISSION-FORMAT.md", "LEARNING-RECORD-FORMAT.md", "GLOSSARY-FORMAT.md", "RESOURCES-FORMAT.md"):
            self.assertIn("(./%s)" % name, read("skills", NAME, "modos", MODES[2], "MODO.md"))

    def test_chief_of_staff_only_on_request(self):
        text = read("skills", NAME, "modos", MODES[0], "MODO.md")
        self.assertIn("Solo cuando el usuario lo pida de forma", text)
        self.assertIn("Beta", text)

    def test_modes_answer_in_the_users_language(self):
        for mode in MODES:
            self.assertRegex(read("skills", NAME, "modos", mode, "MODO.md"), r"idioma\s+del\s+usuario", mode)


if __name__ == "__main__":
    unittest.main(verbosity=2)
