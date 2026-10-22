# To-do

Work top to bottom. Tick items off in the commit that completes them. This is the only to-do list: the generator is the framework submodule in `framework/`, and its features and the general features it enables are in section 3.

## 0. Principles (see `PHILOSOPHY.md`)

- [x] **Self-host the fonts and remove the Google Fonts request.** Done: Hanken Grotesk and Literata (SIL OFL 1.1) are served from `content/gair-wrth-air/static/fonts/` with their licences, latin and latin-ext only (157 KB). Tests check that no page or stylesheet requests another site, that every packed character is in a shipped range, and that each font file is used and has its licence. `ŵ` and `ŷ` are covered, though the current text does not use them yet.
  - [ ] Re-check both fonts' licences and versions before each release (Fontsource 5.3.0 at the time of writing).
- [ ] **Decide the licence for `content/`**: CC0 or CC BY 4.0 (CC BY 4.0 is safer if any source requires attribution). Add it as a separate licence file and to the README.
- [x] **Record the source and licence of every translation.** Done: per-pack sources, a generated Sources page, and licence validation. The two existing packs are marked `draft`.
- [ ] **Replace every `draft` source with a real one**, then switch the CI build to `python3 build.py dist --strict` so a draft can never reach the public site.
- [ ] **State the promises in the README**, including that GitHub Pages keeps its own ordinary logs.

## 1. Languages and content

