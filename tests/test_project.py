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
        self.assertEqual(rel, ["group-everyday.html", "group-geography.html", "group-weather-forecast.html"])
        self.assertEqual(dev, ["group-everyday.html", "group-geography.html", "group-news.html", "group-sport.html",
                               "group-weather-forecast.html"])

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
        self.assertIn("Drizzle here and there", [w["second"]["text"] for w in rain["children"]])


if __name__ == "__main__":
    unittest.main()


class RelatedTopicsTests(unittest.TestCase):
    """The weather topics link to the place phrases, and the places link back to how it is said, as a row of tiles."""

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        cls.raw = raw
        cls.site = phrasebook.Site(raw, edition)
        cls.pages = cls.site.render_all()

    def topic(self, slug):
        """A topic's own part: its page, or on the weather forecast's one page its accordion."""
        page = self.pages[self.site.href(slug).split("#")[0]]
        if slug not in self.site.homes:
            return page
        start = page.index(f'<details class="fold topic" aria-labelledby="h-topic-{slug}"')
        end = page.find('<details class="fold topic"', start + 1)
        return page[start : end if end != -1 else page.index("<script>", start)]

    def tiles(self, slug):
        return re.findall(r'<a class="tile-link" href="([^"]+)" data-related>', self.topic(slug))

    def test_the_weather_topics_that_mention_places_open_the_landscape_section_of_where(self):
        for slug in ("rain", "snow-ice"):
            self.assertEqual(self.tiles(slug), ["group-geography.html#landscape"], slug)
        self.assertEqual(self.tiles("patterns"), ["group-geography.html#landscape", "group-geography.html#regions", "when.html"])

    def test_the_tile_is_named_for_the_section_in_welsh_and_english(self):
        row = self.topic("rain")
        row = row[row.index('<section class="related"') :]
        self.assertIn("Pynciau cysylltiedig", row)
        self.assertIn("Related topics", row)
        self.assertIn('<span class="l1" lang="cy">Tirwedd</span><span class="l2">Landscape</span>', row)

    def test_wind_opens_the_compass_and_the_places_open_how_it_is_said(self):
        self.assertEqual(self.tiles("wind"), ["group-geography.html#points"])
        self.assertEqual(self.tiles("compass"), ["group-weather-forecast.html#topic-patterns"])

    def test_how_its_said_opens_time_and_date_as_a_related_page(self):
        """The tile was on The forecast until that card was dropped on 2026-10-27."""
        self.assertIn("when.html", self.tiles("patterns"))
        row = self.topic("patterns")
        row = row[row.index('<section class="related"') :]
        self.assertIn('<span class="l1" lang="cy">Amser a dyddiad</span><span class="l2">Time and date</span>', row)

    def test_every_section_a_tile_lands_on_is_on_the_page_it_opens(self):
        for name, page in self.pages.items():
            for href in re.findall(r'href="([a-z0-9-]+\.html)#([A-Za-z0-9._-]+)" data-related', page):
                target = self.pages[href[0]]
                self.assertIn(f'id="{href[1]}"', target, f"{name} -> {href}")

    def test_a_topic_with_nothing_related_has_no_row_and_the_group_pages_have_none(self):
        self.assertNotIn('class="related"', self.topic("sky"))
        self.assertNotIn('class="related"', self.pages["group-everyday.html"])
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
        points = self.sections[("compass", "points")]["level"]
        self.assertEqual(points, 1)
        self.assertGreater(self.sections[("compass", "directions")]["level"], points)
        self.assertGreater(self.sections[("place-name-elements", "landscape")]["level"], points)

    def test_sentences_are_the_most_advanced_and_single_words_the_simplest(self):
        self.assertEqual(self.pages["patterns"]["level"], 3)
        self.assertEqual(self.pages["sky"]["level"], 3, "the weather cards hold forecast phrases, not single words (2026-10-27)")
        self.assertEqual(self.pages["place-name-elements"]["level"], 1)
        self.assertEqual(self.sections[("patterns", "it-will-be")]["level"], 3)
        self.assertLess(self.pages["place-name-elements"]["level"], self.pages["patterns"]["level"])

    def test_the_days_are_set_by_hand_because_two_written_words_are_one_beginner_item(self):
        days = self.sections[("when", "days")]
        self.assertEqual((days["level"], days["computed"], days["by_hand"]), (1, 2, True))

    def test_the_rule_does_the_work_and_hand_set_levels_stay_few(self):
        by_hand = [k for k, s in self.sections.items() if s["by_hand"]] + [k for k, p in self.pages.items() if p["by_hand"]]
        by_hand += [k for k, g in self.groups.items() if g["by_hand"]]
        self.assertLessEqual(len(by_hand), 5, f"each one needs a reason: {by_hand}")


