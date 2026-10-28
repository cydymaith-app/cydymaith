"""Tests of the Welsh project's content and of the framework running on it.

The framework itself is tested on a neutral made-up project in test_framework.py.
Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import copy
import json
import pathlib
import re
import shutil
import sys
import tempfile
import unittest
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "framework"))

import phrasebook  # noqa: E402
from phrasebook import channels  # noqa: E402
from phrasebook import channels  # noqa: E402
from phrasebook import content as C  # noqa: E402

PROJECT = ROOT / "content" / "cydymaith"


class build:  # noqa: N801  a namespace, so the tests read as they did before the framework was split out
    ContentError = C.ContentError
    LANG_CODE = C.LANG_CODE
    Site = phrasebook.Site
    validate = staticmethod(C.validate)
    pick_edition = staticmethod(C.pick_edition)
    draft_sources = staticmethod(C.draft_sources)
    coverage = staticmethod(C.coverage)

    @staticmethod
    def read(project=PROJECT):
        return C.read(project)

    @staticmethod
    def build(out, data_dir=PROJECT, **kw):
        return phrasebook.build(out, project_dir=data_dir, **kw)

# Entry counts when the site was first restructured. Content may grow, never shrink by accident. Lowered on 2026-10-27, by decision:
# the weather cards hold forecast phrases in place of single words, and The forecast card (warnings) is gone.
ENTRY_FLOOR = {"sky": 17, "rain": 12, "snow-ice": 9, "wind": 18, "temperature": 13, "when": 24, "compass": 22, "patterns": 34, "talk": 11, "geography": 20, "landscape": 14, "place-name-elements": 50}


class Page(HTMLParser):
    """Collects ids, links, the current-page marker and Welsh spans from one built page."""

    def __init__(self, text):
        super().__init__()
        self.ids, self.hrefs, self.cy, self.current = [], [], [], 0
        self._cy_open = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a" and "href" in a:
            self.hrefs.append(a["href"])
        if a.get("aria-current") == "page":
            self.current += 1
        if a.get("lang") == "cy":
            self._cy_open = {"text": ""}
            self.cy.append(self._cy_open)

    def handle_endtag(self, tag):
        if tag in ("span", "p"):
            self._cy_open = None

    def handle_data(self, data):
        if self._cy_open is not None:
            self._cy_open["text"] += data


def topic_html(site, pages, slug):
    """A topic as the reader gets it: its own page, or on a one-page group (the weather forecast) its accordion on the group's page."""
    page = pages[site.href(slug).split("#")[0]]
    if slug not in site.homes:
        return page
    start = page.index(f'<details class="fold topic" aria-labelledby="h-topic-{slug}"')
    end = page.find('<details class="fold topic"', start + 1)
    return page[start : end if end != -1 else page.index("<script>", start)]


def pages_written(site):
    """Every page file: each topic with a page of its own, each group, and twelve more (home, sources, how to use, seven help
    chapters, settings, about)."""
    return len([s for s in site.slugs if s not in site.homes]) + len(site.groups) + 12


def add_pack(data_dir, code, name, direction="ltr", pages=None, edition=None):
    """Write a minimal extra language pack into a copy of the data, and optionally an edition using it.

    pages is {page slug: {section id: [concept ids to translate]}}. Texts are generated as '<code>:<concept>'.
    """
    data_dir = pathlib.Path(data_dir)
    structure = json.loads((data_dir / "structure.json").read_text(encoding="utf-8"))
    meta = {"code": code, "name": name, "dir": direction,
            "ui": {"endonym": name, "home": f"{code}-home", "main_menu": f"{code}-menu",
                   "sources": f"{code}-sources", "phrasebook": f"{code}-book"},
            "groups": {g["id"]: f"{code}-{g['id']}" for g in structure["groups"]},
            "sources": [{"id": "own", "title": "Written by the test author", "licence": "own"}]}
    pack = data_dir / "packs" / code
    (pack / "pages").mkdir(parents=True)
    (pack / "pack.json").write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    for slug, sections in (pages or {}).items():
        page = {"title": f"{code}-{slug}", "source": "own", "sections": {
            sid: {"title": f"{code}-{sid}", "concepts": {c: {"text": f"{code}:{c}"} for c in cids}}
            for sid, cids in sections.items()}}
        (pack / "pages" / f"{slug}.json").write_text(json.dumps(page, ensure_ascii=False), encoding="utf-8")
    if edition:
        ed = {"name": edition, "languages": ["en", "cy", code], "interface": "en", "default_pair": ["en", code],
              "home": {"headline": {"en": "English headline", "cy": "Pennawd", code: f"{code} headline"}}}
        (data_dir / "editions" / "test.json").write_text(json.dumps(ed), encoding="utf-8")