- [ ] Welsh review by a fluent speaker (see `REVIEW.md`).
- [ ] **Add the words heard on the S4C forecast (six uploads, Y Dyddiau Nesaf and Dros Nos).** The forecaster's real vocabulary, as subtitled on air. Every word is a draft until a fluent speaker has checked it (see `REVIEW.md`). Source notes: the memory file `broadcast-words-to-collect.md`.
  - [x] **Weather pages (new entries).** Done: 42 words added, all drafts listed in `REVIEW.md`.
    - Released on their topic pages: *heulwen*, *awyr las*, *llwydaidd*, *sefydlog*, *ansefydlog*, *cyfnewidiol* (Sky); *cymedrol* (Wind); *ar ei uchaf*, *ar ei isaf* (Temperature); *posibilrwydd* (The forecast); *hanner nos* and a new Seasons section (When); *gwlad* (Where); *ardaloedd* (How widespread).
    - Held back on How it's said until checked: quantity, time and linking words, weather verbs and comparisons.
    - Skipped: *uchaf*, which was already there as "Highest".
  - [ ] **Forms heard on air, to check against the standard:** *sy'n*, *mae 'na*, *bydd 'na*, *pethe'n*, *fymryn*, *dechre*, *cyntaf* → *cynta'r*, *fwy* (from *mwy*), *a'r*, *hyrddiadau* (plural of *hyrddiad*), *yn y bore*, *2.00yp*. Decide per form whether it goes in `also` (heard as), or the standard form is the main text with the colloquial form as an `also` chip.
  - [ ] **Patterns (How it's said, held back):** *hwnnw*, *yn ogystal â*, *o ran*, *dod i rym*, *yn ystod y bore*, *hanner nos* and the time phrases fit the existing candidate sections. Add a warning sentence group for *Rhybudd melyn o wynt* (yellow wind warning).
  - [ ] **Places (Geography):** *Caernarfon*, *Harlech*, *Y Drenewydd*, *Aberporth*, *Tyddewi*, *Y Fenni*, *Y Rhyl*, *Hwlffordd*, *Llanfair Dyffryn Clwyd*, *Aberaeron*, *Prestatyn*, *Llanrwst*, *Aberteifi*, *Aberhonddu*, *Llanelli*, *Porth*, *Cemaes*, *Capel Curig*, *Corwen*, *Clunderwen*, *Llanpumsaint*, *Llanelwy*. Check each spelling against an official source before use. The forecast uses these names, so they go with the Welsh place-name review.
  - [ ] **Left out, to check:** *Merch Cwmwl* (a caption, a name, or a graphic label; unclear). Presenter names are not collected.
- [ ] **Research the Ymestyn resources page** ([ymestyn.cymru/resources](https://ymestyn.cymru/resources/)) and point visitors to it where it helps. The aim is to complement these resources, not compete with them. Findings from a first read:
  - Courses and programmes: SaySomethingInWelsh (partial competitor, spoken phrases), LearnWelsh, Siarad, OpenLearn, BBC Catchphrase (complements).
  - Reference and grammar: ClwbMaluCachu, Gareth King's books, BBC Learn Welsh book, Welsh Rules (complements).
  - Tutors, community, audio and TV: Richard Morse, Doctor Cymraeg, Dringo, Discord, Reddit, Paned, Madog Center, Sgwrsio, Hefyd, ypod.cymru, BBC Sounds, Radio Cymru, S4C Clic (complements).
  - The page gives no licence or reuse terms for any resource. Link to them, but do not copy their text (see `ASSETS.md`). Check each linked page before adding it to a "where next" list.
  - Ask the Ymestyn team whether they mind a link from the site, and whether they would like a link back.
  - From the framework notes, also to link, after checking each page as above: [learnwelsh.cymru](https://www.learnwelsh.cymru) and [gov.wales/welsh-language-support-and-services](https://www.gov.wales/welsh-language-support-and-services).
- [ ] Welsh names for English places, starting with Westminster. Verify each name before it goes in.
- [ ] **Navigation and place-name elements.** *Started 2026-10-22: Geography is promoted and the first page, Place-name elements (46 elements in six sections, all drafts from memory), is in it. Still to do: the getting-around page, regional forms, a cleared source, and a fluent speaker's check.* The parts that place names and directions are made of, such as *ffordd* (road) and *llys* (court, hall), so a viewer can read a sign, a road name or a news item about a place.
  - [x] Page of common elements and what they mean: done (draft).
  - [ ] Then a page for getting around (roads, junctions, turnings, left and right, straight on, near, opposite). Group them with the place names page.
  - Place-name elements change after other words (soft mutation) and the changes are part of the meaning, so the commentary boxes should explain the pattern where it shows up in the entries.
  - Elements vary by region and by period, so use the regional forms (varieties) where a form is local, and note when an element is old or only found in names.
  - Research the source of each entry first and record its licence. Check whether any official list of standard place names (government or public body) can be used under a licence `ASSETS.md` accepts, and do not copy from copyrighted gazetteers or dictionaries.
  - **Sources found (research on 2026-10-22).** None is cleared for use yet. Nothing from them has been copied.
    - **RCAHMW Historic Place Names, glossary of Welsh place-name elements** ([historicplacenames.rcahmw.gov.uk/glossary](https://historicplacenames.rcahmw.gov.uk/glossary), also at [placenameswales.esdm.co.uk/geirfa](https://placenameswales.esdm.co.uk/geirfa)). Each entry has the element, its part of speech, an English meaning, example names with grid references and audio. Developed by Prof. Hywel Wyn Owen, Dr Geraint Wyn Jones and Gruffudd Prys of Bangor University with the Ordnance Survey. The footer says "© Crown copyright 2026: Royal Commission on the Ancient and Historical Monuments of Wales", and the page thanks the Ordnance Survey and Bangor University "for permission to reproduce this glossary". **No open licence is stated.** Its "Terms and Conditions" and "Community Content: Licences and Intellectual Property Rights" pages were not read. Status: not usable until the RCAHMW confirms a licence `ASSETS.md` accepts (for example OGL v3.0) or gives written permission. Best candidate for the meanings if cleared.
    - **Welsh Language Commissioner, standardised Welsh place-names** (lists of about 3,500 names, and the Place-names Standardisation Panel's "Guidelines for Standardising Place-names in Wales", June 2023 version). Wikipedia says the lists were published under the Open Government Licence v3.0, which `ASSETS.md` accepts. **This is second-hand.** The Commissioner's own page could not be fetched, so the licence and the current guidelines are unconfirmed. These are lists of names and spellings, not a glossary of elements, so they help with correct spellings (and the Geography group) rather than with meanings.
    - **Seen, not used:** the Hendre Coed Merioneth glossary ([hendrecoed.org.uk](https://hendrecoed.org.uk/Merioneth-Manganese/furtherInfo/glossary.html), licence not checked); the British History Online glossary ([british-history.ac.uk](https://prod.british-history.ac.uk/node/40506), an older work, licence not checked); [Wikipedia, Welsh toponymy](https://en.wikipedia.org/wiki/Welsh_toponymy) (CC BY-SA, which `ASSETS.md` does not accept). Published books, such as the Dictionary of the Place-Names of Wales, are copyright and must not be copied.
    - **Not found:** any Welsh Government guidance on place-name elements.
    - **Next:** read the RCAHMW licence pages, then ask the RCAHMW whether the glossary can be reused. Meanwhile any entry would be written from first principles, with the meaning checked by a fluent speaker, and recorded as an unreviewed `draft` source.
  - Verify every entry with a fluent speaker before release, and add the uncertain ones to `REVIEW.md`.
  - A figure or map is not needed. A plain table of element, meaning and example name may be enough.
  - From the framework notes: a travel and transport section covering roads and traffic news, and how place names are constructed in Welsh. Elements named there: *rhos*, *llys*, *maes*, *pentre*, *pen*, *dref*, *caer*, *llan*, *ffordd* and *lon* (*lôn*). The first page already has all but *rhos*, *pentre* and *lôn*.
- [ ] News topics: politics, crime, business, tourism, farming. These depend on the place names page and the navigation and place-name elements above. The framework notes name: law, crime and policing, politics, economics, business and finance.
- [ ] Sport topics: football, rugby, cricket, athletics, and more as it grows. A football page mockup is in `docs/mockups/listening-football.html`.
- [ ] Culture, music and poetry topics. Vocabulary and phrases only, not lyrics or poems.
  - From the framework notes: events such as *nos galan gaeaf*, and what the *Mari Lwyd* is; traditional songs and their meanings, for example *Calon Lân*. Check this against the rule above: vocabulary and phrases only, so a song's words would need to be public domain before they are quoted.
- [ ] **Add a second language** when you have material. A right-to-left or non-Latin language would test the framework hardest. Each non-Latin script needs an open-licence font subset, which affects offline size.

## 2. App features

- [ ] Translate the search messages (`search_*` in `phrasebook/messages/en.json`) into Welsh and any other interface language. (Also part of the dictionary lookup widget in 3.2.)
- [x] **Search lists the page being browsed first.** Done: words found on that page (on a group page, the group's pages) come first, then a separator headed "Other results".
  - [ ] `search_other` needs a Welsh translation, with the other `search_*` messages above.
- [ ] **Fill the held-back groups** (News and Sports; Geography is now released): each has one placeholder page and its Welsh title is a draft in `docs/REVIEW.md`. Remove the `status` when a group has reviewed content. Geography already holds the town and country names (Cardiff to the United Kingdom), moved from the weather pages, so the release has 12 fewer weather entries until it is published.
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
- [x] **Standalone About page.** Done: `about.html`, linked by the information icon above the settings gear on every page (and from Settings). It states the aims and philosophy in Welsh and English, with a language toggle at the top right (Welsh first) and a link to Sources. The copy is in the edition's `about_page`; the Welsh is an unchecked draft in `REVIEW.md`.
  - [ ] Check the page in a browser at phone width: the toggle at the top right, the icon above the gear, keyboard focus on the toggle, all palettes, light and dark, and right to left.
  - [ ] Link About from the home page text as well, and say in the copy that the app is open source once the licence for `content/` is decided.
  - [ ] From the framework notes: say that the app is for improvers, not beginners, and that the best experience is, of course, interacting with people.
  - [ ] A QR code and a share link.
  - [ ] Instructions on how to install the app for offline use.
  - [x] The "no AI" promise is on the About page (Welsh and English), in `PHILOSOPHY.md` and in the README: the app never calls an AI service or a language model. "Zero AI" means exactly that, not a claim about how the framework or the Welsh was written.
  - [ ] The rest of the philosophy wording from the framework notes: free to use, available offline, zero tracking and free to extend, with links back to the GitHub project site. Say "free to use" and "free to extend" only once the licence for `content/` is decided. Keep the honesty about the Welsh separate: every translation still has to be hand-verified by a fluent speaker (see `REVIEW.md`).
  - [ ] A question left open in the notes: is there a name for this kind of development ethos? Candidates to consider: privacy by design, calm technology, humane design, the small web.
  - [x] Settings and About pages have a Cy|En toggle rather than inline translations (from the framework notes). Done for both; the toggle does not yet remember its language.
- [ ] **Technology section, with App development.** A new page `technology` (group `technology`) with the section `app-development`, marked `"status": "development"` so it stays out of the release until it is ready.
  - Concepts already named: app, app-development, icon, navigation, dictionary, lookup, card, overlay, version, release, open-source, licence, offline, build, translation.
  - Translations are added as the app is built, in English and Welsh. The Welsh group title "Technoleg" is a first draft and needs review.
  - Remove the `status` when the section is ready to publish, after the translations are reviewed.
  - From the framework notes: begin with app development as this app is developed, and keep it updated with findings.

## 3. Framework

Features of the framework and the general features it enables, driven from this list. The framework repository (`framework/`) has no to-do list of its own: work there is committed in that repository, then the pointer is updated here. Mockups are in `framework/docs/mockups/`.

### 3.0 Principles

- [x] **Test that fails on third-party requests**, for both the neutral fixture and the real project.
- [x] **Decide a framework name.** The package is still called `phrasebook`, a working name, and the repository is `cydymaith-framework`. Decide a name for the framework, and check it for collisions before the first public deploy. A rename touches every import, the docs and the tests, so do it as one change.
- [x] Format all the Python with black. Settings are in `pyproject.toml` (line length 130); CI runs `black --check .`. Run `black .` before committing.

### 3.1 Languages and theming

- [x] **i18n and l10n conformance, and framework kept apart from the content.** `phrasebook/` holds no language; `content/gair-wrth-air/` holds everything of the project. Interface text is in a keyed message catalogue with fallback, placeholders, CLDR plurals and list patterns. Content must be in Unicode normal form C. Direction and language are marked relative to the surrounding text. The CSS uses logical properties and role class names. Details and gaps: `FRAMEWORK.md`.
  - [ ] **Look at it in a real browser**: right-to-left (switch the fixture interface to its right-to-left language), the phone layout, and the menu arrow in both directions.
  - [ ] Warn at build time when a pair language has no `ui` words for the labels shown beside it, instead of silently showing English.
  - [ ] Number formatting by locale (digit shapes, grouping) if any language needs it.
  - [ ] Let the interface language be chosen by the visitor (needs a catalogue in the page and the script).
  - [ ] Allow an interface language that has no phrase pack.
  - [ ] Add plural rules for each new language as it arrives, and consider shipping interface catalogues for common languages in `phrasebook/messages/`.
- [x] **Language-agnostic framework.** Concepts, language packs and editions; any pair from the edition's languages; right-to-left support in the metadata; coverage report. Output for English and Welsh is unchanged apart from capital letters on the compass labels.
- [x] **Save user preferences in the browser's own storage.** Done in `phrasebook/assets/app.js`: one versioned key per site (`<edition>:prefs`, named by the edition so sites on one origin stay apart), every read and write in `try/catch`, anything unrecognised ignored, applied before first paint, and tested with Node. It never touches the network or cookies.
  - [ ] Extend the same object for the language pair as that control arrives. The theme is done (version 2). Bump the version if the shape changes.
- [x] **Regional forms (varieties).** Concepts can hold several forms tagged by variety (for Welsh, north and south). Every form is labelled, and a control emphasises one variety and dims the rest. Needs a hands-on check in a real browser, especially on a phone, where the control sits in the menu drawer.
  - [ ] Search must find any form, so "llefrith" finds "milk" as well as "llaeth". Compare in normal form C and fold case by the language's own rules (`Intl.Collator`), not with ASCII lower-casing.
  - [ ] Consider an "only my variety" mode that hides the other forms, if dimming proves too busy.
  - [ ] Varieties are one flat axis today. Add a second axis (for example formal and colloquial) only if the content needs it.
  - [ ] Research and add more regional pairs, and check each label. Confirm the dimming has enough contrast in the dark theme.
- [x] **About page.** Done: an optional `about_page` in the edition gives a standalone page with a no-script language toggle at the top right, linked from the rail above the settings gear. See `FRAMEWORK.md`.
- [x] **Listen-first rows, "also heard as", section order and linked tiles.** Done: the first language leads each row (the language heard), `also` forms are chips that search can find, a section can state its order, and a group can show a tile for a page that lives in another group. See `FRAMEWORK.md`.
  - [ ] Show the regional form's label and the `also` forms on the lookup card as a hint of why a word matched.
  - [ ] Show linked pages in `tree.json`, once something reads it.
- [ ] **Choose the language pair ("from" and "to").** This replaces the old "swap direction" item and covers any number of languages.
  - Render every language of the edition into each page (all cells present, two shown), so size grows linearly with languages. Without scripts it shows the edition's default pair.
  - Needs table rows turned into CSS grid rows so columns can be reordered. Keep table semantics with explicit roles.
  - Show commentary (notes, intros, boxes) for any displayed language that has it.
  - Home page copy is currently per language, not per pair. Template it so any pair reads naturally.
  - Remember the pair in preferences. Also accept a URL fragment, so a pair can be shared.
- [x] **Light/dark appearance and colour palettes.** Done: *Same as device* (default), *Light* and *Dark*, plus a choice of palette. Four ship: `default`, `high-contrast` (AAA), `red-green-safe` and `blue-yellow-safe`. Palettes are OKLCH data (`phrasebook/palettes/`, and a project's own `palettes/`), converted to `palettes.css` at build time; the build fails a palette that breaks its contrast or colour-vision promises. Saved with the other preferences (version 2, which still reads version 1) and applied before first paint. See `FRAMEWORK.md`.
  - [x] **Screenshots of every theme**: `python3 build.py dist --screenshots` writes one picture of each palette, light and dark, into `docs/screenshots` (git-ignored), with a gallery README. Still to do: run it in CI and keep the pictures as a build artifact, so a pull request can show a change to a palette.
  - [ ] **Look at it in real browsers and on real devices**, in each palette and variant: the compass rose, focus rings, the current-page marker, the dimming of other regional forms, the Settings page at phone width.
  - [ ] **Ask people with colour-vision deficiencies to try the palettes.** The checks are arithmetic on simulations; they are not evidence that the palettes work for people.
  - [ ] Choose the palette automatically from `prefers-contrast: more` when the visitor has not chosen, without taking the choice away from them.
  - [ ] Check Windows forced-colours mode by hand, and screen-reader announcement of the radio groups.
  - [ ] Meet the 3:1 contrast for the boundaries of controls (jump links, pager, menu button) in the default palette, or give them text-only identification. `rule-strong` is below 3:1 there; the `high-contrast` palette meets it.
  - [ ] Consider more palettes (monochrome for achromatopsia, a low-glare dark, a sepia) and text-size and line-spacing preferences. Each is a data file or a small control.
- [x] **Tests for the controls and the preferences logic.** Node tests cover reading, validating, applying and saving the preferences; build tests cover the controls, the pre-paint script and the generated palettes.

### 3.2 App features of the framework

- [x] **Installable offline app (PWA).** All pages install with the app and work with no network.
  - Web manifest with a relative `start_url` and `scope`, so it works under the GitHub Pages sub-path. Icons at 192, 512 and maskable sizes, declared per edition and validated.
  - Service worker that pre-caches every built file, with a cache name versioned from a hash of their content. The build generates the file list itself, so new pages are included automatically.
  - Updates arrive silently on the next visit (the new service worker takes over at once; no update banners, no install nags). Installing is the person's choice, through the browser's own menu.
  - Everything is installed at once (the site is small); no per-topic offline choice.
  - No push notifications and no background sync.
  - Tests cover the manifest fields, icon validation and that the pre-cache list matches the built files, on both the real project and the neutral fixture (which has no icons, so the manifest degrades gracefully). Still to check by hand: install and offline behaviour on an iOS device.
- [x] **Client-side search across all entries.** Done with the lookup card below: every word and phrase in both languages of the pair, every regional form, and every topic title, matched with the language's own case rules and then again with accents ignored. See `FRAMEWORK.md`.
- [x] **Dictionary lookup widget.** Done: the search button at the top of the rail opens a card that slides out from behind the rail as an overlay. As the person types, it lists the matching words with their translations, and under each word the topics it is in, as links that land on the word's row. Escape, the Close button, a tap outside and following a link all dismiss it; `/` opens it from the keyboard.
  - The card lists matching words with their translations.
  - Links to matching pages arrive on the card as sub-items.
  - Build on the client-side search above, and use the same normal-form and case-folding rules for matching.
  - The index is `dictionary.json`, generated by every build from the packs and pages (`phrasebook/dictionary.py`), and each page of an entry carries a link to the word's row. It is read once, when the card first opens, and is precached, so search works offline.
  - [ ] **Try the card on a phone**: the slide out from the rail, the keyboard coming up over the results, the Close button, a tap outside, a result link landing on its row, then offline, and TalkBack and VoiceOver.
  - [ ] **Try it right to left** (switch the fixture interface to its right-to-left language): the card should slide out from the other side.
  - [ ] Show the regional form's label (north, south) beside each form on the card, and match a query typed in a third language of an edition with more than two.
- [x] **Tile navigation from the mockup** (`docs/mockups/navigation-mockup.png`), replacing the sidebar menu, the Explore dialog and the home panel. Done: a rail with the Settings gear, a top bar with Back and the trail, tiles for groups and for each group's topics (both languages, Carbon icons), keys (Right goes in, Left goes back, Up and Down move along) and a swipe with the reading direction to go back, and `tree.json` kept for search. Designed mobile first, which is now in `PHILOSOPHY.md`. See `FRAMEWORK.md`.
  - [ ] **Try it on a phone**: tap targets, the card sliding in from the right when a tile is tapped, dragging it back out with a finger (follows the finger, springs back when let go early, leaves on a flick, ignores the screen edge), Back, the rail gear, the tiles at 2 across, install, then offline, and TalkBack.
  - [ ] **Smooth card transitions.** Work more on the slide of the cards: the search card leaving from behind the rail, the tile-to-topic and topic-to-tile slides, and the drag back. Check the timing and easing against the page slide so the two feel like one motion, keep them steady while the keyboard is up, and respect reduced motion throughout.
  - [ ] **Try it with VoiceOver, and right to left** (switch the fixture interface to its right-to-left language).
  - [x] **Site search in the rail.** Done: the button is hidden until `search.js` runs (so without scripts there is no control that does nothing), then opens the card.
  - [ ] Consider a "recent" row of tiles on the home page for the last topics visited, only if it can be kept on the device and without nudging anyone to return.
- [x] **Entries should not repeat the title.** Done: a section heading that matches the page title in both languages (case and normal form ignored) is left out (`repeats_title` in `phrasebook/site.py`); the section keeps its `id`, so links still land. Column headers stay, as they name the languages and appear once per table.
  - [ ] Add a test that a section titled like its page has no `<h2>`, and look at the topic pages in a browser.
  - Also done: the ENGLISH and CYMRAEG column headers are visually hidden (kept for screen readers); each table sits on its own card in the surface shade; the title-bar trail gives the second language only as far as the parent; the settings are an accordion (`details`, one open at a time); the Welsh app's default palette is now red and green.
  - Also done: a section whose words are all on the page's figure (the compass) is no longer a table as well; the compass labels carry the word anchors, so search links still land.
  - [ ] Look at the cards, the accordion and the red and green default in a browser, in light and dark.

### 3.3 Settings screen

Use icons for light dark and an accessibility/high contrast toggle. Colour schemes to feature miniature pallets below those options.
All oklch compatible. 

**Plan (mockup: `framework/docs/mockups/settings-mockup.html`, open it in a browser; the controls change its colours).**

- [x] **1. Decide the open questions** (below), then freeze the mockup.
- [x] **2. Messages.** New keys for the section headings, the three modes, the contrast switch and its hint, the palette badges and the language toggle label. The framework keeps English only; the Welsh strings go in the Welsh pack's `ui` table and are listed in the project's `REVIEW.md`.
- [x] **3. Page markup** (`Site.settings_page`, `theme_controls`, `variety_fields`). Replace the accordion with cards that are all visible: Appearance, Accessibility, Colour schemes, Regional forms, About this app. Appearance becomes three icon tiles (light, dark, same as device). Accessibility becomes a three-way segmented control, **Standard | Safe colours | High contrast**, that **filters** the colour schemes on offer and changes no scheme. Palettes become a grid of swatch cards, each a miniature page (header bar, tile, card with two text lines, accent dot) drawn from that palette's own colours, with a badge for AAA and colour-blind-safe. Each scheme belongs to exactly one level, worked out from its palette file: `level: AAA` is High contrast; otherwise any `colour_vision` claim makes it Safe colours; otherwise it is Standard (today in the Welsh app: Standard has `default` and `yellow-green`; Safe colours has `red-green-safe`, `blue-yellow-safe` and `yellow-green-safe`; High contrast has `high-contrast` and `yellow-green-high-contrast`). The build writes the level on each card, and CSS (`:has` on the checked radio) lists only the cards of the chosen level, so it works with no script; if a level has only one scheme, a line says more appear when a palette is added for it. Regional forms become a segmented control with a live example.
- [x] **4. Palette previews at build time.** The build already holds each palette's light and dark colours as oklch (`palettes.py`). Emit them as custom properties on each swatch (`--pv-bg`, `--pv-tile` and so on) in the generated `palettes.css`, so the preview follows the current mode with no script. No new colour maths and nothing hard-coded in the stylesheet.
- [x] **5. Language toggle (Cy|En).** Reuse the About page's radio toggle at the top right. Each label is rendered once per language of the pair and the stylesheet shows one; the controls and their state exist once. The toggle is the same group of radios, so it works with no script. This is the "toggle rather than inline translations" note above, and applies to Settings and About together.
- [x] **6. Preferences** (`app.js`). Prefs version 3 adds `access` (`standard`, `safe` or `high`) and keeps `appearance`, `palette` and the varieties. Each level remembers the scheme last picked in it, so changing level and coming back returns to your earlier choice. A saved palette that is not in the active level falls back to that level's first scheme, and choosing a palette also sets the level it belongs to when prefs are read. Versions 1 and 2 still read. Remember the toggle's language too. Node tests for read, validate, apply and save, and for old versions.
- [x] **7. Styles** (`style.css`). Segmented control and icon tiles, switch, swatch grid (2 across on a phone, 4 on wide screens), selected and focus rings that do not rely on colour alone, 44px targets, logical properties only, `forced-colors` and `prefers-reduced-motion`.
- [x] **8. Icons.** Add Carbon `light`, `asleep`, `screen` and `contrast` to `ui-icons/` (same package and version, Apache-2.0), and record them in `ASSETS.md`. The mockup uses stand-in drawings.
- [x] **9. Tests and checks.** Build tests for each control, the preview properties and the toggle; the no-script fallback (controls hidden, language toggle works); the palette contrast checks still pass; update the tests that expect the accordion.
- [ ] **10. Look at it** on a phone and desktop in every palette, light and dark, right to left, forced colours and keyboard only, then run the screenshot script (`--screenshots`) and read the pictures.

**Built (2026-10-22).** Steps 1 to 9. Not done: the Cy|En toggle does not remember its language between visits (the page shows the first language of the pair each time); Settings now has the toggle, About keeps its own; and step 10, looking at it in real browsers and with the screenshot script, is still to do. Welsh words for the new settings messages are drafts in the project's `REVIEW.md`.

**Open questions.** (Settled: Accessibility has three levels, Standard, Safe colours and High contrast, which filter the schemes on offer by a rule on the palette file; no scheme changes. More schemes can be added later as palette files.)

1. **Keep the three modes, or only light and dark?** The mockup keeps "same as device" as the third tile, because it is the default.
2. **Should the Safe colours schemes name the kind of colour blindness they cover** (red-green, blue-yellow) on the card, as well as the badge? The labels are drafts.
3. **Where should Regional forms sit?** Last, as now, or above Colour schemes, since it changes the words rather than the look.

**As built, where it differs from the plan above.** The level is not stored as a preference: it is worked out from the saved palette, and preferences version 3 stores `picks` (the palette last picked at each level) instead of `access`. There are no AAA or colour-blind-safe badges on the cards, because the level already says it, and the swatches are 3 across on wide screens, not 4. Regional forms are a segmented control without the live example. The Settings page has the Cy|En toggle and About keeps its own; neither remembers its language, and both show the first language of the pair each time.

### 3.4 Usability

Script to generate and test each screen and score them for usability. Run each time a screen is modified. Not every build.

### 3.5 Screen tile reordering

Ability to customise the order of tiles on home page and sub pages. A spanner or other icon - toggle the edit order mode on. Edit order mode shows smaller buttons with just their icon. User can drag the buttons to where they want like on an app screen. Toggle edit mode off saves the new config. 
Screen background changes colour, and the toggled edit icon background matches it. Title says drag to reorder. Needs a reset default option.

### 3.6 Report issue screen

Via a flag icon on the side bar. 
Opens a mode like edit mode, says select the element that is wrong, or skip - button to skip. Next step, an email is created with a report section in markdown filled out. User can type what else they want and the email is sent. Can it send in the background? Can I set up a separate email for it? Save this for a future feature.

## Done

- [x] Restructure into data files, tests, CI and deploy workflow
- [x] Sources and licences on every pack
- [x] Framework split into its own repository (`cydymaith-framework`) and used here as a submodule in `framework/`
- [x] Release channels: sections marked `development` are held back from the release build (`phrasebook/channels.py`)
- [x] Language-agnostic framework with packs and editions
- [x] Framework separated from the content, with a localisable interface
