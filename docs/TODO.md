# To-do

Work top to bottom. Tick items off in the commit that completes them. The generator is the framework submodule in `framework/`; its own to-do list (features, themes, search, navigation) is in `framework/docs/TODO.md`.

## 0. Principles (see `PHILOSOPHY.md`)

- [x] **Self-host the fonts and remove the Google Fonts request.** Done: Hanken Grotesk and Literata (SIL OFL 1.1) are served from `content/gair-wrth-air/static/fonts/` with their licences, latin and latin-ext only (157 KB). Tests check that no page or stylesheet requests another site, that every packed character is in a shipped range, and that each font file is used and has its licence. `ŵ` and `ŷ` are covered, though the current text does not use them yet.
  - [ ] Re-check both fonts' licences and versions before each release (Fontsource 5.3.0 at the time of writing).
- [ ] **Decide the licence for `content/`**: CC0 or CC BY 4.0 (CC BY 4.0 is safer if any source requires attribution). Add it as a separate licence file and to the README.
- [x] **Record the source and licence of every translation.** Done: per-pack sources, a generated Sources page, and licence validation. The two existing packs are marked `draft`.
- [ ] **Replace every `draft` source with a real one**, then switch the CI build to `python3 build.py dist --strict` so a draft can never reach the public site.
- [ ] **State the promises in the README**, including that GitHub Pages keeps its own ordinary logs.

## 1. Languages and content

- [ ] Welsh review by a fluent speaker (see `REVIEW.md`).
- [ ] **Research the Ymestyn resources page** ([ymestyn.cymru/resources](https://ymestyn.cymru/resources/)) and point visitors to it where it helps. The aim is to complement these resources, not compete with them. Findings from a first read:
  - Courses and programmes: SaySomethingInWelsh (partial competitor, spoken phrases), LearnWelsh, Siarad, OpenLearn, BBC Catchphrase (complements).
  - Reference and grammar: ClwbMaluCachu, Gareth King's books, BBC Learn Welsh book, Welsh Rules (complements).
  - Tutors, community, audio and TV: Richard Morse, Doctor Cymraeg, Dringo, Discord, Reddit, Paned, Madog Center, Sgwrsio, Hefyd, ypod.cymru, BBC Sounds, Radio Cymru, S4C Clic (complements).
  - The page gives no licence or reuse terms for any resource. Link to them, but do not copy their text (see `ASSETS.md`). Check each linked page before adding it to a "where next" list.
  - Ask the Ymestyn team whether they mind a link from the site, and whether they would like a link back.
- [ ] Welsh names for English places, starting with Westminster. Verify each name before it goes in.
- [ ] **Navigation and place-name elements.** The parts that place names and directions are made of, such as *ffordd* (road) and *llys* (court, hall), so a viewer can read a sign, a road name or a news item about a place.
  - Start with a page of common elements and what they mean, then a page for getting around (roads, junctions, turnings, left and right, straight on, near, opposite). Group them with the place names page.
  - Place-name elements change after other words (soft mutation) and the changes are part of the meaning, so the commentary boxes should explain the pattern where it shows up in the entries.
  - Elements vary by region and by period, so use the regional forms (varieties) where a form is local, and note when an element is old or only found in names.
  - Research the source of each entry first and record its licence. Check whether any official list of standard place names (government or public body) can be used under a licence `ASSETS.md` accepts, and do not copy from copyrighted gazetteers or dictionaries.
  - Verify every entry with a fluent speaker before release, and add the uncertain ones to `REVIEW.md`.
  - A figure or map is not needed. A plain table of element, meaning and example name may be enough.
- [ ] News topics: politics, crime, business, tourism, farming. These depend on the place names page and the navigation and place-name elements above.
- [ ] Sport topics.
- [ ] Culture, music and poetry topics. Vocabulary and phrases only, not lyrics or poems.
- [ ] **Add a second language** when you have material. A right-to-left or non-Latin language would test the framework hardest. Each non-Latin script needs an open-licence font subset, which affects offline size.

## 2. App features

  - [ ] Translate the search messages (`search_*` in `phrasebook/messages/en.json`) into Welsh and any other interface language.
  - [x] Search lists the words found on the page being browsed first (on a group page, the group's pages), then a separator headed "Other results". `search_other` needs a Welsh translation with the other search messages.
  - [ ] **Fill the held-back groups** (Geography, News, Sports): each has one placeholder page and its Welsh title is a draft in `docs/REVIEW.md`. Remove the `status` when a group has reviewed content. Geography already holds the town and country names (Cardiff to the United Kingdom), moved from the weather pages, so the release has 12 fewer weather entries until it is published.
  - [x] **Weather regrouped around what a forecast talks about**: Sky and visibility, Rain snow and ice, Wind, Temperature, Forecasts and warnings, When, Where, and Talking about the weather, in the order a forecast runs. Each topic ends with its own sentences. All 182 words and phrases were kept. The new Welsh titles are first drafts in `docs/REVIEW.md`.
  - [x] **Weather tree reorganised after the content-tree review**: the forecast first, Rain and storms and Snow and ice split, the four "In a sentence" sections gathered on one "How it's said" page (`patterns`), When and Where tidied, and Talking about the weather moved to Everyday. All 170 words and phrases kept; the tree is checked by `.claude/skills/content-tree/tree_report.py`. Page and section addresses changed (`rain-snow.html` is gone).
    - [x] Listen-first layout: the Welsh leads each row, rows run in a stated order, and the "also heard as" forms are searchable chips (framework change, see `framework/docs/FRAMEWORK.md`). The mockups are in `docs/mockups/`.
    - [x] Linking words, change verbs, pressure systems, greetings and quantities added to `patterns`, held back (`status: development`) until checked; listed in `REVIEW.md`.
      - [ ] Check them against a recent Welsh forecast, then remove the `status`. Fill `extent` (one word so far) and the two-word `pressure` and `opening-closing` sections.
    - [x] Snow and ice has its own icon (Carbon `snow`).
    - [x] Framework: linked tiles. When and Where are now the shared Time and place group, which Weather links to.
      - [ ] Link Time and place from News and Sports when they leave development.
      - [ ] Add a mutation decoder page ("heard something you cannot find?") and link it from every topic, as in the mockups.
      - [ ] Check the new layout in a browser at phone width, in every palette. The longest rows (`Gogledd-orllewinol`, `Amser ychwanegol`) should wrap, not squeeze the English.
  - [ ] When the weather section is complete, use it as the worked example on the how-to page.
  - [ ] Use the daffodil icon (the rose was dropped in the move to Carbon, which has no flower) on a page, and add icons for the Sources and How-to links if they are wanted.
- [ ] **Technology section, with App development.** A new page `technology` (group `technology`) with the section `app-development`, marked `"status": "development"` so it stays out of the release until it is ready.
  - Concepts already named: app, app-development, icon, navigation, dictionary, lookup, card, overlay, version, release, open-source, licence, offline, build, translation.
  - Translations are added as the app is built, in English and Welsh. The Welsh group title "Technoleg" is a first draft and needs review.
  - Remove the `status` when the section is ready to publish, after the translations are reviewed.

## Done

- [x] Restructure into data files, tests, CI and deploy workflow
- [x] Sources and licences on every pack
- [x] Framework split into its own repository (`cydymaith-framework`) and used here as a submodule in `framework/`
