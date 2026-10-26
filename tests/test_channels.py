"""Release channels: sections marked "status": "development" are held back from the release build only.

Run from the repo root:  python3 -m unittest discover -s tests -v
"""
import copy
import json
import pathlib
import shutil
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "framework"))

import phrasebook  # noqa: E402
from phrasebook import channels, content  # noqa: E402

PROJECT = ROOT / "content" / "cydymaith"


def edit_json(path, fn):
    path = pathlib.Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    fn(data)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ChannelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = pathlib.Path(tempfile.mkdtemp())
        cls.data = cls.tmp / "project"
        shutil.copytree(PROJECT, cls.data)
        # Hold back the snow section of snow-ice, and every section of food-drink and talk (the whole Everyday group).
        edit_json(cls.data / "pages" / "snow-ice.json", lambda d: next(
            s for s in d["sections"] if s["id"] == "snow").update(status="development"))
        edit_json(cls.data / "pages" / "food-drink.json", lambda d: d["sections"][0].update(status="development"))
        edit_json(cls.data / "pages" / "talk.json", lambda d: [s.update(status="development") for s in d["sections"]])
        cls.release = cls.tmp / "release"
        cls.development = cls.tmp / "development"
        phrasebook.build(cls.release, project_dir=cls.data)
        phrasebook.build(cls.development, project_dir=cls.data, channel="development")
        cls.rel_dict = json.loads((cls.release / "dictionary.json").read_text(encoding="utf-8"))
        cls.dev_dict = json.loads((cls.development / "dictionary.json").read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def concept_ids(self, dictionary):
        return {e["concept"] for e in dictionary["entries"]}

    def test_the_release_build_leaves_out_a_held_back_section(self):
        self.assertNotIn("snow", self.concept_ids(self.rel_dict))
        self.assertIn("snow", self.concept_ids(self.dev_dict))
        self.assertIn("rain", self.concept_ids(self.rel_dict))

    def test_the_release_build_is_the_default(self):
        out = self.tmp / "default"
        phrasebook.build(out, project_dir=self.data)
        self.assertFalse((out / "food-drink.html").exists())

    def test_a_page_with_every_section_held_back_is_dropped_from_the_release(self):
        self.assertFalse((self.release / "food-drink.html").exists())
        self.assertTrue((self.development / "food-drink.html").exists())
        index = (self.release / "index.html").read_text(encoding="utf-8")
        self.assertNotIn("food-drink.html", index)
        self.assertFalse((self.release / "group-everyday.html").exists(), "a group left with no page has no tile and no page")
        self.assertNotIn("group-everyday.html", index)
        dev_index = (self.development / "index.html").read_text(encoding="utf-8")
        self.assertIn("group-everyday.html", dev_index)
        self.assertIn("food-drink.html", (self.development / "group-everyday.html").read_text(encoding="utf-8"))

    def test_the_offline_cache_lists_only_what_the_channel_publishes(self):
        sw = (self.release / "sw.js").read_text(encoding="utf-8")
        self.assertNotIn("food-drink.html", sw)
        self.assertIn("when.html", sw)

    def test_the_held_back_section_is_still_validated(self):
        raw = content.read(self.data)
        bad = copy.deepcopy(raw)
        bad["pages"]["snow-ice"]["sections"][0]["status"] = "soon"
        with self.assertRaises(content.ContentError):
            content.validate(bad)

    def test_an_unknown_channel_is_rejected(self):
        with self.assertRaises(content.ContentError):
            channels.select(content.read(self.data), "beta")

    def test_selecting_a_channel_does_not_change_the_project(self):
        raw = content.read(self.data)
        before = copy.deepcopy(raw)
        channels.select(raw, channel="release")
        self.assertEqual(raw, before)

    def test_a_figure_cannot_lose_its_concepts_to_a_held_back_section(self):
        data = self.tmp / "figure-project"
        shutil.copytree(PROJECT, data)
        edit_json(data / "pages" / "where.json", lambda d: d["sections"][0].update(status="development"))
        with self.assertRaises(content.ContentError):
            phrasebook.build(self.tmp / "figure-out", project_dir=data)


if __name__ == "__main__":
    unittest.main()
