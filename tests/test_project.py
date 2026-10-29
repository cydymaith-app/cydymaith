"""The Welsh project's own icons, tree and documents, built with the framework in framework/.

Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import json
import math
import pathlib
import re
import sys
import tempfile
import unicodedata
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "framework"))

import phrasebook  # noqa: E402
from phrasebook import colour, content, grading, icons, palettes  # noqa: E402
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
    """The weather topics link to the place phrases, and the places link back to how it is said. On a one-page group the related
    pages of every topic are one row of tiles at the bottom of the whole page, each once."""

    WEATHER, GEOGRAPHY = "group-weather-forecast.html", "group-geography.html"

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        cls.raw = raw
        cls.site = phrasebook.Site(raw, edition)
        cls.pages = cls.site.render_all()

    def row(self, name):
        page = self.pages[name]
        return page[page.index('<section class="related"') :]

    def tiles(self, name):
        return re.findall(r'<a class="tile-link" href="([^"]+)" data-related>', self.row(name))

    def test_the_weather_page_ends_with_one_row_of_related_pages_each_once(self):
        tiles = self.tiles(self.WEATHER)
        self.assertEqual(len(tiles), len(set(tiles)))
        self.assertEqual(
            set(tiles),
            {
                "group-geography.html#points",  # from Wind
                "group-geography.html#topic-compass",  # the group's own link
            },
        )
        self.assertEqual(self.pages[self.WEATHER].count('<section class="related"'), 1)

    def test_the_row_is_after_every_topic_and_none_is_inside_one(self):
        page = self.pages[self.WEATHER]
        self.assertLess(page.rindex("</details>"), page.index('<section class="related"'))
        topics = page[page.index('<div class="topics">') : page.index('<section class="related"')]
        self.assertNotIn('class="related"', topics)

    def test_geography_links_back_to_the_weather_and_not_to_its_own_topics(self):
        """Pages of the one Geography page are an accordion apart, so only the links out to the weather make tiles."""
        tiles = self.tiles(self.GEOGRAPHY)
        self.assertEqual(len(tiles), len(set(tiles)))
        self.assertEqual(
            set(tiles),
            {"group-weather-forecast.html#topic-patterns"},  # from the Compass; Landscape, which linked to Rain and Snow and ice, is gone
        )

    def test_the_tile_is_named_for_the_section_in_welsh_and_english(self):
        row = self.row(self.WEATHER)
        self.assertIn("Pynciau cysylltiedig", row)
        self.assertIn("Related topics", row)
        self.assertIn('<span class="l1" lang="cy">Cwmpawd</span><span class="l2">Compass</span>', row)


    def test_every_section_a_tile_lands_on_is_on_the_page_it_opens(self):
        for name, page in self.pages.items():
            for href in re.findall(r'href="([a-z0-9-]+\.html)#([A-Za-z0-9._-]+)" data-related', page):
                target = self.pages[href[0]]
                self.assertIn(f'id="{href[1]}"', target, f"{name} -> {href}")

    def test_pages_with_nothing_related_have_no_row(self):
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
        self.assertGreater(self.sections[("compass", "which-part")]["level"], points)
        self.assertGreater(self.sections[("compass", "from-which-way")]["level"], points)

    def test_sentences_are_the_most_advanced_and_single_words_the_simplest(self):
        self.assertEqual(self.pages["patterns"]["level"], 3)
        self.assertEqual(self.pages["sky"]["level"], 3, "the weather cards hold forecast phrases, not single words (2026-10-27)")
        self.assertEqual(self.pages["place-name-elements"]["level"], 1)
        self.assertEqual(self.sections[("patterns", "it-will-be")]["level"], 3)
        self.assertLess(self.pages["place-name-elements"]["level"], self.pages["patterns"]["level"])


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


class YellowGreenPaletteTests(unittest.TestCase):
    """The yellow and green schemes are consistent in OKLCH (2026-10-28): every colour is written in OKLCH, the green tint is one hue
    in light and dark, each key colour keeps its hue in both, and no key is mistaken for the accent."""

    IDS = ("yellow-green", "yellow-green-safe", "yellow-green-high-contrast")

    @classmethod
    def setUpClass(cls):
        cls.raw = palettes.load(PROJECT / "palettes")
        cls.files = {pid: json.loads((PROJECT / "palettes" / f"{pid}.json").read_text(encoding="utf-8")) for pid in cls.IDS}

    def test_every_colour_is_written_in_oklch(self):
        for pid, palette in self.files.items():
            for variant in ("light", "dark"):
                for role, text in palette.get(variant, {}).items():
                    if text.startswith("#"):
                        self.assertEqual(text, "", f"{pid} {variant} {role} is hex")

    def test_the_green_tint_of_the_neutrals_is_the_same_hue_in_light_and_dark(self):
        for pid in ("yellow-green", "yellow-green-high-contrast"):
            resolved = palettes.resolve(self.raw[pid])
            for variant in ("light", "dark"):
                for role in ("bg", "ink", "surface"):
                    self.assertAlmostEqual(self.hue_of(resolved[variant][role]), 175, delta=6, msg=(pid, variant, role))

    def hue_of(self, rgb):
        a, b = colour.rgb_to_oklab(rgb)[1:]
        return math.degrees(math.atan2(b, a)) % 360

    def test_each_key_colour_keeps_its_hue_between_light_and_dark(self):
        for pid in ("yellow-green", "yellow-green-high-contrast"):
            for key in palettes.KEYS_OF_WORDS:
                light, dark = (self.hue_of(palettes.resolve(self.raw[pid])[v][key]) for v in ("light", "dark"))
                self.assertAlmostEqual(light, dark, delta=6, msg=(pid, key))

    def test_no_key_colour_is_mistaken_for_the_accent(self):
        for pid in self.IDS:
            for variant, colours in palettes.resolve(self.raw[pid]).items():
                for key in palettes.KEYS_OF_WORDS:
                    self.assertGreaterEqual(colour.distance(colours["accent"], colours[key]), palettes.SEPARATION, (pid, variant, key))


class TimeAndDateSpreadTests(unittest.TestCase):
    """The Time and date page was dropped from Everyday on 2026-10-29. Its words went into the forecast phrases, so a learner finds
    each one where it is used; nothing it held may be lost."""

    WEATHER = ("sky", "rain", "snow-ice", "wind", "temperature", "change", "patterns", "talk", "compass")
    WORDS = [
        "Yr oriau nesaf", "Heddiw", "Heno", "Yfory", "Bore fory", "Nos yfory", "Yn hwyrach", "Y dyddiau nesaf", "Yr wythnos hon",
        "Gweddill yr wythnos", "Y penwythnos", "Yr wythnos nesaf", "Bore", "Prynhawn", "Min nos", "Nos", "Hanner nos", "Oriau mân",
        "Dros nos", "Drwy'r dydd", "Diwrnod", "Yn ystod", "Am gyfnod", "Cyn", "Erbyn", "Tan", "Ar ôl",
        "Dydd Llun", "Dydd Mawrth", "Dydd Mercher", "Dydd Iau", "Dydd Gwener", "Dydd Sadwrn", "Dydd Sul",
        "Gwanwyn", "Haf", "Hydref", "Gaeaf", "Tymor",
    ]

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)
        cls.texts = [
            unicodedata.normalize("NFC", t).casefold()
            for slug in cls.WEATHER
            for sec in cls.raw["packs"]["cy"]["pages"][slug]["sections"].values()
            for c in sec["concepts"].values()
            for t in [c.get("text", ""), *c.get("also", [])]
        ]

    def test_the_page_is_gone_and_nothing_links_to_it(self):
        self.assertNotIn("when", self.raw["pages"])
        self.assertNotIn("when", self.raw["packs"]["cy"]["pages"])
        for slug, page in self.raw["pages"].items():
            self.assertNotIn("when", page.get("related", []), slug)
        for group in self.raw["structure"]["groups"]:
            self.assertNotIn("when", group["pages"])

    def test_every_time_and_date_word_is_found_inside_a_weather_phrase(self):
        for word in self.WORDS:
            found = re.compile(r"(?<![\w'])" + re.escape(unicodedata.normalize("NFC", word).casefold()) + r"(?!\w)")
            self.assertTrue(any(found.search(t) for t in self.texts), f"{word} is in no weather phrase")

    def test_the_days_and_seasons_are_phrases_and_each_day_keeps_its_plain_form(self):
        days = self.raw["packs"]["cy"]["pages"]["patterns"]["sections"]["days"]["concepts"]
        self.assertEqual(len(days), 7)
        for name in ("Llun", "Mawrth", "Mercher", "Iau", "Gwener", "Sadwrn", "Sul"):
            self.assertTrue(any(name in c["text"] and f"dydd {name}" in " ".join([c["text"], *c.get("also", [])]) for c in days.values()), name)
        for row in [*days.values(), *self.raw["packs"]["cy"]["pages"]["patterns"]["sections"]["seasons"]["concepts"].values()]:
            self.assertGreater(len(row["text"].split()), 1, f"{row['text']} is a single word, not a phrase")


class TalkingAboutTheWeatherTests(unittest.TestCase):
    """Small talk was too small for a card, so on 2026-10-29 it joined Asking as one card, and the page moved into the weather group."""

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)

    def test_the_page_is_one_card_of_asking_and_chatting_in_the_weather_group(self):
        groups = {g["id"]: g for g in self.raw["structure"]["groups"]}
        self.assertEqual(groups["weather-forecast"]["pages"][-1], "talk")
        self.assertNotIn("talk", groups["everyday"]["pages"])
        sections = self.raw["pages"]["talk"]["sections"]
        self.assertEqual([s["id"] for s in sections], ["asking-and-chatting"])
        self.assertEqual(len(sections[0]["concepts"]), 11, "every word kept")
        cy = self.raw["packs"]["cy"]["pages"]["talk"]["sections"]["asking-and-chatting"]
        en = self.raw["packs"]["en"]["pages"]["talk"]["sections"]["asking-and-chatting"]
        self.assertEqual((cy["title"], en["title"]), ("Gofyn a sgwrsio", "Asking and chatting"))
        self.assertTrue(cy["order"])

    def test_every_row_marks_its_key_words_in_both_languages_the_same_way(self):
        cy = self.raw["packs"]["cy"]["pages"]["talk"]["sections"]["asking-and-chatting"]["concepts"]
        en = self.raw["packs"]["en"]["pages"]["talk"]["sections"]["asking-and-chatting"]["concepts"]
        for cid, row in cy.items():
            self.assertTrue(any(row["keys"]), cid)
            self.assertEqual([k is None for k in row["keys"]], [k is None for k in en[cid]["keys"]], cid)

    def test_a_word_keeps_the_colour_it_has_on_the_weather_pages(self):
        slot = {}
        for slug in ("sky", "rain", "snow-ice", "wind", "temperature", "change", "patterns"):
            for sec in self.raw["packs"]["en"]["pages"][slug]["sections"].values():
                for c in sec["concepts"].values():
                    for n, key in enumerate(c.get("keys", [])):
                        if key is not None:
                            slot.setdefault(key.casefold(), n)
        talk = self.raw["packs"]["en"]["pages"]["talk"]["sections"]["asking-and-chatting"]["concepts"]
        for cid, row in talk.items():
            for n, key in enumerate(row["keys"]):
                if key is not None and key.casefold() in slot:
                    self.assertEqual(n, slot[key.casefold()], f"{cid}: {key}")


class NoDoubleEntriesTests(unittest.TestCase):
    """A row says a thing once. A note is commentary, written once in the Welsh pack; the same note in the English pack as well
    showed twice under the row (found on the Snow card, 2026-10-29)."""

    @classmethod
    def setUpClass(cls):
        raw = select(content.read(PROJECT))
        _, edition = content.pick_edition(raw)
        cls.raw = raw
        cls.pages = phrasebook.Site(raw, edition).render_all()

    @staticmethod
    def plain(html):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html)).strip()

    def test_no_row_has_a_note_in_both_packs(self):
        both = []
        for slug, page in self.raw["packs"]["cy"]["pages"].items():
            for sid, section in page["sections"].items():
                other = self.raw["packs"]["en"]["pages"].get(slug, {}).get("sections", {}).get(sid, {}).get("concepts", {})
                both += [f"{slug}/{sid}/{cid}" for cid, c in section["concepts"].items() if c.get("note") and other.get(cid, {}).get("note")]
        self.assertEqual(both, [], "a note belongs in one pack only (the Welsh one, where {{ }} marks the Welsh words)")

    def test_no_row_on_any_card_shows_the_same_note_twice(self):
        twice = []
        for name, page in self.pages.items():
            for row in re.findall(r'<tr id="([^"]+)">(.*?)</tr>', page, flags=re.S):
                notes = [self.plain(n) for n in re.findall(r'<small class="note">(.*?)</small>', row[1], flags=re.S)]
                if len(notes) != len(set(notes)):
                    twice.append(f"{name}#{row[0]}")
        self.assertEqual(twice, [], "a row shows a note twice")

    def test_no_card_lists_the_same_phrase_twice(self):
        twice = []
        for slug, page in self.raw["packs"]["cy"]["pages"].items():
            for sid, section in page["sections"].items():
                texts = [c.get("text") for c in section["concepts"].values() if c.get("text")]
                twice += [f"{slug}/{sid}: {t}" for t in set(texts) if texts.count(t) > 1]
        self.assertEqual(twice, [], "a card has the same Welsh twice")


class TemperatureAndPressureTests(unittest.TestCase):
    """Uploads 13 and 14 (2026-10-29): the temperature said in full, falling and double figures, and the pressure that influences the weather."""

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)

    def rows(self, slug, sid, code="cy"):
        return self.raw["packs"][code]["pages"][slug]["sections"][sid]["concepts"]

    def test_a_temperature_is_written_in_full_and_found_by_the_form_on_screen(self):
        rows = self.rows("temperature", "figures")
        self.assertEqual(rows["about-15-degrees-celsius-at-the-highest"]["text"], "Rhyw 15 gradd Celsius ar ei uchaf")
        self.assertIn("rhyw 15C", rows["about-15-degrees-celsius-at-the-highest"]["also"])
        self.assertIn("rhwng 13C ac 16C", rows["between-13-and-16-degrees-celsius"]["also"])
        self.assertIn("yn disgyn i 8C", rows["the-temperature-falling-to-8-degrees-celsius"]["also"])
        for row in rows.values():
            self.assertNotRegex(row["text"], r"\dC", "the text is the spoken form, never the caption form")

    def test_the_pressure_card_has_the_influence_and_the_map_labels_are_forms(self):
        rows = self.rows("change", "pressure")
        self.assertIn("under-the-influence-of-high-pressure", rows)
        self.assertEqual(rows["high-pressure-influencing-the-weather"]["text"], "Gwasgedd uchel yn parhau i ddylanwadu ar y tywydd")
        self.assertIn("Uchel", rows["high-pressure-in-charge"]["also"])
        self.assertIn("Isel", rows["an-area-of-intense-low-pressure"]["also"])
        self.assertEqual(rows["a-series-of-fronts-spreading-over-wales"]["text"], "Cyfres o ffryntiau wedi lledu dros Gymru")

    def test_a_word_keeps_its_colour_on_the_new_rows_as_on_the_old_ones(self):
        colour = {}
        for slug in ("sky", "rain", "snow-ice", "wind", "temperature", "change", "patterns"):
            for sec in self.raw["packs"]["en"]["pages"][slug]["sections"].values():
                for c in sec["concepts"].values():
                    for n, key in enumerate(c.get("keys", [])):
                        if key is not None and key.casefold() in ("high pressure", "temperature", "falling", "highest", "front", "fronts"):
                            colour.setdefault(key.casefold().rstrip("s"), set()).add(n)
        self.assertEqual({k: v for k, v in colour.items() if len(v) > 1}, {})


class SportScaffoldTests(unittest.TestCase):
    """The Sport group is shaped like the weather (2026-10-27): one page of topics, every section with a stated order, and all of it
    held back until the words heard on air replace the seed rows (docs/SPORT-WORDS.md)."""

    PAGES = ["football", "rugby", "results", "competitions", "sport-patterns"]

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)
        cls.groups = {g["id"]: g for g in cls.raw["structure"]["groups"]}

    def test_sport_is_one_page_of_football_rugby_and_the_shared_topics(self):
        sport = self.groups["sport"]
        self.assertEqual(sport["layout"], "one-page")
        self.assertEqual(sport["pages"], self.PAGES)
        self.assertNotIn("sport", self.raw["pages"], "the placeholder page is gone")

    def test_numbers_is_an_everyday_page_for_the_scores_and_the_forecast(self):
        self.assertEqual(self.groups["everyday"]["pages"], ["numbers", "food-drink"])
        self.assertIn("numbers", self.raw["pages"]["results"]["related"])

    def test_every_section_is_held_back_and_states_its_order(self):
        for slug in [*self.PAGES, "numbers"]:
            for section in self.raw["pages"][slug]["sections"]:
                self.assertEqual(section.get("status"), "development", f"{slug}/{section['id']}")
                cy = self.raw["packs"]["cy"]["pages"][slug]["sections"][section["id"]]
                self.assertTrue(cy.get("order"), f"{slug}/{section['id']} has no order")

    def test_section_and_concept_ids_are_unique_on_the_one_page(self):
        sections = [s["id"] for slug in self.PAGES for s in self.raw["pages"][slug]["sections"]]
        concepts = [c for slug in self.PAGES for s in self.raw["pages"][slug]["sections"] for c in s["concepts"]]
        self.assertEqual(len(sections), len(set(sections)))
        self.assertEqual(len(concepts), len(set(concepts)))

    def test_every_row_is_in_both_languages_and_marked_as_a_draft(self):
        for slug in [*self.PAGES, "numbers"]:
            for code in ("cy", "en"):
                pack = self.raw["packs"][code]["pages"][slug]
                self.assertEqual(pack["source"], "draft", f"{code} {slug}")
                for section in self.raw["pages"][slug]["sections"]:
                    self.assertEqual(list(pack["sections"][section["id"]]["concepts"]), section["concepts"], f"{code} {slug}")

    def test_the_release_has_no_sport_and_no_numbers(self):
        released = select(self.raw)
        self.assertNotIn("sport", {g["id"] for g in released["structure"]["groups"]})
        self.assertNotIn("numbers", released["pages"])


class GeographyStandardTests(unittest.TestCase):
    """The Geography pages are held to the standard of the weather pages (2026-10-27): every section states its order, the names a
    listener hears after a preposition are findable, and the page of forecast phrases is apart from the one for reading names."""

    WELSH = ["a", "b", "c", "ch", "d", "dd", "e", "f", "ff", "g", "ng", "h", "i", "l", "ll", "m", "n", "o", "p", "ph", "r", "rh", "s", "t", "th", "u", "w", "y"]

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)

    def welsh_order(self, word):
        """Sort key in the Welsh alphabet, where ch, dd, ff, ng, ll, ph, rh and th are letters of their own."""
        word, key, n = word.casefold(), [], 0
        while n < len(word):
            pair = word[n : n + 2]
            letter = pair if pair in self.WELSH else word[n]
            key.append(self.WELSH.index(letter) if letter in self.WELSH else len(self.WELSH))
            n += len(letter)
        return key

    def section(self, slug, sid):
        return self.raw["packs"]["cy"]["pages"][slug]["sections"][sid]

    def skeleton(self, slug, sid):
        return next(s["concepts"] for s in self.raw["pages"][slug]["sections"] if s["id"] == sid)

    def test_every_geography_section_states_its_order(self):
        for slug in ("compass", "place-name-elements"):
            for sid, section in self.raw["packs"]["cy"]["pages"][slug]["sections"].items():
                self.assertTrue(section.get("order"), f"{slug}/{sid} has no order")

    def test_there_is_no_place_names_page_because_a_list_of_places_can_never_be_complete(self):
        """Removed on 2026-10-28: the towns heard after yn and the landmarks. Landmarks joined Landscape; no list of places is kept."""
        self.assertNotIn("geography", self.raw["pages"])
        self.assertNotIn("geography", self.raw["packs"]["cy"]["pages"])
        self.assertNotIn("geography", next(g for g in self.raw["structure"]["groups"] if g["id"] == "geography")["pages"])

    def test_a_region_is_one_row_heard_after_in_and_the_plain_name_is_another_way_it_is_heard(self):
        regions = {
            cid: c
            for sid in ("from-which-way", "which-part", "parts-of-wales")
            for cid, c in self.section("compass", sid)["concepts"].items()
            if cid.endswith("-wales")
        }
        self.assertEqual(len(regions), 9)  # south-west Wales was added on 2026-10-28, a draft not heard on air
        self.assertEqual(regions["in-north-wales"]["text"], "Yng ngogledd Cymru")
        self.assertIn("Gogledd Cymru", regions["in-north-wales"]["also"])
        self.assertIn("Yng Nghymru", regions["across-wales"]["also"])

    def test_landscape_is_spread_into_the_weather_phrases_and_the_page_is_gone(self):
        """2026-10-29: the place words are inside forecast phrases, so Landscape was dropped and nothing links to it."""
        self.assertNotIn("landscape", self.raw["pages"])
        self.assertNotIn("landscape", self.raw["packs"]["cy"]["pages"])
        for slug, page in self.raw["pages"].items():
            self.assertNotIn("landscape", page.get("related", []), slug)
        texts = [
            unicodedata.normalize("NFC", t).casefold()
            for slug in ("sky", "rain", "snow-ice", "wind", "temperature", "change", "patterns", "talk")
            for sec in self.raw["packs"]["cy"]["pages"][slug]["sections"].values()
            for c in sec["concepts"].values()
            for t in [c.get("text", ""), *c.get("also", [])]
        ]
        for word in ("arfordir", "arfordirol", "ardaloedd", "glannau", "Ceredigion", "Môr Iwerddon", "Môr Hafren", "mewndiroedd", "cymoedd",
                     "bryniau", "dir uchel", "mynyddoedd", "Dyffryn Conwy", "Dyffryn Clwyd", "Eryri", "Bannau Brycheiniog", "Ynys Môn", "Pen Llŷn"):
            found = re.compile(r"(?<![\w'])" + re.escape(unicodedata.normalize("NFC", word).casefold()) + r"(?!\w)")
            self.assertTrue(any(found.search(t) for t in texts), f"{word} is in no weather phrase")

    def test_the_compass_has_one_card_for_each_way_a_forecast_uses_a_direction(self):
        """2026-10-28: the cards were by kind, not by point: which way it comes from, which part, and which part of Wales."""
        from_ = list(self.section("compass", "from-which-way")["concepts"])
        self.assertEqual(from_, [f"from-the-{d}" for d in ("north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west")])
        self.assertEqual(list(self.section("compass", "which-part")["concepts"])[:4],
                         ["in-the-north", "in-the-east", "in-the-south", "in-the-west"])
        wales = list(self.section("compass", "parts-of-wales")["concepts"])
        self.assertEqual(wales[:2], ["in-north-wales", "in-north-east-wales"])
        self.assertEqual(wales[-2:], ["across-wales", "across-the-whole-country"])
        self.assertIn("in-south-west-wales", wales)

    def test_every_compass_direction_is_the_first_key_word_so_it_keeps_its_colour(self):
        for code in ("cy", "en"):
            for sid in ("from-which-way", "which-part", "parts-of-wales"):
                for cid, c in self.raw["packs"][code]["pages"]["compass"]["sections"][sid]["concepts"].items():
                    if cid.startswith(("across", "further")):
                        continue
                    self.assertIsNotNone(c["keys"][0], (code, cid))

    def test_no_geography_key_word_is_a_function_word(self):
        function_words = {"o'r", "dros", "ar hyd", "ledled", "from", "over", "along", "across"}
        for slug in ("compass",):
            for code in ("cy", "en"):
                for section in self.raw["packs"][code]["pages"][slug]["sections"].values():
                    for cid, concept in section["concepts"].items():
                        for key in concept.get("keys", []):
                            self.assertNotIn((key or "").casefold(), function_words, f"{code} {slug}/{cid}")


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

    GEOGRAPHY = ("compass", "place-name-elements")
    MARKED = {
        "compass": {"from-which-way", "which-part", "parts-of-wales"},
        "place-name-elements": set(),
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


class UploadTwelveTests(unittest.TestCase):
    """The phrases of upload 12 (27 October 2026): flooding, the place-first pattern, the forecast map, and rivers named in phrases."""

    @classmethod
    def setUpClass(cls):
        cls.raw = content.read(PROJECT)

    def ids(self, slug):
        return [s["id"] for s in self.raw["pages"][slug]["sections"]]

    def concepts(self, slug, sid):
        return next(s for s in self.raw["pages"][slug]["sections"] if s["id"] == sid)["concepts"]

    def test_rain_has_a_flooding_card_between_rain_and_thunder_and_the_risk_of_flooding_moved_there(self):
        self.assertEqual(self.ids("rain"), ["rain", "flooding", "storms"])
        self.assertEqual(self.concepts("rain", "flooding")[0], "a-risk-of-flooding")
        self.assertNotIn("a-risk-of-flooding", self.concepts("rain", "rain"))

    def test_how_its_said_puts_the_place_first_after_there_will_be(self):
        ids = self.ids("patterns")
        self.assertEqual(ids[ids.index("there-will-be") + 1], "place-first")
        self.assertNotIn("status", next(s for s in self.raw["pages"]["patterns"]["sections"] if s["id"] == "place-first"))

    PLACE_PHRASES = [
        ("patterns", "extent", "in-coastal-areas"), ("patterns", "extent", "showers-in-pembrokeshire-llyn-and-anglesey"),
        ("rain", "storms", "big-waves-along-the-shores"), ("rain", "storms", "rough-weather-along-the-severn-estuary"),
        ("change", "which-way", "showers-reaching-cardigan-bay"), ("change", "which-way", "rain-crossing-the-irish-sea"),
        ("temperature", "hot-cold", "colder-inland"), ("sky", "fog", "fog-in-the-conwy-valley"), ("rain", "flooding", "flooding-in-the-vale-of-clwyd"),
        ("snow-ice", "snow", "snow-over-snowdonia"), ("snow-ice", "frost-ice", "frost-in-the-brecon-beacons"),
    ]

    def test_no_card_is_a_list_of_place_names(self):
        """No gazetteers (rule 7 in docs/PHILOSOPHY.md): a place is named inside a phrase, never as a row of its own.
        The place-name elements are the exception, since they teach how names are built."""
        for slug, sid, cid in self.PLACE_PHRASES:
            text = self.raw["packs"]["cy"]["pages"][slug]["sections"][sid]["concepts"][cid]["text"]
            self.assertGreater(len(text.split()), 2, f"{slug}/{sid}/{cid}: {text!r} is too short to be a phrase")
        for page in ("geography", "landscape"):
            self.assertNotIn(page, self.raw["packs"]["cy"]["pages"])

    def test_a_river_is_named_in_a_phrase_and_never_listed_on_its_own(self):
        """There are too many rivers in Wales to list, so one is only ever part of a phrase (2026-10-28)."""
        welsh = {
            c.get("text", "")
            for slug in ("rain", "sky")
            for s in self.raw["packs"]["cy"]["pages"][slug]["sections"].values()
            for c in s["concepts"].values()
        }
        for phrase in ("Rhybudd llifogydd ar Afon Tywi", "Afon Clwyd yn uchel yn Rhuddlan", "Niwl yn Nyffryn Conwy", "Tywydd garw ar hyd Môr Hafren"):
            self.assertIn(phrase, welsh)
        for slug, page in self.raw["packs"]["cy"]["pages"].items():
            for s in page["sections"].values():
                for cid, c in s["concepts"].items():
                    self.assertNotRegex(c.get("text", ""), r"^Afon \w+$", f"{slug}/{cid}: a river on its own")

    def test_every_new_weather_row_marks_its_key_words_in_both_languages(self):
        new = {
            "sky": ["a-cloudy-day-on-the-whole", "sunshine-and-showers", "foggy-in-the-morning", "more-settled-by-wednesday"],
            "rain": ["a-risk-of-rain", "river-levels-are-high", "some-have-already-seen-flooding"],
            "wind": ["the-worst-of-the-wind-overnight", "there-are-warnings-in-force"],
            "change": ["a-front-bringing-more-rain", "the-isobars-closing-up", "a-band-of-heavy-rain-moving-east"],
            "patterns": ["the-west-will-see-the-worst", "the-north-had-the-best-of-the-sunshine"],
        }
        for slug, cids in new.items():
            for code in ("cy", "en"):
                found = {
                    cid: c
                    for s in self.raw["packs"][code]["pages"][slug]["sections"].values()
                    for cid, c in s["concepts"].items()
                }
                for cid in cids:
                    self.assertTrue(found[cid].get("keys"), (slug, code, cid))

    def test_no_storm_is_named(self):
        for code in ("cy", "en"):
            for slug in ("sky", "rain", "wind", "change", "patterns"):
                self.assertNotRegex(json.dumps(self.raw["packs"][code]["pages"][slug], ensure_ascii=False), r"Storm [A-Z]")
