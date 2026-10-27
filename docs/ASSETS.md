# Assets and licensing

Everything in this repository is open: code, fonts, icons, and every Welsh phrase. Nothing is used under a licence that restricts copying, modifying or redistributing it. The policy (which licences are accepted and which are not) is in the framework's [docs/ASSETS.md](../framework/docs/ASSETS.md), and applies here too.

This is a working policy, not legal advice.

## Fonts in use

| Font | Role | Licence | Source |
|---|---|---|---|
| Hanken Grotesk | Interface text | SIL OFL 1.1 | https://github.com/marcologous/hanken-grotesk |
| Literata | Text in the second language | SIL OFL 1.1 | https://github.com/googlefonts/literata |

Both are self-hosted from `content/cydymaith/static/fonts/`, taken from the Fontsource packages `@fontsource/hanken-grotesk` and `@fontsource/literata` 5.3.0, which carry the OFL text and copyright lines (`*-OFL.txt` beside the files). Licences read on 2026-10-17. Re-check before each release.

- Neither licence names a Reserved Font Name, so the unmodified files are used as published. Check again before subsetting or renaming them yourself.
- Only the `latin` and `latin-ext` subsets are shipped. **Welsh needs `ŵ` and `ŷ`** (U+0175, U+0177), which are in `latin-ext`, confirmed in the shipped files. A test fails if any character in the packs falls outside the shipped ranges.
- **Each new script needs its own open-licence font.** Greek, Cyrillic and Arabic have OFL fonts. CJK fonts are very large, so they would need subsetting to keep offline installs small.

## Icons in use

| Set | Licence | Source |
|---|---|---|
| IBM Carbon, `@carbon/icons` 11.91.0 | Apache-2.0 | https://carbon-design-system.com, https://github.com/carbon-design-system/carbon |

The sixteen Carbon icons below are copied from the npm package `@carbon/icons@11.91.0` (the `svg/32` set) into `content/cydymaith/icons/`, with the package's Apache-2.0 `LICENSE` beside them. Licence read on 2026-10-21 in the package and in the repository root. Re-check the licence and version before each release.

The paths are unmodified. The only change is a one-line comment added at the top of each file naming the package, version and licence. The build adds `fill="currentColor"` when inlining, because Carbon's files name no fill.

| Icon | Used for |
|---|---|
| `rain--scattered` | The weather forecast group |
| `partly-cloudy` | Sky and visibility |
| `rain` | Rain and storms |
| `snow` | Snow and ice |
| `windy` | Wind |
| `temperature` | Temperature |
| `calendar` | Time and date |
| `compass` | Compass |
| `chat` | Talking about the weather, and How it's said |
| `earth` | The Geography group |
| `map` | Places, the Geography page of towns, cities and countries |
| `tree` | Place-name elements (`building` would also suit) |
| `restaurant` | Everyday words, and Food and drink |
| `mobile` | Technology |
| `blog` | The News group (Carbon has no newspaper) |
| `trophy` | The Sports group |

- **Drawn for this site:** `daffodil`, as a 24px-grid, 2px round-stroke outline, so it is a different style from the filled Carbon icons and may need redrawing to match. It is the project's own work, released under the same MIT licence as the code, and carries a comment saying so. No open icon set has a daffodil: Iconify, which indexes most of them, finds none. The public-domain daffodil and narcissus ornaments on Wikimedia Commons (from 1909 and 1915 books) are engravings of 28 to 138 KB, too heavy and too detailed to inline, and the CC BY-SA ones are not accepted above. Not used by a page yet.
- Apache-2.0 needs the licence text kept with copies, and changes stated. The `LICENSE` file is in each icons folder, and a test fails if it goes missing. The licence does not cover IBM's names or trademarks.
- A project's own icons go in its `icons/` folder and are named with `icon` on a group or a page. The framework checks each file as a safe SVG subset at build time, then inlines it. The framework's own three interface icons are recorded in its `docs/ASSETS.md`.
- Icons are decorative beside their labels, so they are hidden from screen readers.
- **Not yet checked: BBC GEL icon sets.** The BBC's Global Experience Language ([BBC GEL iconography](https://www.bbc.co.uk/gel/features/iconography#licensing)) has alternative icon sets that are free for non-commercial use only. Under the policy above, a non-commercial licence is not accepted, so none of them may be used unless the BBC grants other terms. The page could not be fetched while writing this note, so the wording was not verified.

## Colour palettes in use