class OnePageWeatherTests(unittest.TestCase):
    """The weather forecast is one page: each of its topics is an accordion, shut until opened, in the written order, and the
    topics have no pages of their own (the owner's design pivot of 2026-10-26: too many separate pages under weather)."""

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        cls.site = phrasebook.Site(raw, edition)
        cls.pages = cls.site.render_all()
        cls.page = cls.pages["group-weather-forecast.html"]
        cls.weather = next(g for g in cls.site.groups if g["id"] == "weather-forecast")

    def test_every_weather_topic_is_a_shut_accordion_in_the_written_order(self):
        found = re.findall(r'<details class="fold topic" aria-labelledby="h-topic-([a-z0-9-]+)" id="topic-\1" data-level="[123]">', self.page)
        self.assertEqual(found, self.weather["pages"])
        self.assertNotRegex(self.page, r'<details class="fold topic"[^>]* open', "all shut until opened")

    def test_the_weather_topics_have_no_pages_of_their_own(self):
        for slug in self.weather["pages"]:
            self.assertNotIn(f"{slug}.html", self.pages, slug)

    def test_the_other_groups_keep_their_tiles(self):
        for gid in ("everyday",):
            self.assertIn('<ul class="tiles" data-tiles data-order=', self.pages[f"group-{gid}.html"], gid)


class KeyWordTests(unittest.TestCase):
    """The weather pages mark the words that match across Welsh and English, so the eye can pair them."""

    WEATHER = ("sky", "rain", "snow-ice", "wind", "temperature", "change", "patterns")

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)

    def concepts(self, code, slug):
        for section in self.raw["packs"][code]["pages"][slug]["sections"].values():
            yield from section["concepts"].items()

    def test_every_weather_page_marks_key_words_and_both_languages_mark_the_same_rows(self):
        for slug in self.WEATHER:
            welsh = {cid: len(c.get("keys", [])) for cid, c in self.concepts("cy", slug)}
            english = {cid: len(c.get("keys", [])) for cid, c in self.concepts("en", slug)}
            self.assertEqual(welsh, english, slug)
            self.assertTrue(any(welsh.values()), slug)

    def test_the_only_rows_left_plain_are_function_words_not_weather(self):
        plain = {cid for slug in self.WEATHER for cid, c in self.concepts("cy", slug) if "keys" not in c}
        self.assertFalse({"its-sunny", "rain-in-the-north", "a-cold-northerly"} & plain)

    GEOGRAPHY = ("compass", "geography", "place-name-elements")
    MARKED = {
        "compass": {"from", "directions"},
        "geography": {"regions", "uk"},
        "place-name-elements": {"landscape"},
    }

    def test_the_geography_phrases_mark_key_words_in_both_languages_and_the_single_word_sections_stay_plain(self):
        for slug in self.GEOGRAPHY:
            for sid, sec in self.raw["packs"]["cy"]["pages"][slug]["sections"].items():
                welsh = {cid: len(c.get("keys", [])) for cid, c in sec["concepts"].items()}
                english = {cid: len(c.get("keys", [])) for cid, c in self.raw["packs"]["en"]["pages"][slug]["sections"][sid]["concepts"].items()}
                self.assertEqual(welsh, english, (slug, sid))
                if sid in self.MARKED[slug]:
                    self.assertTrue(any(welsh.values()), (slug, sid))
                else:
                    self.assertFalse(any(welsh.values()), f"{slug}/{sid} is single words and stays plain")

    def test_a_word_has_one_colour_throughout_the_geography_page(self):
        colour = {}
        for slug in self.GEOGRAPHY:
            for sec in self.raw["packs"]["en"]["pages"][slug]["sections"].values():
                for cid, c in sec["concepts"].items():
                    for n, key in enumerate(c.get("keys", [])):
                        if key is not None:
                            colour.setdefault(key.casefold(), set()).add(n)
        self.assertEqual({k: v for k, v in colour.items() if len(v) > 1}, {})

    def test_the_key_colour_settings_are_in_welsh(self):
        ui = self.raw["packs"]["cy"]["meta"]["ui"]
        for key in ("keys_title", "keys_hint", "keys_colour", "keys_line", "keys_off"):
            self.assertTrue(ui.get(key), key)


