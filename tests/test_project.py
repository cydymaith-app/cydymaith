"""The Welsh project's own icons, tree and documents, built with the framework in framework/.

Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import json
import pathlib
import re
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "framework"))

import phrasebook  # noqa: E402
from phrasebook import content, grading, icons  # noqa: E402
from phrasebook.channels import select  # noqa: E402

PROJECT = ROOT / "content" / "cydymaith"


class PhilosophyTests(unittest.TestCase):
    def test_the_purpose_says_so(self):
        text = (ROOT / "docs" / "PHILOSOPHY.md").read_text(encoding="utf-8")
        self.assertIn("Mobile first", text)
        self.assertIn("one hand", text)


class ProjectNavigationTests(unittest.TestCase):
    """The English and Welsh project's own icons and tree."""

    @classmethod
    def setUpClass(cls):
        import shutil
        import tempfile
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        phrasebook.build(cls.tmp / "dist")
        cls.doc = json.loads((cls.tmp / "dist" / "tree.json").read_text(encoding="utf-8"))
        cls.raw = content.read(PROJECT)
        cls._shutil = shutil

    @classmethod
    def tearDownClass(cls):
        cls._shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_every_group_and_page_that_is_published_has_an_icon_that_exists(self):
        for group in self.doc["nodes"]:
            self.assertIn(group["icon"], self.doc["icons"], group["id"])
            for page in group["children"]:
                self.assertIn(page["icon"], self.doc["icons"], page["id"])

    def test_the_icon_set_keeps_its_licence_with_it_and_the_policy_names_it(self):
        licence = (PROJECT / "icons" / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", licence)
        assets = (ROOT / "docs" / "ASSETS.md").read_text(encoding="utf-8")
        self.assertIn("Carbon", assets)
        self.assertRegex(assets, r"@carbon/icons\S* ?\d+\.\d+\.\d+")

    def test_every_icon_file_is_a_safe_svg_that_says_where_it_came_from_and_is_in_the_policy(self):
        files = sorted((PROJECT / "icons").glob("*.svg"))
        self.assertTrue(files)
        assets = (ROOT / "docs" / "ASSETS.md").read_text(encoding="utf-8")
        for f in files:
            text = f.read_text(encoding="utf-8")
            self.assertTrue("@carbon/icons" in text or "Project icon" in text, f"{f.name} does not say where it came from")
            icons.markup(text)
            self.assertIn(f"`{f.stem}`", assets, f"{f.name} is not recorded in docs/ASSETS.md")

    def test_the_release_publishes_four_groups_and_development_adds_the_held_back_ones(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            release, development = pathlib.Path(tmp) / "r", pathlib.Path(tmp) / "d"
            phrasebook.build(release, project_dir=PROJECT)
            phrasebook.build(development, project_dir=PROJECT, channel="development")
            rel = sorted(f.name for f in release.glob("group-*.html"))
            dev = sorted(f.name for f in development.glob("group-*.html"))
        self.assertEqual(rel, ["group-everyday.html", "group-geography.html", "group-time-and-place.html", "group-weather-forecast.html"])
        self.assertEqual(dev, ["group-everyday.html", "group-geography.html", "group-news.html", "group-sport.html",
                               "group-time-and-place.html", "group-weather-forecast.html"])

    def test_the_held_back_groups_have_their_mockup_icons_and_welsh_titles_marked_for_review(self):
        structure = json.loads((PROJECT / "structure.json").read_text(encoding="utf-8"))
        icons_by_group = {g["id"]: g.get("icon") for g in structure["groups"]}
        self.assertEqual({k: icons_by_group[k] for k in ("geography", "news", "sport")},
                         {"geography": "earth", "news": "blog", "sport": "trophy"})
        cy = json.loads((PROJECT / "packs" / "cy" / "pack.json").read_text(encoding="utf-8"))["groups"]
        self.assertEqual((cy["geography"], cy["news"], cy["sport"]), ("Daearyddiaeth", "Newyddion", "Chwaraeon"))
        review = (ROOT / "docs" / "REVIEW.md").read_text(encoding="utf-8")
        for word in ("Daearyddiaeth", "Newyddion", "Chwaraeon"):
            self.assertIn(word, review)

    def test_the_weather_group_has_the_scattered_rain_icon(self):
        weather = self.doc["nodes"][0]
        self.assertEqual(weather["icon"], "rain--scattered")

    def test_the_worked_example_in_the_to_do_is_a_real_path_through_the_tree(self):
        weather = self.doc["nodes"][0]
        self.assertEqual(weather["id"], "1")
        titles = [p["second"]["text"] for p in weather["children"]]
        self.assertIn("Rain and storms", titles)
        rain_page = next(p for p in weather["children"] if p["second"]["text"] == "Rain and storms")
        rain = next(s for s in rain_page["children"] if s["href"].endswith("#rain"))
        self.assertIn("Drizzle", [w["second"]["text"] for w in rain["children"]])


if __name__ == "__main__":
    unittest.main()


class RelatedTopicsTests(unittest.TestCase):
    """The weather topics link to the place phrases, and the places link back to how it is said, as a row of tiles."""

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        cls.raw = raw
        cls.pages = phrasebook.Site(raw, edition).render_all()

    def tiles(self, name):
        page = self.pages[name]
        return re.findall(r'<a class="tile-link" href="([^"]+)" data-related>', page)

    def test_the_weather_topics_that_mention_places_open_the_landscape_section_of_where(self):
        for name in ("rain.html", "snow-ice.html", "patterns.html"):
            self.assertEqual(self.tiles(name), ["where.html#landscape"], name)

    def test_the_tile_is_named_for_the_section_in_welsh_and_english(self):
        row = self.pages["rain.html"]
        row = row[row.index('<section class="related"') :]
        self.assertIn("Pynciau cysylltiedig", row)
        self.assertIn("Related topics", row)
        self.assertIn('<span class="l1" lang="cy">Tirwedd</span><span class="l2">Landscape</span>', row)

    def test_wind_opens_the_compass_and_the_places_open_how_it_is_said(self):
        self.assertEqual(self.tiles("wind.html"), ["where.html#points"])
        self.assertEqual(self.tiles("where.html"), ["patterns.html"])

    def test_every_section_a_tile_lands_on_is_on_the_page_it_opens(self):
        for name, page in self.pages.items():
            for href in re.findall(r'href="([a-z0-9-]+\.html)#([A-Za-z0-9._-]+)" data-related', page):
                target = self.pages[href[0]]
                self.assertIn(f'id="{href[1]}"', target, f"{name} -> {href}")

    def test_a_topic_with_nothing_related_has_no_row_and_the_group_pages_have_none(self):
        self.assertNotIn('class="related"', self.pages["sky.html"])
        self.assertNotIn('class="related"', self.pages["group-weather-forecast.html"])
        self.assertNotIn('class="related"', self.pages["index.html"])


class GradingTests(unittest.TestCase):
    """How demanding each tile and section is, from beginner to advanced, worked out from the size of a typical Welsh entry.

    The rule is in framework/phrasebook/grading.py; `python3 build.py --grades` prints the grades. A level set by hand
    (`"level"` in a skeleton file) is for the few places where the rule is plainly wrong, and each is explained below.
    """

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        graded = grading.grade(raw, edition)
        cls.groups = {g["id"]: g for g in graded["groups"]}
        cls.pages = {p["id"]: p for g in graded["groups"] for p in g["pages"]}
        cls.sections = {(p["id"], s["id"]): s for p in cls.pages.values() for s in p["sections"]}

    def test_the_words_counted_are_the_welsh_the_viewer_hears(self):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        self.assertEqual(grading.settings(edition)[0], "cy")

    def test_everything_published_has_a_level_from_one_to_three(self):
        for node in [*self.groups.values(), *self.pages.values(), *self.sections.values()]:
            self.assertIn(node["level"], (1, 2, 3), node["id"])

    def test_one_word_for_a_thing_is_simpler_than_the_same_thing_in_a_phrase(self):
        """north = gogledd comes first; in the north, on the coast, in the valleys follow."""
        points = self.sections[("where", "points")]["level"]
        self.assertEqual(points, 1)
        self.assertGreater(self.sections[("where", "directions")]["level"], points)
        self.assertGreater(self.sections[("where", "landscape")]["level"], points)

    def test_sentences_are_the_most_advanced_and_single_words_the_simplest(self):
        self.assertEqual(self.pages["patterns"]["level"], 3)
        self.assertEqual(self.pages["sky"]["level"], 1)
        self.assertEqual(self.pages["place-name-elements"]["level"], 1)
        self.assertEqual(self.sections[("patterns", "it-will-be")]["level"], 3)
        self.assertLess(self.pages["sky"]["level"], self.pages["patterns"]["level"])

    def test_the_days_are_set_by_hand_because_two_written_words_are_one_beginner_item(self):
        days = self.sections[("when", "days")]
        self.assertEqual((days["level"], days["computed"], days["by_hand"]), (1, 2, True))

    def test_the_rule_does_the_work_and_hand_set_levels_stay_few(self):
        by_hand = [k for k, s in self.sections.items() if s["by_hand"]] + [k for k, p in self.pages.items() if p["by_hand"]]
        by_hand += [k for k, g in self.groups.items() if g["by_hand"]]
        self.assertLessEqual(len(by_hand), 5, f"each one needs a reason: {by_hand}")