class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.out = cls.tmp / "dist"
        cls.count = build.build(cls.out)
        cls.raw = build.read()
        _, cls.edition = build.pick_edition(cls.raw)
        cls.site = build.Site(channels.select(cls.raw), cls.edition)  # what the release publishes
        cls.built = {f.name: f.read_text(encoding="utf-8") for f in cls.out.glob("*.html")}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_every_page_is_written(self):
        self.assertEqual(self.count, pages_written(self.site))
        self.assertEqual(set(self.built), {"index.html", "sources.html", "how-to.html", "help-finding-your-way.html", "help-looking-up-words.html", "help-reading-a-topic.html", "help-your-settings.html", "help-arranging-tiles.html", "help-offline-and-install.html", "help-using-help.html", "settings.html", "about.html"} | {f"{s}.html" for s in self.site.slugs if s not in self.site.homes} | {f"group-{g['id']}.html" for g in self.site.groups})
        self.assertTrue((self.out / "style.css").is_file())

    def test_the_site_installs(self):
        manifest = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], self.site.name)
        self.assertTrue(manifest["short_name"])
        self.assertLessEqual(len(manifest["short_name"]), 12)
        self.assertEqual(manifest["display"], "standalone")
        sizes = {icon["sizes"] for icon in manifest["icons"]}
        self.assertEqual(sizes, {"192x192", "512x512"})
        self.assertIn("maskable", {icon["purpose"] for icon in manifest["icons"]})
        for icon in manifest["icons"]:
            self.assertTrue((self.out / icon["src"]).is_file(), icon["src"])
        # start_url must be exactly a precached file, not a bare directory: the cache only matches a
        # request's exact URL, so "./" would miss the cache and fail to launch offline.
        self.assertTrue((self.out / manifest["start_url"].lstrip("./")).is_file(), manifest["start_url"])
        for page in self.built.values():
            self.assertIn('<link rel="manifest" href="manifest.json">', page)
            self.assertIn('navigator.serviceWorker.register("sw.js")', page)

    def test_the_project_palette_records_where_its_colours_came_from(self):
        palette = json.loads((PROJECT / "palettes" / "red-green.json").read_text(encoding="utf-8"))
        self.assertIn("hellocolor.de", palette["notes"])
        self.assertIn("derived", palette["notes"].lower())
        assets = (ROOT / "docs" / "ASSETS.md").read_text(encoding="utf-8")
        self.assertIn("hellocolor.de", assets)

    def test_the_installed_app_wears_the_default_palette(self):
        manifest = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(self.site.default_palette, "red-green")
        palette = C.palettes.resolve(self.raw["palettes"]["red-green"])["light"]
        self.assertEqual(manifest["theme_color"], C.palettes.colour.rgb_to_hex(palette["accent"]))
        self.assertEqual(manifest["background_color"], C.palettes.colour.rgb_to_hex(palette["bg"]))

    def test_the_service_worker_precaches_every_built_file(self):
        sw = (self.out / "sw.js").read_text(encoding="utf-8")
        files = json.loads(re.search(r"const FILES = (\[.*\]);", sw).group(1))
        on_disk = {str(p.relative_to(self.out)).replace("\\", "/") for p in self.out.rglob("*")
                  if p.is_file() and p.name != "sw.js"}
        self.assertEqual(set(files), on_disk)
        self.assertRegex(sw, r'const CACHE = "phrasebook-[0-9a-f]{16}";')

    def test_the_weather_tiles_follow_what_a_forecast_talks_about_in_the_order_it_runs(self):
        weather = next(g for g in self.site.groups if g["id"] == "weather-forecast")
        self.assertEqual(weather["pages"], ["sky", "rain", "snow-ice", "wind", "temperature", "patterns"])

    def test_time_and_place_is_split_up_the_compass_is_geography_and_time_and_date_is_everyday_and_a_related_page_of_how_its_said(self):
        """Time and place was split on 2026-10-27: the compass went to Geography (one page), Time and date to Everyday."""
        weather = next(g for g in self.site.groups if g["id"] == "weather-forecast")
        everyday = next(g for g in self.site.groups if g["id"] == "everyday")
        self.assertNotIn("time-and-place", [g["id"] for g in self.site.groups])
        self.assertEqual(everyday["pages"], ["talk", "when", "food-drink"])
        self.assertEqual(weather["links"], ["compass"])
        page = self.built["group-weather-forecast.html"]
        tiles = page[page.rindex("</details>") : page.index('class="pager"')]  # the row of the pages the group links to
        self.assertNotIn('href="when.html"', tiles, "Time and date is reached from How it's said as a related page, not a group tile")
        self.assertIn('href="group-geography.html#topic-compass"', tiles)
        self.assertIn('href="when.html"', self.built["group-everyday.html"])
        self.assertIn('href="when.html" data-related', topic_html(self.site, self.built, "patterns"))  # moved here when The forecast went
        self.assertIn("Amser a dyddiad", self.built["when.html"])
        self.assertIn("Time and date", self.built["when.html"])

    def test_pressure_opens_change_and_movement_which_is_a_held_page_and_the_forecast_card_is_gone(self):
        """The forecast card was dropped on 2026-10-27; its pressure went to Change and movement, its warnings to the cards."""
        self.assertFalse((PROJECT / "pages" / "warnings.json").exists())
        change = json.loads((PROJECT / "pages" / "change.json").read_text(encoding="utf-8"))
        self.assertEqual([s["id"] for s in change["sections"]], ["pressure", "moving", "which-way", "changing", "other-verbs"])
        self.assertTrue(all(s.get("status") == "development" for s in change["sections"]), "the page stays held until reviewed")
        self.assertNotIn("change.html", self.built)
        patterns = json.loads((PROJECT / "pages" / "patterns.json").read_text(encoding="utf-8"))
        ids = [s["id"] for s in patterns["sections"]]
        self.assertFalse({"moving", "verbs", "pressure"} & set(ids), "these moved off How it's said")

    def test_the_settings_page_offers_the_three_accessibility_levels_each_with_its_own_schemes_in_welsh_and_english(self):
        page = self.built["settings.html"]
        self.assertIn('id="settings-lang-cy" value="cy" checked', page, "the Welsh shows first")
        self.assertIn('<h1><span class="t" data-n="1" lang="cy">Gosodiadau</span><span class="t" data-n="2">Settings</span></h1>', page)
        levels = {}
        for tier, pid in re.findall(r'data-tier="(\w+)"><input type="radio" name="palette" value="([\w-]+)"', page):
            levels.setdefault(tier, []).append(pid)
        self.assertEqual(levels, {
            # the app's own schemes first, then the framework's in its own order
            "standard": ["red-green", "yellow-green", "default", "blue-white-red", "green-white-red", "green-white-orange",
                         "red-yellow", "black-red-gold", "sepia"],
            "high": ["yellow-green-high-contrast", "high-contrast"],
            "safe": ["yellow-green-safe", "red-green-safe", "blue-yellow-safe", "monochrome"],
        })
        for welsh, english in (("Safonol", "Standard"), ("Lliwiau diogel", "Safe colours"), ("Cyferbyniad uchel", "High contrast")):
            self.assertIn(f'lang="cy">{welsh}</span><span class="t" data-n="2">{english}</span>', page)
        for name in ("Coch a gwyrdd", "Melyn a gwyrdd"):
            self.assertIn(name, page)

    def test_the_about_page_is_in_both_languages_and_links_to_the_sources(self):
        page = self.built["about.html"]
        self.assertIn('<article class="about-text" id="about-cy" lang="cy"><header><h1>Ynglŷn â Chydymaith am iaith</h1>', page)
        self.assertIn('<article class="about-text" id="about-en"><header><h1>About Cydymaith am iaith</h1>', page)
        self.assertIn('id="about-lang-cy" value="cy" checked', page, "the Welsh shows first")
        self.assertEqual(page.count('<a href="sources.html">'), 2)

    def test_technoleg_dda_is_held_back_from_the_release_until_its_text_is_reviewed(self):
        """Held back on 2026-10-27: the statement and the Hywel Dda text are not ready for the live site."""
        for words in ("Technoleg Dda", "Hywel", "docs/TECHNOLEG-DDA.md", "Nothing to sell"):
            self.assertNotIn(words, self.built["about.html"])
        page = build.Site(self.raw, self.edition).render_all()["about.html"]  # the development channel keeps it
        self.assertIn('<blockquote class="principle"><p>Technology should serve the person using it, and ask nothing in return.</p></blockquote>', page)
        self.assertIn("<blockquote class=\"principle\"><p>Dylai technoleg wasanaethu'r sawl sy'n ei defnyddio, heb ofyn dim yn ôl.</p></blockquote>".replace("'", "&#x27;"), page)
        for promise in ("Nothing to sell", "Nothing taken", "Nothing hidden", "No nagging", "For everyone", "Small and open", "People first",
                        "Dim i&#x27;w werthu", "Dim yn cael ei gymryd", "Dim yn gudd", "Dim swnian", "I bawb", "Bach ac agored", "Pobl yn gyntaf"):
            self.assertIn(promise, page)
        self.assertIn("no AI, because the app never calls an AI service or a language model", page)
        self.assertIn("docs/TECHNOLEG-DDA.md", page)

    def test_the_about_page_says_how_to_install_and_share_and_where_to_correct_the_welsh(self):
        page = self.built["about.html"]
        for words in ("Install it for offline use", "Ei osod i&#x27;w ddefnyddio all-lein", "Share it", "Ei rannu"):
            self.assertIn(words, page)
        self.assertEqual(page.count('class="share" data-url="https://cydymaith-app.github.io/cydymaith/"'), 2)
        self.assertEqual(page.count("issues/new?template=welsh-correction.md"), 2)
        self.assertTrue((ROOT / ".github" / "ISSUE_TEMPLATE" / "welsh-correction.md").is_file())

    def test_the_about_page_is_an_accordion_with_the_first_two_sections_open(self):
        page = self.built["about.html"]
        english = page[page.index('id="about-en"') :]
        opened = re.findall(r'<details class="fold" open><summary><h2>([^<]+)</h2>', english)
        self.assertEqual(opened, ["What it is for"])
        self.assertEqual(english.count('<details class="fold"'), 7, "the held-back sections are not in the release")

    def test_the_settings_page_groups_its_choices_in_folds_with_only_accessibility_and_appearance_open(self):
        page = self.built["settings.html"]
        self.assertEqual(len(re.findall(r'<details class="fold card"[^>]* open>', page)), 1)
        self.assertIn('<details class="fold card" aria-labelledby="h-look" open>', page)
        self.assertEqual(
            re.findall(r'<details class="fold card"[^>]*aria-labelledby="(h-[a-z-]+)"', page),
            ["h-look", "h-order-group", "h-var-cy"],
            "accessibility and appearance; order and tile layout; the Welsh regional forms",
        )

    def test_the_settings_groups_are_named_in_welsh_and_english(self):
        page = self.built["settings.html"]
        for words in (
            "Hygyrchedd a golwg", "Accessibility and appearance", "Modd gweld", "View mode",
            "Trefn a chynllun y teils", "Order and tile layout", "Cynllun y teils", "Tile layout",
        ):
            self.assertIn(words, page)

    def test_where_next_waits_for_the_links_to_be_checked(self):
        last = self.edition["about_page"]["en"]["sections"][-1]
        self.assertEqual((last["title"], last.get("status")), ("Where next", "development"))
        self.assertNotIn("learnwelsh.cymru", self.built["about.html"])
        self.assertNotIn("Where next", self.built["about.html"])

    def test_the_home_page_leaves_the_links_to_the_about_page_which_holds_them(self):
        """About this app and Sources and licences are linked from the About page only; every page has its information icon."""
        home = self.built["index.html"]
        self.assertNotIn("About this app", home)
        self.assertNotIn("Sources and licences", home)
        self.assertNotIn('href="sources.html"', home)
        self.assertEqual(home.count('href="about.html"'), 1, "only the rail's information icon")

    def test_the_about_page_links_to_how_to_and_the_sources_in_each_language(self):
        page = self.built["about.html"]
        self.assertEqual(page.count('<p class="about-more"><a href="how-to.html">'), 2)
        self.assertEqual(page.count('</a> · <a href="sources.html">'), 2)

    def test_no_page_but_about_links_to_how_to_or_the_sources_in_the_text(self):
        for name, page in self.built.items():
            if name == "about.html":
                continue
            for target in ("how-to.html", "sources.html"):
                if target == "how-to.html" and name.startswith("help-"):
                    continue  # a help chapter sits under the contents page, so its trail names it
                self.assertNotIn(f'<a href="{target}">', page, f"{name} links to {target}")

    def test_every_page_has_the_about_link_above_the_gear_and_the_trail_says_amdanom_ni(self):
        for name, page in self.built.items():
            rail = page[page.index('<nav class="rail"') : page.index("</nav>", page.index('<nav class="rail"'))]
            self.assertIn('href="about.html"', rail, name)
        self.assertIn("Amdanom ni", self.built["about.html"])

    def test_the_welsh_comes_first_because_it_is_the_language_that_is_heard(self):
        self.assertEqual(list(self.edition["default_pair"]), ["cy", "en"])
        self.assertIn('<th scope="row" class="l1" lang="cy"><span class="key" data-k="2">Glaw mân</span> yma ac acw</th>', topic_html(self.site, self.built, "rain"))

    def test_every_section_states_its_order(self):
        shown = {"sky": 3, "rain": 2, "snow-ice": 2, "wind": 3, "temperature": 3, "when": 4, "compass": 2, "geography": 3, "landscape": 3, "patterns": 6, "place-name-elements": 6}
        for slug, count in shown.items():
            self.assertEqual(topic_html(self.site, self.built, slug).count('<p class="order">'), count, slug)

    def test_a_word_heard_in_another_form_is_found_by_that_form(self):
        dictionary = json.loads((self.out / "dictionary.json").read_text(encoding="utf-8"))
        rain = next(e for e in dictionary["entries"] if e["concept"] == "spells-of-heavy-rain-as-well")
        self.assertIn("chyfnodau o law trwm", rain["also"]["cy"])
        self.assertIn("Cyfnodau o law trwm hefyd", [t["text"] for t in rain["terms"]["cy"]])

    def test_the_sentences_live_on_one_patterns_page_and_no_topic_repeats_an_in_a_sentence_section(self):
        for slug in self.site.slugs:
            self.assertNotIn("in-a-sentence", [s["id"] for s in self.site.sections(slug)], slug)
        self.assertEqual([s["id"] for s in self.site.sections("patterns")],
                         ["it-is", "doing", "it-will-be", "there-will-be", "wind-from", "extent"])

    def test_the_weather_group_holds_every_word_it_held_before_the_regrouping(self):
        slugs = ("sky", "rain", "snow-ice", "wind", "temperature", "when", "compass", "patterns", "talk")
        self.assertGreaterEqual(sum(self.site.count_entries(s) for s in slugs), 170)  # words only ever get added

    def test_geography_is_one_page_of_compass_place_names_landscape_and_the_place_name_elements(self):
        """Merged on 2026-10-27: Regions of Wales joined the place names. Later that day Landscape, a page of forecast phrases,
        was split from the place-name elements, which are for reading names and signs."""
        geography = next(g for g in self.site.groups if g["id"] == "geography")
        self.assertEqual(geography["layout"], "one-page")
        self.assertEqual(geography["pages"], ["compass", "geography", "landscape", "place-name-elements"])
        skeleton = self.site.skel["geography"]
        self.assertEqual([s["id"] for s in skeleton["sections"]], ["regions", "places", "uk"])
        self.assertTrue(all("status" not in s for s in skeleton["sections"]), "Geography is no longer held back")
        # one row per region as it is heard (the plain names are "also heard as"), so 11 region rows became 8
        self.assertEqual(self.site.count_entries("geography"), 20)
        self.assertEqual([s["id"] for s in self.site.skel["landscape"]["sections"]], ["coast", "inland", "named"])
        self.assertEqual([s["id"] for s in self.site.skel["compass"]["sections"]], ["points", "from", "directions"])

    def test_the_place_name_elements_are_found_by_the_forms_they_take_in_names(self):
        self.assertEqual([s["id"] for s in self.site.sections("place-name-elements")], ["settlements", "water", "hills", "land", "ways", "describing"])
        dictionary = json.loads((self.out / "dictionary.json").read_text(encoding="utf-8"))
        bridge = next(e for e in dictionary["entries"] if e["concept"] == "bridge")
        self.assertEqual([t["text"] for t in bridge["terms"]["cy"]], ["pont"])
        self.assertIn("bont", bridge["also"]["cy"])

    def test_entry_counts_do_not_shrink(self):
        for slug, floor in ENTRY_FLOOR.items():
            self.assertGreaterEqual(self.site.count_entries(slug), floor, f"{slug} lost entries")

    def test_the_tiles_link_every_group_and_topic_and_show_no_counts(self):
        for group in self.site.groups:
            self.assertIn(f'href="group-{group["id"]}.html"', self.built["index.html"])
            page = self.built[f"group-{group['id']}.html"]
            for slug in group["pages"]:  # a tile, or on a one-page group an accordion
                self.assertIn(f'id="topic-{slug}"' if slug in self.site.homes else f'href="{slug}.html"', page)
            self.assertNotIn("entries", page)
            self.assertNotIn("entry", page)

    def test_internal_links_and_anchors_resolve(self):
        parsed = {name: Page(text) for name, text in self.built.items()}
        for name, page in parsed.items():
            for href in page.hrefs:
                if re.match(r"^[a-z]+:", href):
                    continue
                target, _, frag = href.partition("#")
                target = target or name
                self.assertIn(target, parsed, f"{name}: broken link {href}")
                if frag:
                    self.assertIn(frag, parsed[target].ids, f"{name}: missing anchor {href}")

    def test_ids_are_unique_per_page(self):
        for name, text in self.built.items():
            ids = Page(text).ids
            self.assertEqual(len(ids), len(set(ids)), f"{name}: duplicate ids")

    def test_navigation_marks_exactly_one_current_page(self):
        for name, text in self.built.items():
            # The trail marks where you are. The settings and about pages are marked twice, in the trail and on their icon in the rail.
            self.assertEqual(Page(text).current, {"index.html": 0, "settings.html": 2, "about.html": 2}.get(name, 1), name)

    def test_welsh_is_marked_up_and_not_empty(self):
        for name, text in self.built.items():
            self.assertNotIn("{{", text, name)
            self.assertNotIn("}}", text, name)
            self.assertNotIn("&amp;#", text, f"{name}: text escaped twice")
            for span in Page(text).cy:
                self.assertTrue(span["text"].strip(), f"{name}: empty Welsh span")

    def test_the_compass_page_has_its_figure(self):
        self.assertIn('class="rose"', self.built["group-geography.html"])
        self.assertIn("Compass rose labelled in English and Welsh", self.built["group-geography.html"])

    def test_the_document_language_is_the_interface_language(self):
        for text in self.built.values():
            self.assertIn('<html lang="en" data-storage="cydymaith-am-iaith"', text)