class ThemingTests(unittest.TestCase):
    """The app owns the Welsh colours and inherits the framework's schemes."""

    WELSH = ("red-green", "yellow-green", "yellow-green-safe", "yellow-green-high-contrast")

    @classmethod
    def setUpClass(cls):
        import tempfile
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        phrasebook.build(cls.tmp / "dist")
        cls.raw = content.read(PROJECT)
        cls.page = (cls.tmp / "dist" / "settings.html").read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        import shutil
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def offered(self):
        return re.findall(r'name="palette" value="([a-z-]+)"', self.page)

    def test_the_red_and_green_of_the_welsh_flag_is_the_default(self):
        edition = json.loads((PROJECT / "editions" / "cydymaith.json").read_text(encoding="utf-8"))
        self.assertEqual(edition["default_palette"], "red-green")
        self.assertNotIn("palettes", edition, "the app inherits every framework scheme, so it keeps no list")
        self.assertIn('name="palette" value="red-green" data-pref="palette" checked', self.page)

    def test_the_welsh_schemes_are_the_apps_own_and_come_first(self):
        self.assertEqual(sorted(p.stem for p in (PROJECT / "palettes").glob("*.json")), sorted(self.WELSH))
        self.assertEqual(self.offered()[: len(self.WELSH)].count("red-green"), 1)
        self.assertEqual(set(self.offered()[: len(self.WELSH)]), set(self.WELSH))

    def test_the_framework_schemes_are_inherited_after_them(self):
        from phrasebook import palettes
        self.assertEqual(self.offered()[len(self.WELSH) :], list(palettes.ENGINE_ORDER))

    def test_the_safe_and_high_contrast_yellow_and_green_start_from_yellow_and_green(self):
        for name in ("yellow-green-safe", "yellow-green-high-contrast"):
            data = json.loads((PROJECT / "palettes" / f"{name}.json").read_text(encoding="utf-8"))
            self.assertEqual(data["extends"], "yellow-green", name)
            self.assertLess(len(data["light"]), 15, name)

    def test_every_scheme_the_app_offers_is_named_in_welsh(self):
        ui = self.raw["packs"]["cy"]["meta"]["ui"]
        for pid in self.raw["palettes"]:
            named = "cy" in self.raw["palettes"][pid].get("names", {}) or ui.get("palette_" + pid.replace("-", "_"))
            self.assertTrue(named, pid)

    def test_the_colour_schemes_are_named_by_their_colours_not_their_countries(self):
        for pid in ("blue-white-red", "green-white-red", "green-white-orange", "red-yellow", "black-red-gold"):
            text = json.dumps(self.raw["palettes"][pid]).lower()
            for country in ("france", "french", "ireland", "irish", "spain", "spanish", "germany", "german", "italy", "italian"):
                self.assertNotIn(country, text, (pid, country))


class ContrastStartTests(unittest.TestCase):
    """A first-time visitor whose device asks for more contrast starts on a palette they can read."""

    def test_every_page_names_the_welsh_high_contrast_scheme_as_the_start(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            phrasebook.build(pathlib.Path(tmp) / "dist")
            for page in (pathlib.Path(tmp) / "dist").glob("*.html"):
                self.assertIn('data-contrast-palette="yellow-green-high-contrast"', page.read_text(encoding="utf-8"), page.name)

    def test_the_help_for_it_is_in_both_languages(self):
        raw = content.read(PROJECT)
        help_en = json.loads((ROOT / "framework" / "phrasebook" / "help" / "en.json").read_text(encoding="utf-8"))
        self.assertIn("more contrast", " ".join(help_en["features"]["colour-schemes"]["body"]))
        self.assertIn("cyferbyniad", " ".join(raw["packs"]["cy"]["help"]["features"]["colour-schemes"]["body"]))