| Palette | Where it came from | Licence |
|---|---|---|
| `content/cydymaith/palettes/red-green.json` | Generated at hellocolor.de by the author, 2026-10-20, then adjusted (below) | **To confirm.** See below |
| `content/cydymaith/palettes/yellow-green.json` | Derived from `red-green.json` by the author, 2026-10-22: the red (OKLCH 0.489 0.198 25.4) replaced by the gold of the St David's cross (0.887 0.18 95.3), nearly the same chroma, the greens unchanged | Own work; inherits the open question on `red-green.json` above |
| `content/cydymaith/palettes/yellow-green-safe.json` | Derived from `yellow-green.json` by the author, 2026-10-22: only the two accents moved apart in lightness (light 0.489 to 0.33, dark 0.887 to 0.80) so it passes the protan, deutan and tritan checks | Own work; inherits the open question on `red-green.json` above |
| `content/cydymaith/palettes/yellow-green-high-contrast.json` | Derived from `yellow-green.json` by the author, 2026-10-22, at level AAA (7:1 text, 3:1 borders) | Own work; inherits the open question on `red-green.json` above |

The framework's own palettes are recorded in its `docs/ASSETS.md`.

The tool's settings, so the palette can be regenerated: <https://www.hellocolor.de/?base=%23EF4444&preset=art-deco&size=8&contrast=0.56&vibrancy=0.78&brightness=0.48&a11y=AA> (preset Art Deco, base `#EF4444`, scale size 8, contrast 0.56, vibrancy 0.78, brightness 0.48, accessibility AA). The tool builds its colours in the browser, so the link records the inputs, not the output. The output is kept in the palette file.

- **Taken as the tool gave them:** background, text, muted text and border; the light surface and the dark elevated surface; the light accent (step 400 of the tool's primary scale, `#b6001a`); the dark accent (the tool's ring colour, `#ff333b`).
- **Why the light accent is not the tool's primary (`#e60024`):** the primary is 4.31:1 on the light surface, under the 4.5:1 that AA needs for text. Step 400 of its own scale passes.
- **Derived here, because the tool has no such colour:** `rule-strong` in both variants; the dark `rule` (the tool's border `#161111` is 1.09:1 on its background, which cannot be seen); the compass star, tinted from the tool's secondary green (`#00967d`, OKLCH hue 175). The green with the red accent gives the red and green of the Welsh flag.
- **Not used:** the tool's success, warning and danger colours, and the rest of its scale, because the interface has no roles for them.
- **The tool's own audit** (its System Audit panel, read 2026-10-20, for the settings above): score 97, excellent. WCAG compliance 100% (26 of 26 token pairs pass AA, 13 reach AAA, light and dark). Average contrast 9.93:1. Average Delta E between primary, secondary and accent 0.270 in OKLab. Harmony, visual balance and token consistency 100%. This is the tool's report on its own tokens. It does not cover the colours derived here, or the pairings this interface makes (for example the accent on the surface, where the primary fell short). What gates the palette is the project's build, which checks the pairings the pages actually use.
- **Licence to confirm.** A palette is a list of colour values chosen by the author, and nothing here copies a design. The terms of hellocolor.de were not checked for what the author may do with its output. Read them before release, and record the result here.
- The colour-vision promises (`colour_vision`) are not made for this palette: red against green is the case they exist to protect, and the star is tinted pale so the red needle stays distinct from it by lightness.

## Welsh content

- Every language pack lists its sources and their licences in `pack.json`. Each pack page names its default source, and a concept can name another. The build publishes them on the Sources page.
- Phrases the author writes or translates personally belong to the author and are released under the data licence below.
- **Public domain is narrower than it sounds for Welsh.** Old public domain Welsh, such as 16th-century Bible translations, uses archaic spelling and vocabulary. It cannot supply modern terms such as weather forecast, warning or humidity.
- Compilations such as dictionaries, term banks and phrasebooks can carry their own copyright or database rights even when each word is common. Check the compilation, not only the words.
- UK Crown and Welsh Government material is often available under the Open Government Licence. Confirm per document.
- Mark anything unreviewed as unreviewed until a fluent speaker has checked it.

## Licences for this repository

| Part | Licence |
|---|---|
| Code (`build.py`, `tests/`) | MIT, see `LICENSE` |
| Fonts | SIL OFL 1.1, each font keeps its own licence file |
| Phrase data (`content/`) | **To decide.** CC0 (no conditions) or CC BY 4.0 (credit required) |