class RejectsBase(unittest.TestCase):
    """Shared helper: apply a mutation to a copy of the real data and expect validation to fail."""

    def setUp(self):
        self.raw = build.read()

    def check_rejects(self, mutate, fragment):
        raw = copy.deepcopy(self.raw)
        mutate(raw)
        with self.assertRaises(build.ContentError) as ctx:
            build.validate(raw)
        self.assertIn(fragment, str(ctx.exception))


class StructureValidationTests(RejectsBase):
    def test_unlisted_page(self):
        self.check_rejects(lambda r: r["pages"].update(orphan=r["pages"]["compass"]), "not listed")

    def test_missing_page_file(self):
        self.check_rejects(lambda r: r["structure"]["groups"][0]["pages"].append("ghost"), "does not exist")

    def test_repeated_page(self):
        self.check_rejects(lambda r: r["structure"]["groups"][0]["pages"].append("compass"), "more than once")

    def test_reserved_slug(self):
        def mutate(r):
            r["pages"]["index"] = r["pages"]["compass"]
            r["structure"]["groups"][0]["pages"].append("index")
        self.check_rejects(mutate, "reserved")

    def test_group_ids_are_unique(self):
        def mutate(r):
            r["structure"]["groups"].append({"id": r["structure"]["groups"][0]["id"], "pages": []})
        self.check_rejects(mutate, "unique id")

    def test_duplicate_section_id(self):
        def mutate(r):
            secs = r["pages"]["when"]["sections"]  # a tiles group: one-page groups have their own message
            secs[1]["id"] = secs[0]["id"]
        self.check_rejects(mutate, "repeated")

    def test_repeated_concept_on_a_page(self):
        def mutate(r):
            secs = r["pages"]["compass"]["sections"]
            secs[1]["concepts"].append(secs[0]["concepts"][0])
        self.check_rejects(mutate, "concept id repeated")

    def test_unknown_figure(self):
        self.check_rejects(lambda r: r["pages"]["compass"].update(figure="unicorn"), "unknown figure")

    def test_figure_needs_its_concepts(self):
        def mutate(r):
            r["pages"]["compass"]["sections"][0]["concepts"].remove("north")
        self.check_rejects(mutate, "needs concepts north")


