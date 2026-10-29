# Cydymaith am iaith

A multilingual phrasebook as a small static site: a navigation tree, one page per topic, two languages side by side. The first edition is English and Welsh. *Cydymaith am iaith* means "a companion for language".

A companion to keep open while watching the news, the weather, sport or anything else.

No sign-up, no accounts, no ads, no tracking, no payments, no subscription, no nagging, no pressure sales, no AI, no addictive features. See [docs/PHILOSOPHY.md](docs/PHILOSOPHY.md), and the founding principle, [Technoleg Dda](docs/TECHNOLEG-DDA.md).

> **Status: in early development, most features have not been added yet, and not all the translations have been verified.** Treat it as a draft until [docs/REVIEW.md](docs/REVIEW.md) is complete. Corrections are welcome through the "Welsh correction" issue template.

Users can find the **live site here: <https://cydymaith-app.github.io/cydymaith/>**

## Quick start (for developers)

Requires Python 3.12 or later (CI uses 3.12) and git. There are no dependencies. Node 20 or later is optional and only runs the tests for the small browser script. The generator is the [framework](https://github.com/cydymaith-app/cydymaith-framework), kept here as a git submodule, so clone with it:

```sh
git clone --recurse-submodules https://github.com/cydymaith-app/cydymaith.git
# or, in a clone you already have:  git submodule update --init

python3 build.py dist                      # write the site to dist/
python3 -m http.server -d dist 8000        # preview at http://localhost:8000
python3 -m unittest discover -s tests -v   # the project's tests
python3 -m unittest discover -s framework/tests -v   # the framework's own tests (browser script tests too, if Node is installed)
```

To move to a newer framework: `git -C framework pull`, run the tests, then commit the new `framework` pointer.

Options: `--project DIR` picks a project (default: the only folder in `content/`), `--edition NAME` picks an edition when a project holds several, and `--strict` fails while any source is still an unreviewed draft.

## How it is organised

This repository is the **project**: the English and Welsh phrases, the regional forms and the site's branding. The **framework** that builds it lives in its own repository, [cydymaith-framework](https://github.com/cydymaith-app/cydymaith-framework), and is included here as a git submodule in `framework/`. The framework contains no language, no phrase and no wording of its own beyond an English message catalogue, and a test fails if it ever names a language.

| Path | What it holds |
|---|---|
| `framework/` | The generator (a submodule of `cydymaith-framework`): the interface message catalogue, plural rules, and the stylesheet and scripts shared by every site. |
| `content/cydymaith/` | One translator: `structure.json`, `pages/`, `packs/<code>/`, `editions/`, and `static/` (this project's fonts and typography). |
| `build.py` | Short entry point: puts `framework/` on the path and builds `content/`. |
| `tests/` | `test_content.py`, `test_channels.py` and `test_project.py` check the real content. The framework's own tests are in `framework/tests/`. |

The framework follows i18n and l10n conventions (BCP 47 tags, `lang` and `dir`, logical CSS, keyed messages with CLDR plurals and fallback, Unicode normal form C). See [framework/docs/FRAMEWORK.md](framework/docs/FRAMEWORK.md) for the file formats, the conventions, what is not done yet, and how to start another translator.

## Editing Welsh

A concept in `content/cydymaith/packs/cy/pages/weather.json` looks like this:

```json
"warning-for-wind": { "text": "Rhybudd am wynt", "note": "{{am}} softens {{gwynt}} to {{wynt}}" }
```

Section `intro` and `box` entries, and row notes, are commentary on that language, written in the pack's `commentary_lang` (English unless stated). Mark text in the pack's own language with `{{double braces}}`.

## Grading

Every group, page and section has a level from 1 (beginner) to 3 (advanced), worked out from what it holds: the median number of Welsh words in an entry. One word for a thing (*gogledd*, north) is level 1; a phrase built round it (*yn y gogledd*, in the north) comes after; a whole sentence (*bydd hi'n heulog yfory*, it will be sunny tomorrow) is level 3. The point is to let tiles and sections be ordered from simple to advanced, or the other way round for more advanced users.

```sh
python3 build.py --grades      # print every level and how it was worked out; builds nothing
```

Where the rule is plainly wrong, a skeleton file sets `"level": 1`, `2` or `3` by hand and the report stars it. One is set so far: the days of the week (*Dydd Llun*, Monday, is two written words but one beginner item), in `pages/when.json`. `tests/test_project.py` keeps the grades honest. The grades, like the Welsh, want a fluent speaker's review. How it works, and how to use it for another project, is in the framework's [README](https://github.com/cydymaith-app/cydymaith-framework#grading-your-content) and [docs/FRAMEWORK.md](framework/docs/FRAMEWORK.md#grading-how-demanding-a-tile-or-section-is). The levels put tiles and sections in order from simple to advanced, or the reverse, when a visitor asks: **Settings → Trefn / Order** offers Arferol / Default (as written, which stays the default), Y symlaf yn gyntaf / Simplest first and Y mwyaf datblygedig yn gyntaf / Most advanced first. A screen whose tiles they have arranged themselves keeps their order. The Welsh for those labels is a draft for a fluent speaker to check.

## Related topics

An end topic can link to related topics as a row of tiles, with `"related"` in its page file (`content/cydymaith/pages/<slug>.json`). So far the how-it's-said topic opens the Compass, the wind topic opens the eight points, and the Compass opens how it is said. Back returns to the topic you came from. `tests/test_project.py` checks the links. The Welsh heading, *Pynciau cysylltiedig*, is a draft for a fluent speaker to check.

## Listening aids

The Welsh comes first in each row (above the English), because it is the language being heard (`default_pair` in the edition). Five fields help someone who has just heard a word and needs to find it:

- `also`: other forms the word is heard as, such as a changed beginning. They show as chips under the row and search finds the word from any of them.

  ```json
  "rain": { "text": "Glaw", "also": ["law"] }
  ```
- `keys`: up to three words of the text, with the matching words in the other language in the same order. They are drawn in the same colour, or the same underline, in both, to match what is heard to what is read. The position in the list is the colour, and `null` skips one, so a word keeps its colour from row to row. **Settings → Geiriau allweddol / Key words** chooses colour, underline or neither; colour is not offered with high contrast or monochrome.

  ```json
  "heavy-rain-and-strong-wind": { "text": "Glaw trwm a gwynt cryf", "keys": ["gwynt", "Glaw"] }
  ```
- `order` (on a section, in the pack): one line saying what order the rows run in, such as "lightest to heaviest".
- `links` (on a group in `structure.json`): shows a tile for a page that lives in another group, so When and Where are written once and reached from Weather as well as from Time and place.
- `"status": "development"` (on a section): holds it back from the release. The new words on the How it's said page wait there until a fluent speaker has checked them.
- `about_page` (in the edition): the standalone About page, `about.html`, in each language it is written in. A toggle at the top right switches language with no script, an information icon above the settings gear links to it from every page, and it ends with links to How to use the app and Sources (the one place they are linked from, so the home page and Settings do not repeat them; an edition with no About page keeps them there instead).

The `listening-layout` and `content-tree` skills in `.claude/skills/` review a topic's layout and the shape of the tree.

## Regional forms

Languages vary by region. Declare a pack's varieties once in its `pack.json`:

```json
"varieties": [
  { "id": "north", "name": "North", "short": "N" },
  { "id": "south", "name": "South", "short": "S" }
]
```

Then give a concept several `forms` in place of one `text`, tagging each with the varieties that use it:

```json
"milk": { "forms": [
  { "text": "Llaeth",   "varieties": ["south"] },
  { "text": "Llefrith", "varieties": ["north"] }
] }
```

- **Recognised.** Every form is shown with a small label (N, S), so a regional word is never mistaken for the only one.
- **Switchable.** A control in the menu, "Welsh: regional forms", offers All, North and South. Choosing a variety emphasises its forms and dims the others. Nothing is hidden.
- **Remembered on the device only.** The choice is kept in the browser's own storage. Without the script every form shows equally and the control does not appear.
- **Rules.** A form with no `varieties` applies everywhere. A concept known in only one region is never dimmed. Forms can carry their own `note`.
- **Any language.** Any pack can declare its own varieties, such as British and American English.

## Adding a page

1. Create `content/cydymaith/pages/<slug>.json` with its sections and concept ids.
2. List the slug under a group in `structure.json`.
3. Add `packs/<code>/pages/<slug>.json` for each language you can fill, setting its `source`.
4. Run the tests. The build refuses unlisted pages, unknown or repeated ids, texts that match no concept, and sources without an accepted licence.

The lookup dictionary (`dictionary.json`) needs no step of its own. Every build regenerates it from the pages and packs (`framework/phrasebook/dictionary.py`), and the offline cache includes it.

## Adding a language

1. Create `packs/<code>/pack.json` using a lower-case BCP 47 code (`gd`, `ga`, `ar`, `zh-hant`). Copy an existing pack for the shape: name, `dir` (`ltr` or `rtl`), `ui.endonym`, group titles and sources.
2. Add `packs/<code>/pages/<slug>.json` files with whatever concepts you have. Partial coverage is fine.
3. Add the code to `languages` and `home.headline` in an edition.

The full checklist, including interface wording and plural rules, is in [framework/docs/FRAMEWORK.md](framework/docs/FRAMEWORK.md).

## Republishing under another name

Write another file in `editions/`: a new site `name`, a different set of `languages`, a different `default_pair`, new home copy. Build it with `python3 build.py dist --edition <name>`. To make a different translator altogether, add a project folder under `content/`.

## Sources and licences

Each pack lists its sources in `pack.json`, each pack page names its default `source`, and a concept can name another with `"source": "<id>"`. The build publishes the lot on a generated Sources page.

```json
"sources": [
  { "id": "own", "title": "Translated by the author", "licence": "own" },
  { "id": "ogl", "title": "Welsh Government weather glossary", "licence": "OGL-3.0", "url": "https://example.gov.wales/glossary" }
]
```

- Accepted licences: `public-domain`, `CC0-1.0`, `CC-BY-4.0`, `OGL-3.0`, `own`. The policy is in [docs/ASSETS.md](docs/ASSETS.md).
- `draft` marks an unreviewed source. A normal build warns about drafts. `--strict` fails on them, so use it as the gate for a public release.

## Release channels

A section still in early development can be held back from the release build. In its page file, `pages/<slug>.json`, give the section `"status": "development"`:

```json
{ "id": "winter", "status": "development", "concepts": ["snow", "snowy"] }
```

- `python3 build.py dist` (the release channel, the default) leaves the section out. A page with every section held back is dropped from the menu, the site and the offline cache.
- `python3 build.py dist --channel development` includes everything.
- Held-back content is still validated in both channels, and a held-back section cannot strip a figure of its concepts. Logic is in `framework/phrasebook/channels.py`, so any project can use it.
- Only `development` is accepted as a status. A section without one is released.

## Publishing

Pushing to `main` runs the tests and deploys `dist/` to GitHub Pages. In the repository, set **Settings > Pages > Source** to **GitHub Actions** once.

## Roadmap

See [docs/TODO.md](docs/TODO.md).

## Licence

Code: [MIT](LICENSE). Fonts and phrase data have their own licences; see [docs/ASSETS.md](docs/ASSETS.md).