class PackValidationTests(RejectsBase):
    def test_pack_code_must_match_its_folder(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"].update(code="xx"), "'code' must be")

    def test_pack_needs_its_endonym(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["ui"].pop("endonym"), "ui word 'endonym'")

    def test_pack_needs_every_group_title(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["groups"].clear(), "group title")

    def test_direction_must_be_valid(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"].update(dir="up"), "ltr or rtl")

    def test_pack_page_without_skeleton(self):
        def mutate(r):
            r["packs"]["cy"]["pages"]["ghost"] = copy.deepcopy(r["packs"]["cy"]["pages"]["compass"])
        self.check_rejects(mutate, "no matching")

    def test_pack_page_needs_a_title(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["pages"]["compass"].update(title=""), "missing 'title'")

    def test_pack_page_source_must_exist(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["pages"]["compass"].update(source="nope"), "'source' must be")

    def test_unknown_section_in_pack(self):
        def mutate(r):
            r["packs"]["cy"]["pages"]["compass"]["sections"]["nope"] = {"title": "x", "concepts": {}}
        self.check_rejects(mutate, "unknown section")

    def test_unknown_concept_in_pack(self):
        def mutate(r):
            r["packs"]["cy"]["pages"]["compass"]["sections"]["points"]["concepts"]["nope"] = {"text": "x"}
        self.check_rejects(mutate, "unknown concept")

    def test_concept_without_text(self):
        def mutate(r):
            r["packs"]["cy"]["pages"]["compass"]["sections"]["points"]["concepts"]["north"]["text"] = ""
        self.check_rejects(mutate, "exactly one of 'text' or 'forms'")

    def test_language_codes_are_lower_case(self):
        self.assertTrue(build.LANG_CODE.match("cy"))
        self.assertTrue(build.LANG_CODE.match("zh-hant"))
        for bad in ("CY", "c", "cy_GB", 'cy"]', ""):
            self.assertFalse(build.LANG_CODE.match(bad), bad)

    def test_concept_naming_an_unknown_source(self):
        def mutate(r):
            r["packs"]["cy"]["pages"]["compass"]["sections"]["points"]["concepts"]["north"]["source"] = "nope"
        self.check_rejects(mutate, "unknown source")


MILK = ("cy", "food-drink", "drinks", "milk")


def milk(raw):
    return raw["packs"]["cy"]["pages"]["food-drink"]["sections"]["drinks"]["concepts"]["milk"]


class VarietyValidationTests(RejectsBase):
    def test_a_concept_cannot_have_both_text_and_forms(self):
        self.check_rejects(lambda r: milk(r).update(text="Llaeth"), "exactly one of")

    def test_a_concept_needs_text_or_forms(self):
        def mutate(r):
            milk(r).pop("forms")
        self.check_rejects(mutate, "exactly one of")

    def test_forms_need_declared_varieties(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"].pop("varieties"), "declares no varieties")

    def test_a_form_cannot_name_an_undeclared_variety(self):
        self.check_rejects(lambda r: milk(r)["forms"][0].update(varieties=["west"]), "undeclared varieties: west")

    def test_a_form_needs_text(self):
        self.check_rejects(lambda r: milk(r)["forms"][0].update(text=""), "without 'text'")

    def test_a_form_cannot_be_listed_twice(self):
        self.check_rejects(lambda r: milk(r)["forms"][1].update(text="Llaeth"), "twice")

    def test_a_variety_needs_id_name_and_short(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["varieties"][0].pop("short"), "'id', 'name' and 'short'")

    def test_variety_ids_are_unique(self):
        def mutate(r):
            r["packs"]["cy"]["meta"]["varieties"][1]["id"] = "north"
        self.check_rejects(mutate, "repeated")

    def test_variety_ids_are_safe_and_not_reserved(self):
        for bad in ("all", "North", 'n"]', "1x"):
            self.check_rejects(lambda r, b=bad: r["packs"]["cy"]["meta"]["varieties"][0].update(id=b), "variety id")


class VarietyRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = build.read()
        _, cls.edition = build.pick_edition(cls.raw)
        cls.site = build.Site(cls.raw, cls.edition)
        cls.tmp = pathlib.Path(tempfile.mkdtemp())

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def plain_raw(self):
        """The real data with the regional forms taken out."""
        raw = copy.deepcopy(self.raw)
        raw["packs"]["cy"]["meta"].pop("varieties")
        milk(raw).pop("forms")
        milk(raw)["text"] = "Llaeth"
        return raw

    def test_every_form_is_rendered_and_labelled(self):
        page = self.site.render_all()["food-drink.html"]
        row = re.search(r"<tbody>(.*?)</tbody>", page, re.S).group(1)
        self.assertIn('<span lang="cy">Llaeth</span><abbr class="vtag" title="South">S</abbr>', row)
        self.assertIn('<span lang="cy">Llefrith</span><abbr class="vtag" title="North">N</abbr>', row)
        self.assertLess(row.index("Llaeth"), row.index("Llefrith"))

    def test_each_form_says_which_varieties_it_is_emphasised_for(self):
        page = self.site.render_all()["food-drink.html"]
        self.assertIn('data-lang="cy" data-show="south"><span lang="cy">Llaeth', page)
        self.assertIn('data-lang="cy" data-show="north"><span lang="cy">Llefrith', page)

    def test_untagged_forms_show_for_every_variety(self):
        forms = [{"text": "a", "varieties": [], "note": None}, {"text": "b", "varieties": ["north"], "note": None}]
        self.assertEqual(self.site.show_sets("cy", forms), [["north", "south"], ["north"]])

    def test_a_concept_known_in_one_region_is_never_dimmed_away(self):
        forms = [{"text": "a", "varieties": ["north"], "note": None}]
        self.assertEqual(self.site.show_sets("cy", forms), [["north", "south"]])

    def test_two_forms_in_one_variety_both_show_there(self):
        forms = [{"text": "a", "varieties": ["north"], "note": None},
                 {"text": "b", "varieties": ["north", "south"], "note": None}]
        self.assertEqual(self.site.show_sets("cy", forms), [["north"], ["north", "south"]])

    def test_a_plain_row_keeps_the_plain_markup(self):
        page = topic_html(self.site, self.site.render_all(), "sky")
        self.assertNotIn('class="forms"', page)
        self.assertIn('<th scope="row" class="l1" lang="cy">Digon o <span class="key" data-k="3">heulwen</span></th>', page)

    def test_a_form_can_carry_its_own_note(self):
        raw = copy.deepcopy(self.raw)
        milk(raw)["forms"][0]["note"] = "Used in {{Gwent}}."
        build.validate(raw)
        page = build.Site(raw, self.edition).render_all()["food-drink.html"]
        self.assertIn('<small class="note">Used in <span lang="cy">Gwent</span>.</small>', page)

    def test_the_control_is_hidden_until_the_script_runs(self):
        page = self.site.render_all()["settings.html"]
        self.assertIn('<div class="prefs" id="prefs" hidden>', page)
        self.assertIn("Welsh: regional forms", page)
        for value in ("all", "north", "south"):
            self.assertIn(f'name="variety-cy" value="{value}" data-variety-lang="cy"', page)
        self.assertIn('value="all" data-variety-lang="cy" checked', page)
        self.assertNotIn("variety-en", page)  # English declares no varieties

    def test_the_controls_are_on_the_settings_page_and_not_in_every_menu(self):
        for name, page in self.site.render_all().items():
            if name == "settings.html":
                self.assertIn('id="prefs"', page)
            else:
                self.assertNotIn('id="prefs"', page, name)
            self.assertIn('href="settings.html"', page, name)

    def test_script_and_generated_css_are_linked_when_varieties_exist(self):
        for page in self.site.render_all().values():
            self.assertIn('<script src="app.js"></script>', page)
            self.assertIn('<link rel="stylesheet" href="varieties.css">', page)

    def test_generated_css_dims_the_other_varieties_for_each_language(self):
        css = self.site.varieties_css()
        for v in ("north", "south"):
            self.assertIn(f'html[data-v-cy="{v}"] .form[data-lang="cy"]:not([data-show~="{v}"])', css)
        self.assertNotIn('data-v-en', css)
        out = self.tmp / "with"
        build.build(out)
        self.assertEqual((out / "varieties.css").read_text(encoding="utf-8"), css)
        self.assertTrue((out / "app.js").is_file())

    def test_no_variety_machinery_is_emitted_without_varieties(self):
        raw = self.plain_raw()
        site = build.Site(raw, self.edition)
        pages = site.render_all()
        for name, page in pages.items():
            self.assertNotIn("varieties.css", page, name)
            self.assertNotIn("data-variety-lang", page, name)
        self.assertIn('data-pref="appearance"', pages["settings.html"])  # the theme controls are always there
        self.assertNotIn('class="forms"', pages["food-drink.html"])
        self.assertFalse(site.has_varieties())

    def test_the_pair_can_be_swapped_with_forms_on_the_first_side(self):
        site = build.Site(self.raw, self.edition, pair=("cy", "en"))
        pages = site.render_all()
        self.assertIn('<th scope="row" class="l1"><span class="forms"><span class="form" data-lang="cy" data-show="south">', pages["food-drink.html"])
        self.assertIn("Welsh: regional forms", pages["settings.html"])


class SourcesValidationTests(RejectsBase):
    def test_pack_without_sources(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"].pop("sources"), "needs at least one entry")

    def test_unknown_licence(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["sources"][0].update(licence="all-rights-reserved"),
                           "accepted:")

    def test_source_without_title(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["sources"][0].update(title=""), "needs a title")

    def test_duplicate_source_ids(self):
        def mutate(r):
            srcs = r["packs"]["cy"]["meta"]["sources"]
            srcs.append(dict(srcs[0]))
        self.check_rejects(mutate, "repeated")

    def test_url_must_be_https(self):
        self.check_rejects(lambda r: r["packs"]["cy"]["meta"]["sources"][0].update(url="javascript:alert(1)"),
                           "https://")


class EditionValidationTests(RejectsBase):
    ED = "cydymaith"

    def edition(self, raw):
        return raw["editions"][self.ED]

    def test_unknown_language(self):
        self.check_rejects(lambda r: self.edition(r)["languages"].append("xx"), "no pack")

    def test_needs_two_languages(self):
        self.check_rejects(lambda r: self.edition(r).update(languages=["en"]), "at least two")

    def test_interface_must_be_included(self):
        self.check_rejects(lambda r: self.edition(r).update(interface="xx"), "'interface'")

    def test_default_pair_must_be_two_different_languages(self):
        self.check_rejects(lambda r: self.edition(r).update(default_pair=["en", "en"]), "default_pair")

    def test_headline_needed_for_each_language_of_the_pair(self):
        self.check_rejects(lambda r: self.edition(r)["home"]["headline"].pop("cy"), "home.headline")

    def test_edition_needs_a_name(self):
        self.check_rejects(lambda r: self.edition(r).update(name=""), "missing 'name'")

    def test_edition_choice(self):
        raw = build.read()
        self.assertEqual(build.pick_edition(raw)[0], self.ED)
        raw["editions"]["second"] = raw["editions"][self.ED]
        with self.assertRaises(build.ContentError) as ctx:
            build.pick_edition(raw)
        self.assertIn("--edition", str(ctx.exception))
        self.assertEqual(build.pick_edition(raw, "second")[0], "second")
        with self.assertRaises(build.ContentError):
            build.pick_edition(raw, "nope")


class AddingALanguageTests(unittest.TestCase):
    """The point of the framework: new languages and editions are added by data alone."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.data = cls.tmp / "data"
        shutil.copytree(PROJECT, cls.data)
        # gd translates two concepts of one page; ar (right to left) translates one concept of another.
        add_pack(cls.data, "gd", "Gaelic", pages={"compass": {"points": ["north", "south"]}}, edition="Test Edition")
        add_pack(cls.data, "ar", "Arabic", direction="rtl", pages={"sky": {"sun-cloud": ["plenty-of-sunshine"]}})

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def raw(self):
        raw = build.read(self.data)
        build.validate(raw)
        return raw

    def test_the_new_data_validates(self):
        self.raw()

    def test_a_partial_language_shows_only_what_it_has(self):
        raw = self.raw()
        site = build.Site(raw, raw["editions"]["test"])  # default pair en -> gd
        self.assertEqual(site.slugs, ["compass"])  # every other page has no gd rows
        self.assertEqual(site.count_entries("compass"), 2)
        self.assertEqual([s["id"] for s in site.sections("compass")], ["points"])

    def test_building_a_new_edition_renames_the_site(self):
        out = self.tmp / "out"
        n = build.build(out, data_dir=self.data, edition="test")
        self.assertEqual(n, 12)  # home, the group (one page: the compass), sources, how to use, seven help chapters, settings
        home = (out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Test Edition", home)
        self.assertNotIn("Cydymaith am iaith", home)
        compass = (out / "group-geography.html").read_text(encoding="utf-8")
        self.assertIn('lang="gd"', compass)
        self.assertIn("gd:north", compass)
        self.assertNotIn("sky.html", compass)

    def test_the_figure_is_skipped_when_the_pair_lacks_its_concepts(self):
        out = self.tmp / "out2"
        build.build(out, data_dir=self.data, edition="test")
        self.assertNotIn('class="rose"', (out / "group-geography.html").read_text(encoding="utf-8"))

    def test_the_pair_can_be_swapped_without_touching_data(self):
        raw = self.raw()
        site = build.Site(raw, raw["editions"]["test"], pair=("gd", "en"))
        page = site.render_all()["group-geography.html"]
        first_row = re.search(r'<tr id="[^"]+"><th scope="row" class="l1" lang="gd">([^<]*)</th><td><span class="l2">([^<]*)</span>', page)
        self.assertEqual(first_row.groups(), ("gd:north", "North"))

    def test_a_right_to_left_language_gets_dir_attributes(self):
        raw = self.raw()
        ed = dict(raw["editions"]["test"], languages=["en", "cy", "gd", "ar"], default_pair=["en", "ar"])
        ed["home"] = {"headline": {"en": "E", "cy": "C", "gd": "G", "ar": "A"}}
        site = build.Site(raw, ed)
        self.assertEqual(site.slugs, ["sky"])
        page = topic_html(site, site.render_all(), "sky")
        self.assertIn('lang="ar" dir="rtl"', page)
        self.assertIn("ar:plenty-of-sunshine", page)

    def test_coverage_counts_translated_concepts(self):
        raw = self.raw()
        cov = build.coverage(channels.select(raw), raw["editions"]["test"])
        total = sum(len(s["concepts"]) for p in channels.select(raw)["pages"].values() for s in p["sections"])
        self.assertEqual(cov["gd"], (2, total))
        self.assertEqual(cov["en"], (total, total))

    def test_sources_page_lists_the_new_language(self):
        out = self.tmp / "out3"
        build.build(out, data_dir=self.data, edition="test")
        sources = (out / "sources.html").read_text(encoding="utf-8")
        self.assertIn("Written by the test author", sources)
        self.assertIn("Gaelic", sources)


class SourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = build.read()
        _, cls.edition = build.pick_edition(cls.raw)
        cls.tmp = pathlib.Path(tempfile.mkdtemp())

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def copy_data(self, name, licence):
        """Copy data/ to a temp dir with every source of every pack set to `licence`."""
        dest = self.tmp / name
        shutil.copytree(PROJECT, dest)
        for f in dest.glob("packs/*/pack.json"):
            d = json.loads(f.read_text(encoding="utf-8"))
            for s in d["sources"]:
                s["licence"] = licence
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return dest

    def test_strict_build_rejects_draft_sources(self):
        data = self.copy_data("drafts", "draft")
        with self.assertRaises(build.ContentError) as ctx:
            build.build(self.tmp / "out-drafts", data_dir=data, strict=True)
        self.assertIn("draft", str(ctx.exception))

    def test_strict_build_accepts_reviewed_sources(self):
        data = self.copy_data("reviewed", "own")
        self.assertEqual(build.build(self.tmp / "out-reviewed", data_dir=data, strict=True),
                         pages_written(build.Site(channels.select(self.raw), self.edition)))

    def test_normal_build_accepts_draft_sources(self):
        data = self.copy_data("normal", "draft")
        self.assertGreater(build.build(self.tmp / "out-normal", data_dir=data), 2)

    def test_draft_sources_are_listed_per_language(self):
        raw = copy.deepcopy(self.raw)
        raw["packs"]["cy"]["meta"]["sources"][0]["licence"] = "own"
        self.assertEqual(build.draft_sources(raw, self.edition), [("en", "draft")])

    def test_sources_page_lists_every_page_and_counts_every_entry(self):
        site = build.Site(self.raw, self.edition)
        text = site.sources_page()
        # each concept is counted once for each language of the edition
        total = sum(site.count_entries(s) for s in site.slugs) * len(site.langs)
        shown = sum(int(n) for n in re.findall(r"</td><td>(\d+)</td></tr>", text))
        self.assertEqual(shown, total)
        for slug in site.slugs:
            self.assertIn(f'<section id="{slug}">', text)

    def test_entries_are_counted_per_source(self):
        raw = copy.deepcopy(self.raw)
        cy = raw["packs"]["cy"]
        cy["meta"]["sources"].append({"id": "gov", "title": "A glossary", "licence": "OGL-3.0",
                                      "url": "https://example.gov.wales/glossary"})
        concepts = cy["pages"]["compass"]["sections"]["points"]["concepts"]
        concepts["north"]["source"] = "gov"
        concepts["south"]["source"] = "gov"
        build.validate(raw)
        text = build.Site(raw, self.edition).sources_page()
        self.assertIn('<a href="https://example.gov.wales/glossary">A glossary</a>', text)
        self.assertIn("Open Government Licence v3.0</a></td><td>2</td>", text)

    def test_sources_page_is_linked_but_outside_the_pager(self):
        built = build.Site(self.raw, self.edition).render_all()
        self.assertIn('href="sources.html"', built["about.html"])
        self.assertIn('aria-label="Previous and next page"', built["group-geography.html"])
        self.assertNotIn("Previous and next page", built["sources.html"])
        self.assertEqual(Page(built["sources.html"]).current, 1)


class MarkupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        raw = build.read()
        _, ed = build.pick_edition(raw)
        cls.site = build.Site(raw, ed)

    def test_marked_text_gets_the_commentary_language(self):
        self.assertEqual(self.site.markup("cy", "It is {{mae hi'n}} <b>"),
                         "It is <span lang=\"cy\">mae hi&#x27;n</span> &lt;b&gt;")

    def test_marked_text_in_the_interface_language_needs_no_span(self):
        self.assertEqual(self.site.markup("en", "A {{word}}"), "A word")

    def test_plain_text_passes_through(self):
        self.assertEqual(self.site.markup("cy", "no welsh here"), "no welsh here")


def css_ranges(css):
    """The code points covered by every unicode-range in a stylesheet, as a set of (low, high) pairs."""
    spans = set()
    for rng in re.findall(r"unicode-range:\s*([^;}]+)", css):
        for part in rng.split(","):
            lo, _, hi = part.strip().removeprefix("U+").partition("-")
            spans.add((int(lo, 16), int(hi or lo, 16)))
    return spans


class SelfHostedFontsTests(unittest.TestCase):
    """The site must work with no request to any other site, and the fonts must cover the text."""

    @classmethod
    def setUpClass(cls):
        cls.static = PROJECT / "static"
        cls.css = (cls.static / "project.css").read_text(encoding="utf-8")
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.out = cls.tmp / "dist"
        build.build(cls.out)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_no_page_or_stylesheet_requests_another_site(self):
        for f in list(self.out.glob("*.html")) + list(self.out.glob("*.css")):
            text = f.read_text(encoding="utf-8")
            text = text.replace('xmlns="http://www.w3.org/2000/svg"', "")
            # What a page loads: stylesheets, scripts, images and url() in the css. A link a person chooses to follow (the licences,
            # the code on GitHub) is theirs to follow and is not a request.
            urls = re.findall(r"""(?:<link[^>]*\shref|\ssrc)=["']((?:https?:)?//[^"']+)|url\(\s*["']?((?:https?:)?//[^)"']+)""", text)
            external = [a or b for a, b in urls]
            self.assertEqual(external, [], f"{f.name} loads from another site")

    def test_the_edition_lists_no_font_url(self):
        edition = json.loads((PROJECT / "editions" / "cydymaith.json").read_text(encoding="utf-8"))
        self.assertEqual(edition.get("fonts", []), [])

    def test_every_font_file_named_in_the_css_exists_and_is_woff2(self):
        files = re.findall(r"url\((fonts/[^)]+)\)", self.css)
        self.assertGreaterEqual(len(files), 10)
        for rel in files:
            data = (self.static / rel).read_bytes()
            self.assertEqual(data[:4], b"wOF2", rel)
            self.assertTrue((self.out / rel).is_file(), f"{rel} not published")

    def test_no_font_file_is_shipped_without_being_used(self):
        used = {pathlib.Path(f).name for f in re.findall(r"url\(fonts/([^)]+)\)", self.css)}
        shipped = {p.name for p in (self.static / "fonts").glob("*.woff2")}
        self.assertEqual(shipped, used)

    def test_each_font_ships_with_its_licence(self):
        for family, owner in (("hanken-grotesk", "Hanken Grotesk Project Authors"), ("literata", "Literata Project Authors")):
            text = (self.static / "fonts" / f"{family}-OFL.txt").read_text(encoding="utf-8")
            self.assertIn("SIL OPEN FONT LICENSE Version 1.1", text)
            self.assertIn(owner, text)

    def test_every_character_in_the_packs_is_in_a_shipped_range(self):
        spans = css_ranges(self.css)
        raw = build.read()
        text = set()

        def walk(v):
            if isinstance(v, str):
                text.update(v)
            elif isinstance(v, dict):
                for x in v.values():
                    walk(x)
            elif isinstance(v, list):
                for x in v:
                    walk(x)

        walk(raw["packs"])
        walk(raw["editions"])
        missing = sorted(c for c in text if not any(lo <= ord(c) <= hi for lo, hi in spans) and c not in "\n")
        self.assertEqual(missing, [], "characters no shipped font range covers: " + "".join(missing))

    def test_the_welsh_circumflex_letters_are_covered(self):
        spans = css_ranges(self.css)
        for ch in "\u0175\u0177\u0174\u0176":
            self.assertTrue(any(lo <= ord(ch) <= hi for lo, hi in spans), ch)

    def test_the_project_stylesheet_is_linked_and_publishes_the_fonts(self):
        page = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="project.css"', page)
        self.assertNotIn("fonts.googleapis", page)


class DataFilesTests(unittest.TestCase):
    def test_json_is_valid_utf8_with_trailing_newline(self):
        for f in list(PROJECT.rglob("*.json")) + list((ROOT / "framework" / "phrasebook" / "messages").glob("*.json")):
            raw = f.read_bytes()
            json.loads(raw.decode("utf-8"))
            self.assertTrue(raw.endswith(b"\n"), f"{f.relative_to(ROOT)}: missing trailing newline")

    def test_every_pack_folder_validates_on_its_own(self):
        raw = build.read()
        build.validate(raw)
        self.assertEqual(set(raw["packs"]), {"en", "cy"})


class DictionaryTests(unittest.TestCase):
    """The lookup dictionary is generated by every build, so a new page is covered without a separate step."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.out = cls.tmp / "site"
        build.build(cls.out)
        cls.dictionary = json.loads((cls.out / "dictionary.json").read_text(encoding="utf-8"))
        cls.raw = channels.select(build.read())
        cls.ed = build.pick_edition(cls.raw)[1]

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_the_build_writes_the_dictionary_for_the_edition_languages(self):
        self.assertEqual(self.dictionary["languages"], self.ed["languages"])

    def test_every_concept_on_every_page_has_an_entry_linked_to_that_page(self):
        entries = {e["concept"]: e for e in self.dictionary["entries"]}
        for slug, page in self.raw["pages"].items():
            for section in page["sections"]:
                for cid in section["concepts"]:
                    self.assertIn(cid, entries, cid)
                    self.assertIn(slug, [p["slug"] for p in entries[cid]["pages"]], cid)

    def test_every_page_of_an_entry_links_to_the_row_of_the_word_on_that_page(self):
        for entry in self.dictionary["entries"]:
            for page in entry["pages"]:
                page_file, row = page["href"].split("#")
                self.assertEqual(page_file, C.address(self.raw["structure"], page["slug"]).split("#")[0], entry["concept"])
                self.assertTrue(row.endswith("." + entry["concept"]), entry["concept"])
                html = (self.out / page_file).read_text(encoding="utf-8")
                self.assertTrue(f'<tr id="{row}">' in html or f'<g id="{row}">' in html, page["href"])  # a word on the compass is a label

    def test_every_entry_has_terms_in_every_language_of_the_edition(self):
        for entry in self.dictionary["entries"]:
            self.assertEqual(sorted(entry["terms"]), sorted(self.ed["languages"]), entry["concept"])
            for texts in entry["terms"].values():
                self.assertTrue(texts and all(t["text"] for t in texts), entry["concept"])

    def test_terms_are_plain_text_without_marking(self):
        for entry in self.dictionary["entries"]:
            for texts in entry["terms"].values():
                for t in texts:
                    self.assertNotIn("{{", t["text"])
                    self.assertNotIn("}}", t["text"])

    def test_a_new_page_is_picked_up_from_its_files(self):
        data = self.tmp / "extra"
        shutil.copytree(PROJECT, data)
        raw = build.read(data)
        raw["structure"]["groups"][0]["pages"].append("test-page")
        raw["pages"]["test-page"] = {"title": "Test", "source": "draft",
                                     "sections": [{"id": "s", "concepts": ["test-word"]}]}
        for code in raw["packs"]:
            raw["packs"][code]["pages"]["test-page"] = {
                "title": "Test", "source": "draft",
                "sections": {"s": {"title": "S", "concepts": {"test-word": {"text": "Gair {{prawf}}"}}}}}
        index = phrasebook.dictionary.index(raw, self.ed)
        entry = next(e for e in index["entries"] if e["concept"] == "test-word")
        self.assertEqual([p["slug"] for p in entry["pages"]], ["test-page"])
        self.assertEqual(entry["terms"]["cy"], [{"text": "Gair prawf", "varieties": []}])


class HelpBookTests(unittest.TestCase):
    """The Welsh help (packs/cy/help.json) matches the English book entry for entry."""

    @classmethod
    def setUpClass(cls):
        cls.raw = build.read()
        cls.book = phrasebook.help.Book.load(cls.raw["packs"])
        cls.en = json.loads((ROOT / "framework" / "phrasebook" / "help" / "en.json").read_text(encoding="utf-8"))
        cls.cy = cls.raw["packs"]["cy"]["help"]

    def test_the_welsh_covers_every_anchor_and_chapter_and_adds_none(self):
        self.assertEqual(set(self.cy["features"]), set(self.book.anchors()))
        self.assertEqual(set(self.cy["chapters"]), set(self.en["chapters"]))

    def test_each_welsh_entry_has_the_same_parts_as_the_english(self):
        for anchor, entry in self.en["features"].items():
            welsh = self.cy["features"][anchor]
            self.assertEqual({k for k in welsh if k in ("keys", "touch")}, {k for k in entry if k in ("keys", "touch")}, anchor)
            self.assertEqual(len(welsh["body"]), len(entry["body"]), anchor)
            self.assertTrue(welsh["title"].strip(), anchor)

    def test_the_welsh_chapter_page_is_shown_first_with_a_toggle(self):
        site = build.Site(self.raw, build.pick_edition(self.raw)[1])
        page = site.render_all()["help-finding-your-way.html"]
        self.assertEqual(page.count('class="about-bar"'), 1)
        self.assertLess(page.index('id="about-cy"'), page.index('id="about-en"'))
        self.assertIn("<h2>Mynd yn ôl</h2>", page)

    def test_the_report_has_an_address_and_it_is_never_whole_in_a_page(self):
        address = build.pick_edition(self.raw)[1]["contact"]
        self.assertRegex(address, r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
        site = build.Site(self.raw, build.pick_edition(self.raw)[1])
        pages = site.render_all()
        user, host = address.split("@")
        self.assertIn(f'data-contact-user="{user}" data-contact-host="{host}"', pages["index.html"])
        for name, page in pages.items():
            self.assertNotIn(address, page, name)

    def test_chapter_seven_is_shown_and_offers_the_report(self):
        site = build.Site(self.raw, build.pick_edition(self.raw)[1])
        page = site.render_all()["help-using-help.html"]
        for anchor in ("help-button", "help-icons", "report-a-problem"):
            self.assertIn(f'id="{anchor}" data-feature="{anchor}"', page)

    def test_the_welsh_names_the_controls_as_the_welsh_interface_does(self):
        ui = self.raw["packs"]["cy"]["meta"]["ui"]
        text = json.dumps(self.cy, ensure_ascii=False)
        for key in ("settings", "about", "arrange_toggle", "how_to", "sources"):
            self.assertIn(ui[key], text, key)


if __name__ == "__main__":
    unittest.main()
