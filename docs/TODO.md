# To-do

Work top to bottom. Tick items off in the commit that completes them. This is the only to-do list: the generator is the framework submodule in `framework/`, and its features and the general features it enables are in section 3.

## 0. Principles (see `PHILOSOPHY.md`)

- [x] **Self-host the fonts and remove the Google Fonts request.** Done: Hanken Grotesk and Literata (SIL OFL 1.1) are served from `content/cydymaith/static/fonts/` with their licences, latin and latin-ext only (157 KB). Tests check that no page or stylesheet requests another site, that every packed character is in a shipped range, and that each font file is used and has its licence. `ŵ` and `ŷ` are covered, though the current text does not use them yet.
  - [ ] Re-check both fonts' licences and versions before each release (Fontsource 5.3.0 at the time of writing).
- [ ] **Decide the licence for `content/`**: CC0 or CC BY 4.0 (CC BY 4.0 is safer if any source requires attribution). Add it as a separate licence file and to the README.
- [x] **Record the source and licence of every translation.** Done: per-pack sources, a generated Sources page, and licence validation. The two existing packs are marked `draft`.
- [ ] **Replace every `draft` source with a real one**, then switch the CI build to `python3 build.py dist --strict` so a draft can never reach the public site.
- [ ] **State the promises in the README**, including that GitHub Pages keeps its own ordinary logs.

## 1. Languages and content

- [ ] Welsh review by a fluent speaker (see `REVIEW.md`).
- [ ] **Add the words heard on the S4C forecast (eleven uploads, Y Dyddiau Nesaf, Dros Nos and a Newyddion storm report).** The forecaster's real vocabulary, as subtitled on air. Every word is a draft until a fluent speaker has checked it (see `REVIEW.md`). Source notes: the memory file `broadcast-words-to-collect.md`.
  - [x] **Weather pages (new entries).** Done: 42 words added, all drafts listed in `REVIEW.md`.
    - Released on their topic pages: *heulwen*, *awyr las*, *llwydaidd*, *sefydlog*, *ansefydlog*, *cyfnewidiol* (Sky); *cymedrol* (Wind); *ar ei uchaf*, *ar ei isaf* (Temperature); *posibilrwydd* (The forecast); *hanner nos* and a new Seasons section (When); *gwlad* (Where); *ardaloedd* (How widespread).
    - Held back on How it's said until checked: quantity, time and linking words, weather verbs and comparisons.
    - Skipped: *uchaf*, which was already there as "Highest".
  - [x] **Add the synthesised words (plan in `FORECAST-WORDS.md`).** Done 2026-10-26, all drafts listed in `REVIEW.md`:
    - a Pressure section on The forecast (held), with *Cefnlen o wasgedd uchel* and *Ardal o wasgedd isel*;
    - warning verbs and likelihood on The forecast, *Chwythu* and *Ar ei gryfaf* on Wind;
    - When retitled *Amser a dyddiad / Time and date*, with a related tile from The forecast in place of the group link, new rows in Days ahead and Parts of the day, and a held Before and after section;
    - a new held page, *Newid a symud / Change and movement*, taken off How it's said;
    - new rows in How it's said: Extent (released), Linking, Faint, and a held Around a figure.
  - [x] **The weather cards hold forecast phrases, not single words** (2026-10-27; the app is not aimed at beginners). Done, all drafts listed in `REVIEW.md`:
    - The forecast card (`warnings`) dropped. Its warnings went to the cards as phrases (*Rhybudd melyn am law* on Rain, a *Rhybuddion* section on Wind), its pressure to Change and movement (held), and its related tile to Time and date to How it's said.
    - Sky, Rain, Snow and ice, Wind, Temperature and the held Change and movement: every single-word row replaced by a phrase or part-sentence, heard on S4C where one was heard. How it's said is unchanged for now.
    - Grades: the rule is unchanged, so every weather card is now level 3 and the Order setting leaves the weather page in its written order.
  - [x] **Geography is one page; Time and place is split up** (2026-10-27). Compass (`compass`, was Where's points and areas, plus a new From which way section), Place names (`geography`, Regions of Wales moved in first) and Landscape and place-name elements (`place-name-elements`, Landscape moved in first) are accordions on `group-geography.html`. Time and date (`when`) moved to Everyday. The weather page links to the Compass, and How it's said opens Regions of Wales. Landscape and areas are phrases; the eight points and the place-name elements stay as words. Framework: a figure section keeps its address inside an accordion.
  - [x] **Geography brought up to the weather standard** (2026-10-27, after a critique against the weather pages). Landscape is its own page (`landscape`: coast and sea, inland and hills, named places), separate from the place-name elements, which are for reading names and signs. Regions of Wales is one row per region as it is heard after *yn* (the plain names are "also heard as"). Towns are alphabetical in Welsh, with the forms heard after *yn* and *i*; the nations have an order. Every section states its order. Key words no longer mark function words (*o'r*, *dros*, *ar hyd*, *ledled*). Compass rows have one gloss each, with *northerly* and the like as "also heard as" in English. Links between pages of the one Geography page make no tiles, so only the links out to the weather remain.
  - [x] **Compass by direction; Landmarks on Place names** (2026-10-28). From which way, Areas and Regions of Wales are one family per compass point (from, in, then in that part of Wales), in three sections: North and east, South and west, and The middle and all of it. Every row kept (30). Named places moved from Landscape to Place names as Landmarks. How it's said now opens the Compass, not Regions of Wales.
  - [ ] **Geography, still to do:** the places from the list below that are not yet in; the mutation notes on the Compass, Regions and place-name elements each explain a different change, but could be a single short page; and a getting-around page (see the navigation item).
  - [ ] **Snow and ice is all authored**: no winter forecast has been heard yet. Check it against one, and replace what is not said.
  - [ ] **Shelved for now (may come back; the words are kept in `FORECAST-WORDS.md` section 9):**
    - **Impacts and Travel:** one future page, *Effeithiau / Impacts* (the sea, damage, travel). Travel could become a related page for the weather, and other groups would want it too.
    - The new sentence patterns on How it's said, Short forms (*Ffurfiau byr*), On screen (*Ar y sgrin*), and additions to Agor a chau and Cyflwyno pwynt.
    - *Y môr* is too short to release on its own (3 rows), which is another reason to hold Impacts back.
  - [ ] **Check *Sych* stays the same on Sky and Temperature.** A test now compares them; if the Welsh changes, change both.
  - [ ] **Places (Geography):** *Caernarfon*, *Harlech*, *Y Drenewydd*, *Aberporth*, *Tyddewi*, *Y Fenni*, *Y Rhyl*, *Hwlffordd*, *Llanfair Dyffryn Clwyd*, *Aberaeron*, *Prestatyn*, *Llanrwst*, *Aberteifi*, *Aberhonddu*, *Llanelli*, *Porth*, *Cemaes*, *Capel Curig*, *Corwen*, *Clunderwen*, *Llanpumsaint*, *Llanelwy*, *Aberdaron*, *Llanwrtyd*; and *Sir Conwy*, *Ynys Môn*. Check each spelling against an official source before use. The forecast uses these names, so they go with the Welsh place-name review.
  - [ ] **Left out, to check:** *Merch Cwmwl* (a caption, a name, or a graphic label; unclear). Presenter names are not collected.
- [ ] **Time and date page: later additions.** The `when` page, to become *Amser a dyddiad / Time and date* (retitled 2026-10-26; see `FORECAST-WORDS.md` section 2). Every word is a draft for a fluent speaker.
  - [ ] **Seasons:** the four seasons, in the existing *Tymhorau* section (today it has only *tymor*, *hanner tymor* and *cynta'r tymor*).
  - [ ] **Months:** a new section for the twelve months.
  - [ ] **Sequence (*Trefn*), shelved from the forecast words:** *eisoes*, *yn gynharach*, *yn gyntaf*, *wedyn*, *yn nes ymlaen*, *dechrau*, *canol*, *diwedd* (table in `FORECAST-WORDS.md` section 9). *Wedyn*, *yn nes ymlaen* and *canol* are already held on How it's said, waiting for this.
- [x] **Synthesise the collected forecast words.** Done 2026-10-26 for uploads 1 to 11: see `FORECAST-WORDS.md`. Later uploads are added to that file's tables, not as new lists here.
- [ ] **A section on units of measure.** The forecast gives numbers with units, and a learner hears the unit as a word. First one heard: *mya*, the on-screen short form of *milltir yr awr*, miles per hour (*Hyrddio 74mya*, gusting 74 mph). The content already has *Milltir yr awr* on the wind page (`miles-per-hour` in `wind.json`), with *mya* only as a note ("abbreviated mya"). There is no home for units as a group, and the short form as it appears on screen, a number run into the unit (*74mya*), is not explained.
  - [x] **Where it lives (decided 2026-10-24):** a shared page, `units` (*Unedau mesur*), listed in Time and place and linked from the weather group (as `when` and `where` are), not a group of its own and not under a science group. Reasons: a learner meets *mya* and `16C` mid-forecast and should find them in a tap or two; there is no science content to share a group with, and a one-page group breaks the content-tree rules (compare `technology`); units are used across groups, so they are written once and linked. Revisit if a Nature and science group is ever added: the page can move or stay linked from both, at the cost of one edit in `structure.json`.
  - [ ] **Sections for the page:** speed (*milltir yr awr*, *mya*), temperature (the degree), rainfall (only if the forecast uses it), time on the clock (the 24-hour label), and how a figure is said. The wind page keeps its *Milltir yr awr* row; the two point to each other.
  - [ ] **Numbers:** lean towards a numbers page of its own that units link to, since numbers are needed beyond the weather (*saith deg pedwar*). Confirm when the units page is written.
  - [ ] **Entries to write, each a draft for a fluent speaker to check:** *mya* as its own searchable entry beside the existing *Milltir yr awr*, with how a number and the short form are written and said (*74mya*); the unit for temperature (degrees); the unit for rainfall; and the way a number and its unit are said together. Only *mya* has been heard so far, so collect the others from the forecast before writing them, and do not add a unit that has not been heard or checked.
  - [ ] **Check the short forms on screen and aloud:** the user reports that the presenter says the full phrase for the on-screen *74mya*: *saith deg pedwar milltir yr awr*, so the abbreviation is read out in full and 74 is *saith deg pedwar*. Confirm the same for *60mya*, *50mya* and *70mya*, and listen for how a temperature written *16C* is said. Temperatures are written *6C*, *13C*, *16C* with no degree sign. The map also shows a clock label (*16:0…*, 24-hour), which belongs with the time units. Numbers need a home too: the content has no numbers page yet (none of the page names is about numbers), so decide whether the units section also teaches how to say the figures heard on air.
- [ ] **Research the Ymestyn resources page** ([ymestyn.cymru/resources](https://ymestyn.cymru/resources/)) and point visitors to it where it helps. The aim is to complement these resources, not compete with them. Findings from a first read:
  - Courses and programmes: SaySomethingInWelsh (partial competitor, spoken phrases), LearnWelsh, Siarad, OpenLearn, BBC Catchphrase (complements).
  - Reference and grammar: ClwbMaluCachu, Gareth King's books, BBC Learn Welsh book, Welsh Rules (complements).
  - Tutors, community, audio and TV: Richard Morse, Doctor Cymraeg, Dringo, Discord, Reddit, Paned, Madog Center, Sgwrsio, Hefyd, ypod.cymru, BBC Sounds, Radio Cymru, S4C Clic (complements).
  - The page gives no licence or reuse terms for any resource. Link to them, but do not copy their text (see `ASSETS.md`). Check each linked page before adding it to a "where next" list.
  - Ask the Ymestyn team whether they mind a link from the site, and whether they would like a link back.
  - From the framework notes, also to link, after checking each page as above: [learnwelsh.cymru](https://www.learnwelsh.cymru) and [gov.wales/welsh-language-support-and-services](https://www.gov.wales/welsh-language-support-and-services).
- [ ] Welsh names for English places, starting with Westminster. Verify each name before it goes in.
- [ ] **Navigation and place-name elements.** *Started 2026-10-22: Geography is promoted and the first page, Place-name elements (49 elements in six sections, all drafts from memory), is in it. Still to do: the getting-around page, regional forms, a cleared source, and a fluent speaker's check.* The parts that place names and directions are made of, such as *ffordd* (road) and *llys* (court, hall), so a viewer can read a sign, a road name or a news item about a place.
  - [x] Page of common elements and what they mean: done (draft).
  - [ ] Then a page for getting around (roads, junctions, turnings, left and right, straight on, near, opposite). Group them with the place names page.
  - Place-name elements change after other words (soft mutation) and the changes are part of the meaning, so the commentary boxes should explain the pattern where it shows up in the entries.
  - Elements vary by region and by period, so use the regional forms (varieties) where a form is local, and note when an element is old or only found in names.
  - Research the source of each entry first and record its licence. Check whether any official list of standard place names (government or public body) can be used under a licence `ASSETS.md` accepts, and do not copy from copyrighted gazetteers or dictionaries.
  - **Sources found (research on 2026-10-22).** None is cleared for use yet. Nothing from them has been copied.
    - **RCAHMW Historic Place Names, glossary of Welsh place-name elements** ([historicplacenames.rcahmw.gov.uk/glossary](https://historicplacenames.rcahmw.gov.uk/glossary), also at [placenameswales.esdm.co.uk/geirfa](https://placenameswales.esdm.co.uk/geirfa)). Each entry has the element, its part of speech, an English meaning, example names with grid references and audio. Developed by Prof. Hywel Wyn Owen, Dr Geraint Wyn Jones and Gruffudd Prys of Bangor University with the Ordnance Survey. The footer says "© Crown copyright 2026: Royal Commission on the Ancient and Historical Monuments of Wales", and the page thanks the Ordnance Survey and Bangor University "for permission to reproduce this glossary". **No open licence is stated.** *Terms and Conditions read 2026-10-26:* Crown copyright material may be used for non-commercial purposes under the "Non-Commercial Government Licence 1.0", acknowledged as "Crown Copyright: Royal Commission on the Ancient and Historical Monuments of Wales"; commercial use needs an order form. That licence is not one `ASSETS.md` accepts, so nothing is copied. The terms say nothing about linking, and a plain link copies nothing: the Place-name elements page now ends with one (the page's `more` note). "Community Content: Licences and Intellectual Property Rights" was not read. Status: not usable until the RCAHMW confirms a licence `ASSETS.md` accepts (for example OGL v3.0) or gives written permission. Best candidate for the meanings if cleared.
    - **Welsh Language Commissioner, standardised Welsh place-names** (lists of about 3,500 names, and the Place-names Standardisation Panel's "Guidelines for Standardising Place-names in Wales", June 2023 version). Wikipedia says the lists were published under the Open Government Licence v3.0, which `ASSETS.md` accepts. **This is second-hand.** The Commissioner's own page could not be fetched, so the licence and the current guidelines are unconfirmed. These are lists of names and spellings, not a glossary of elements, so they help with correct spellings (and the Geography group) rather than with meanings.
    - **Seen, not used:** the Hendre Coed Merioneth glossary ([hendrecoed.org.uk](https://hendrecoed.org.uk/Merioneth-Manganese/furtherInfo/glossary.html), licence not checked); the British History Online glossary ([british-history.ac.uk](https://prod.british-history.ac.uk/node/40506), an older work, licence not checked); [Wikipedia, Welsh toponymy](https://en.wikipedia.org/wiki/Welsh_toponymy) (CC BY-SA, which `ASSETS.md` does not accept). Published books, such as the Dictionary of the Place-Names of Wales, are copyright and must not be copied.
    - **Not found:** any Welsh Government guidance on place-name elements.
    - **Next:** read the RCAHMW licence pages, then ask the RCAHMW whether the glossary can be reused. Meanwhile any entry would be written from first principles, with the meaning checked by a fluent speaker, and recorded as an unreviewed `draft` source.
  - Verify every entry with a fluent speaker before release, and add the uncertain ones to `REVIEW.md`.
  - A figure or map is not needed. A plain table of element, meaning and example name may be enough.
  - From the framework notes: a travel and transport section covering roads and traffic news, and how place names are constructed in Welsh. Elements named there: *rhos*, *llys*, *maes*, *pentre*, *pen*, *dref*, *caer*, *llan*, *ffordd* and *lon* (*lôn*). The first page already has all but *pentre* and *lôn*.
- [ ] News topics: politics, crime, business, tourism, farming. These depend on the place names page and the navigation and place-name elements above. The framework notes name: law, crime and policing, politics, economics, business and finance.
- [ ] Sport topics: football, rugby, cricket, athletics, and more as it grows. A football page mockup is in `docs/mockups/listening-football.html` (updated 2026-10-28 to the phrase standard, as on the weather).
  - [ ] **Phase 1, collect:** words heard on *Sgorio*, S4C rugby and Radio Cymru commentary, per upload, into `docs/SPORT-WORDS.md`. Check the licence of *termau.cymru* before using its terms, and record it in `ASSETS.md`.
  - [x] **Phase 2, scaffold** (2026-10-27): Sport is one page, like the weather: Football, Rugby (union), Results and tables, Teams and competitions, and How it's said, with a Numbers page in Everyday. Every section is held back (`status: development`), states its order, and has a few seed rows, all drafts. The placeholder `sport` page is gone (it was never released). Icons: Carbon `soccer`, `list--numbered`, `character--whole-number`, and a rugby ball drawn for the site.
  - [ ] **Phase 3, fill Football then Rugby** from the collection: phrases as heard, "also heard as" forms, key words, about 5 to 8 rows a section. Then Results, Teams and competitions, How it's said and Numbers (phase 4).
  - [ ] **Phase 5, release** each section once a fluent speaker has checked it. Cricket and athletics wait until then.
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
    - [ ] Link Time and date (now in Everyday) from News and Sports when they leave development.
    - [ ] Add a mutation decoder page ("heard something you cannot find?") and link it from every topic, as in the mockups.
    - [ ] Check the new layout in a browser at phone width, in every palette. The longest rows (`Gogledd-orllewinol`, `Amser ychwanegol`) should wrap, not squeeze the English.
- [ ] When the weather section is complete, use it as the worked example on the how-to page.
- [ ] Use the daffodil icon (the rose was dropped in the move to Carbon, which has no flower) on a page, and add icons for the Sources and How-to links if they are wanted.
- [x] **Standalone About page.** Done: `about.html`, linked by the information icon above the settings gear on every page. It is the one place How to use the app and Sources are linked from (the home page and Settings no longer repeat them; an edition with no About page keeps them there). It states the aims and philosophy in Welsh and English, with a language toggle at the top right (Welsh first) and a link to Sources. The copy is in the edition's `about_page`; the Welsh is an unchecked draft in `REVIEW.md`.
  - [ ] Check the page in a browser at phone width: the toggle at the top right, the icon above the gear, keyboard focus on the toggle, the quote, the Share button (shown only where the browser can share or copy), all palettes, light and dark, and right to left.
  - [x] About is linked from the home page text, beside Sources.
  - [ ] Say in the copy that the content is open once the licence for `content/` is decided (the page already says the code is MIT).
  - [x] The page says the app is for improvers, not beginners, and that the best way to learn is with people.
  - [x] A share link and Share button. **No QR code (decided).**
  - [x] Instructions on how to install the app for offline use (Android, iPhone and iPad, computer).
  - [x] The "no AI" promise is on the About page (Welsh and English), in `PHILOSOPHY.md` and in the README: the app never calls an AI service or a language model. "Zero AI" means exactly that, not a claim about how the framework or the Welsh was written.
  - [x] The philosophy is now **Technoleg Dda**, the founding principle in `docs/TECHNOLEG-DDA.md`: the statement and seven promises are on the About page in both languages, opening `PHILOSOPHY.md` and the README. It covers zero tracking and no AI. "Free to use" and "free to extend" for the content wait for the licence decision on `content/`, and the honesty about the Welsh stays separate (every translation is still to be hand-verified).
  - [x] The ethos has a name: **Technoleg Dda**, after Hywel Dda. It follows small technology, calm technology, privacy by design and local-first software.
  - [x] Settings and About pages have a Cy|En toggle rather than inline translations (from the framework notes), and both remember the language chosen.
  - [ ] **Technoleg Dda is held back** (`status: development`, 2026-10-27): the About section with the statement, Hywel Dda and the seven promises is out of the live site until its text is reviewed and matured, in both languages. `docs/TECHNOLEG-DDA.md`, `PHILOSOPHY.md` and the README are unchanged.
  - [ ] **Where next** is on the page but held back (`status: development`) until each link is checked and the Ymestyn team has been asked (see the Ymestyn item above). It holds learnwelsh.cymru and the gov.wales Welsh language support page.
  - [ ] A Welsh review of the new About copy (listed in `REVIEW.md`), and decide whether to open a `welsh` label on GitHub for the correction template.
- [ ] **Contact and issue reports by email.** Use the project's contact address, cydymaithapp@gmail.com, in the app for contact and for reporting issues.
  - Contact: a "Contact us" link on the About page (both languages) and in Settings, opening the person's own mail app with the address. No form, no server, no request made by the site.
  - [x] Issue reports: done 2026-10-23 through the help sheet (section 3.7): *Report a problem* builds the message from at most 256 characters of context and the person's own words, and opens it in their mail app. The address is the edition's `contact` and sits in the page in two pieces so a scraper does not take it. Still to do here: the Contact us links on About and Settings, the Welsh and English subject wording check, and the privacy wording.
  - Use the address as a `mailto:` link, with a subject line such as "Cydymaith am iaith: issue" (Welsh and English). Check the address is not copied into the page as plain text where a scraper would take it.
  - Add the Welsh and English labels to `REVIEW.md`, and say in the privacy wording that a message sent by email goes through the person's own mail provider.
  - Decide whether the Welsh correction template (`.github/ISSUE_TEMPLATE/welsh-correction.md`) stays as the route for corrections, with the email as the general contact.
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

- [x] **i18n and l10n conformance, and framework kept apart from the content.** `phrasebook/` holds no language; `content/cydymaith/` holds everything of the project. Interface text is in a keyed message catalogue with fallback, placeholders, CLDR plurals and list patterns. Content must be in Unicode normal form C. Direction and language are marked relative to the surrounding text. The CSS uses logical properties and role class names. Details and gaps: `FRAMEWORK.md`.
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
  - [x] Choose the palette automatically from `prefers-contrast: more` when the visitor has not chosen, without taking the choice away from them. Done 2026-10-27 for issue 5 (no first-run wizard): a first visit starts on the first high-contrast palette, unsaved. Not done: a dismissible one-time pointer to Settings; and with no script a high-contrast visitor still gets the default palette.
  - [ ] Check Windows forced-colours mode by hand, and screen-reader announcement of the radio groups.
  - [ ] Meet the 3:1 contrast for the boundaries of controls (jump links, pager, menu button) in the default palette, or give them text-only identification. `rule-strong` is below 3:1 there; the `high-contrast` palette meets it.
  - [x] **App theming (issue 3) and more themes (issue 4).** Done 2026-10-27. The framework owns the neutral, safe and high-contrast schemes and a library of five colour schemes named by their colours (`blue-white-red`, `green-white-red`, `green-white-orange`, `red-yellow`, `black-red-gold`). A palette can `extends` another and list only what differs. An edition sets `default_palette`. The app owns `red-green` (its default), `yellow-green` and its safe and high-contrast versions, and inherits the rest in the framework's order. The Welsh names of the new schemes are drafts in `docs/REVIEW.md`.
  - [ ] Visitors who saved a colour scheme before 2026-10-27 have `default` saved, which is now the neutral scheme, not red and green. Decide whether that needs a migration before release; nobody has used the app yet, so it may not.
  - [ ] Look at the five new colour schemes in a real browser, light and dark (`python build.py dist --screenshots`), and have the Welsh names checked.
  - [x] **Sections collapse.** Each headed section of a topic is an accordion, shut to begin with unless it is the page's only section (2026-10-28). Still to do: remember which are shut, a shut-all and open-all control, a help entry (run the `app-help` skill), and look at it on a phone with a screen reader.
  - [x] **More palettes** (2026-10-28): `sepia`, warm and low in glare (paper in light, dimmed cream text in dark; standard level), and `monochrome`, greys only for achromatopsia (safe level). The build simulates no colour vision (`achromat`) as well as the three colour blindnesses. Key words are underlined with Monochrome, as with High contrast: its key greys pass the check but the darkest is hard to tell from the text. A low-glare dark is part of Sepia rather than a palette of its own.
  - [x] **Yellow and green made consistent in OKLCH** (2026-10-28): no hex left, one green hue (175) for the neutrals in light and dark, one hue per key colour in both, and no key close to the accent. Tests: `YellowGreenPaletteTests`.
  - [ ] **Check every key colour against the accent in the framework.** The build checks keys against each other and the ink, not the accent. At 0.12, 20 of the 22 palette variants (framework and project) would fail; the worst are `red-green-safe` light (0.024), `monochrome` dark (0.025) and `default` light (0.069). Retune them, then add the check to `palettes.py`. Measured 2026-10-28.
  - [ ] Text-size and line-spacing preferences: each a small control in Accessibility and appearance. Check first that pages reflow at 200% (WCAG 1.4.4) and survive text-spacing overrides (WCAG 1.4.12).
  - [ ] `python build.py dist --screenshots` fails: it shoots `compass.html`, which no longer exists now that Geography is one page.
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
  - [x] **Smooth card transitions.** Work more on the slide of the cards: the search card leaving from behind the rail, the tile-to-topic and topic-to-tile slides, and the drag back. Check the timing and easing against the page slide so the two feel like one motion, keep them steady while the keyboard is up, and respect reduced motion throughout.
  - [ ] **Try it with VoiceOver, and right to left** (switch the fixture interface to its right-to-left language).
  - [x] **Site search in the rail.** Done: the button is hidden until `search.js` runs (so without scripts there is no control that does nothing), then opens the card.
  - [ ] Consider a "recent" row of tiles on the home page for the last topics visited, only if it can be kept on the device and without nudging anyone to return.
- [x] **Entries should not repeat the title.** Done: a section heading that matches the page title in both languages (case and normal form ignored) is left out (`repeats_title` in `phrasebook/site.py`); the section keeps its `id`, so links still land. Column headers stay, as they name the languages and appear once per table.
  - [ ] Add a test that a section titled like its page has no `<h2>`, and look at the topic pages in a browser.
  - Also done: the ENGLISH and CYMRAEG column headers are visually hidden (kept for screen readers); each table sits on its own card in the surface shade; the title-bar trail gives the second language only as far as the parent; the settings are an accordion (`details`, one open at a time); the Welsh app's default palette is now red and green.
  - Also done: a section whose words are all on the page's figure (the compass) is no longer a table as well; the compass labels carry the word anchors, so search links still land.
  - [ ] Look at the cards, the accordion and the red and green default in a browser, in light and dark.
- [x] **Related topics: end topics link to each other, as tiles.** Built 2026-10-23, apart from the review items below. An end topic lists `"related": ["page", "page#section"]` in its page file and gets a **Related topics** row of tiles after its sections, each the tile of the page it opens, named for the section if one is named. Back returns to the topic the tile was followed from (kept in the history entry, so a reload keeps it); the copy that slides in is scrolled to the section, so nothing jumps; the build checks every name. Written up in the framework README, `framework/docs/FRAMEWORK.md` (*Related topics*), the project README and the content-tree skill.
  - [x] **The links are the tiles themselves.** A row of tiles that look like a group page's, in both languages, replacing the earlier "See also" text line.
  - [x] **A tile is a page; Landscape is a section.** A related entry names a page and may name a section, so the tile opens Where at Landscape (the tile is called *Landscape*, with Where's compass icon).
  - [x] **Declared one way, not both.** The first plan was to draw the link at both ends from one declaration; with seven weather topics pointing at Where that would give Where seven tiles, so each topic lists what it wants. Where links back to *How it's said*.
  - [x] **Back after a cross-link.** Back returns to the topic it was followed from, through the same slide; any other way of opening the page keeps the up-the-tree Back.
  - [x] **First pairs.** Rain, Snow and ice, and How it's said open Where at Landscape; Wind opens Where at the eight points (a link to its Areas section read oddly); Where opens How it's said. Checked in a browser.
  - [ ] A fluent speaker checks the Welsh heading, *Pynciau cysylltiedig* (a line is in `docs/REVIEW.md`).
  - [ ] Decide whether more topics should link (Sky, Temperature, Warnings), and whether Where should link to more than How it's said.
  - [x] Put related topics in the how-to page, in both languages. Done 2026-10-23 as the *Linked topics* entry of the help book (`help-reading-a-topic.html#related-topics`); the Welsh is a draft in `REVIEW.md`.
  - [ ] Later, if wanted: links from single phrases (for example "Snow on high ground" to "On high ground"). More precise, but it means editing individual phrases.
- [x] **Grade tiles and sections from beginner to advanced, with a setting for the order.** Done 2026-10-23, apart from the review items below. Each group, page and section has a level (1 beginner to 3 advanced) worked out from what it holds; the build writes it on every tile and topic section (`data-level`); **Settings** offers *Default* (as written, the listen-first order, and what everyone gets until they choose), *Simplest first* and *Most advanced first* (shown only where the levels differ); and `assets/order.js` puts tiles, sections and the "On this page" list in order before the page is painted, and in the copy of a page that `nav.js` slides in, so nothing is seen moving. Written up in the framework README, `framework/docs/FRAMEWORK.md` (*Grading*, *Putting tiles and sections in order*), the content-tree skill and the project memory.
  - [x] **What is graded: tiles and sections** (decided 2026-10-23). Not single words or phrases yet; that could come later.
  - [x] **How: by their content, not by hand.** The level is the median number of words per entry in the heard language (under 1.5 is level 1, under 2.5 level 2, else 3), worked out by `framework/phrasebook/grading.py`; `"level"` on a group, page or section sets it by hand; `python3 build.py --grades` prints the grades to check; the edition may set `grading.language` and `grading.bounds`. Graded: *points* (north = gogledd) is 1, *regions* 2, *directions* and *landscape* (in the north, in the hills) 3, the sentence patterns 3, the single-word weather pages 1. One set by hand: the days of the week to 1 (*Dydd Llun* is two written words but one beginner item).
  - [x] **A saved order wins.** A person's own arrangement of a screen is kept as it is; the setting orders only screens with no saved order; Reset on a screen goes to the setting's order. Checked in a browser, with the other cases.
  - [x] **Inside a page: the levels reversed, not words always first.** Suggested earlier: keep the words-for-things groups first whatever the setting says. Dropped, because the request was that more advanced users may want the other way round (phrases first). *Most advanced first* is the levels reversed with the written order kept among equals, and a section with no level (a drawing) stays where it is.
  - [x] **Setting and ordering code.** A validated `order` preference in `app.js`; `order.js` (stable sort by level, before the first paint, and for the slide-in copy); the Settings card with `order_*` messages; `arrange.js` takes its two orders from the lists (`data-written`, `data-default`). Tested under Node (`tests/order.test.js`, `tests/app.test.js`), in Python (`framework/tests/test_tree.py`, `test_grading.py`) and in a real browser (ordering with `arrange.js` blocked, sections and their list, the slide-in copy, Reset, the Settings choice).
  - [x] **A bug found and fixed on the way.** The earlier before-paint tile order made Reset restore the *saved* order, not the default, because `arrange.js` took its default from the page after it had been reordered. It now reads `data-written` and `data-default`.
  - [ ] A fluent speaker reviews the grades and the Welsh for the new setting (`Trefn`, `Arferol`, `Y symlaf yn gyntaf`, `Y mwyaf datblygedig yn gyntaf` and the hint); lines are in `docs/REVIEW.md`.
  - [ ] A measure for languages written without spaces between words (the count is by white space).
  - [x] Put the setting in the how-to page, in both languages. Done 2026-10-23 (`help-your-settings.html#order-setting`, `help-reading-a-topic.html#levels`); the Welsh is a draft in `REVIEW.md`.
  - [ ] Maybe later: grade single words and phrases, and let the Search results or a topic's rows use the levels.

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

- [x] **Accordions on Settings and About.** Both pages were getting long, so each Settings card and each About section folds. They are `details` elements, so they work with no script and the controls inside a shut card keep their state. On Settings only Appearance starts open; on About the first two sections do (set per section with `open` in `about_page`). *Regrouped 2026-10-23:* the Settings folds are now functional groups, **Accessibility and appearance** (View mode, Accessibility, Colour schemes; open to begin with), **Order and tile layout** (Order, Tile layout) and the regional forms, each choice a headed sub-section of its group.
  - [ ] Remember which cards and sections are open between visits.
  - [ ] An "open all / close all" control for the About page.
  - [ ] Show the current choice in a shut card's summary (for example "Colour schemes: Red and green").
  - [ ] Look at them in a real browser: keyboard, VoiceOver and TalkBack, forced colours, right to left.

### 3.4 Usability

- [x] **The weather forecast is one page** (design pivot, 2026-10-26): there were too many separate pages under weather. The group has `"layout": "one-page"`, so each weather topic is an accordion on the group's page, shut by default, with the topic's tile (icon and both names) as its summary. Settings' order (simplest or most advanced first) now orders the accordions on the page, not the sections inside them. The weather topics have no pages of their own: search, related tiles and the group's link to Where point into the one page.
- [ ] Check the one weather page in a real browser: opening a search result or a related tile inside a shut accordion (it should open and scroll to the word), on a phone, in light and dark, with forced colours and a screen reader.
- [ ] Decide whether other groups (Everyday) should be one page too: it is one line in `structure.json` per group. Geography is one page since 2026-10-27.

Script to generate and test each screen and score them for usability. Run each time a screen is modified. Not every build.

- [x] **Search card actions are symbols** (2026-10-26): an x to close and a delete symbol to clear the field, in place of the word Close and the browser's own clear button. The rule is in `FRAMEWORK.md`; the `symbolic-actions` skill audits the rest.
- [ ] **Make the remaining form actions symbolic** where a symbol says it (see the skill's audit): Save order and Reset in the edit-order bar, and the help sheet's What's this?, Report a problem, Copy and Back. Keep the words for Reset tile layouts. Each needs an icon (`ui-icons/`, with its `ASSETS.md` entry), a name for a screen reader, a test, and the help text updated.

### 3.5 Screen tile reordering

Ability to customise the order of tiles on home page and sub pages. A spanner or other icon - toggle the edit order mode on. Edit order mode shows smaller buttons with just their icon. User can drag the buttons to where they want like on an app screen. Toggle edit mode off saves the new config. 
Screen background changes colour, and the toggled edit icon background matches it. Title says drag to reorder. Needs a reset default option.

- [x] **Done.** Edit order on the home page and group pages (the spanner in the rail): drag a tile, or tap it and tap where it goes, or move it with the keys. Save order keeps it on this device, and leaving without saving drops the change. Reset puts a screen back in its default, and Settings resets every screen at once. The Welsh strings are first drafts in `REVIEW.md`.
  - [ ] Check it by hand on a phone, with TalkBack and VoiceOver, right to left, forced colours, and in each palette, light and dark.

### 3.6 Report issue screen

Merged into 3.7 (2026-10-23): reporting shares its first step with help, so it is one feature, "Ask about this". The original idea is kept below.

> Via a flag icon on the side bar. Opens a mode like edit mode, says select the element that is wrong, or skip - button to skip. Next step, an email is created with a report section in markdown filled out. User can type what else they want and the email is sent. Can it send in the background? Can I set up a separate email for it?

Answer to the last question: no background sending. The person's own mail app sends it (see 3.7).

### 3.7 App help and report an issue ("Ask about this")

Help is a book under About, with in-context help reached from the screens themselves. Reporting an issue shares the same first step, so the two are one feature. The audit and the detailed list are in `framework/docs/app-help-todo.md`; the `app-help` skill (`.claude/skills/app-help/SKILL.md`) re-runs the audit.

**The flow (first draft, 2026-10-23).**

1. A question-mark button in the rail, 4th slot from the bottom (above edit order, About and Settings), turns on a mode. A bar says what to do and has *This page* and *Done*. Small question-mark icons appear on features and tiles.
2. Touching an icon opens a small sheet with **What's this?** first, then **Report a problem**.
3. *What's this?* opens an overlay that loads the text of `help-<chapter>.html#feature`. *Report a problem* shows a preview of the email, with a box for what is wrong.
4. *Open email* opens the person's own mail app with the context filled in. *Copy* puts the same text on the clipboard.

**Decisions and why.**

- **`mailto:` and no background sending.** The app has no server and makes no request except for its own pages. A `mailto:` needs no backend, and the person sees exactly what is sent and presses Send. This keeps the promise that nothing leaves the device unseen. Cost: it needs a mail app, so the preview offers *Copy* and shows the address as plain text.
- **The context the app adds is at most 256 characters** (decided 2026-10-23). The person's own words are extra. Reasons: long `mailto:` links are truncated or refused by some mail apps and browsers; a longer block means more to build, test and explain on every device; a report only needs to say *where*. Anything over 256 means the feature is getting too complex, so the answer is to cut the context, not to raise the limit.
- **What goes in the 256, in order of what is cut last:** page and section (`rain.html#landscape`), the help anchor or element id, the app version (commit short hash), the language pair and the direction. Cut first, and left out by default: saved settings, screen size and user agent. Never page text beyond a short word.
- **Same anchor, two uses.** The `data-help` anchor on an icon is also the report's context, so the book and the reports cannot drift apart.
- **Reports are not only about features.** *This page* in the bar reports the page. A row-level icon is not proposed, because it would clutter phrase tables.
- **The icon is a question mark** (it means "ask"), and the sheet names both actions in words, because a question mark alone does not say "report".

**To do.**

- [x] **The book.** Done 2026-10-23 (plan: `framework/docs/app-help-plan.md`, phases 0 to 3): `how-to.html` is the contents, six chapters are published as `help-<chapter>.html#<feature>` in English with a Welsh draft, and a seventh (Using help) is written but not shown until the help button exists. Audit and what is left: `framework/docs/app-help-todo.md`. Still to do: a fluent speaker checks the Welsh, and the chapters are read in a browser.
- [x] **In-context icons.** Done 2026-10-23 as a first set: the trail, tile grids, a topic's jump links, section Order lines, the pager, the Related row, and six Settings choices. Each is a hidden link marked `data-help="<chapter>#<feature>"` to the book. More can be added with `Site.help_icon`. Which other features and tiles should have one is still open.
- [x] **Rail help button**, in the 4th slot from the bottom (above edit order, About and Settings). Done 2026-10-23 (`assets/help.js`, `#help-toggle`): pressing it, or Escape, shows and hides the icons; nothing is stored. It is not yet the Report entry (the report flag in 3.6 is merged into this button, to come with the sheet).
- [x] **Sheet.** Done 2026-10-23: touching an icon opens *What's this?* (first) and *Report a problem*. The sheet has the Cy|En toggle (not two languages stacked) and closes with a small x, Escape or a tap outside; focus returns to the icon; the page behind is inert. Checked in headless Edge on the home, a topic and the Settings page.
- [x] **Report: build the context.** Done 2026-10-23: at most 256 characters (page, help topic, build date, languages), a preview with a box for the person's words, *Open email* (`mailto:` to the edition's `contact`, `cydymaithapp@gmail.com`, kept in two pieces in the page) and *Copy*. The app sends nothing. Still to try by hand: the `mailto:` link on Android Chrome, iOS Safari and a computer with and without a mail app.
- [x] **Overlay.** Done 2026-10-23: *What's this?* shows that feature's text from its chapter (read from the cached chapter page, in each language it is written in), with *Read the whole chapter* beneath.
- [x] **Write the help, in both languages.** Done 2026-10-23: seven chapters in English and a Welsh draft; the old `how_to_*` messages are gone. Welsh is a draft until a fluent speaker checks it (`REVIEW.md`).
- [ ] **Fold in the older items:** related topics and the Order setting are done; the weather worked example is still to do.
- [x] Update `FRAMEWORK.md`, which said the how-to page "explains all of this" and described the rail without About or Edit order. Done 2026-10-23.

## Done

- [x] Restructure into data files, tests, CI and deploy workflow
- [x] Sources and licences on every pack
- [x] Framework split into its own repository (`cydymaith-framework`) and used here as a submodule in `framework/`
- [x] Release channels: sections marked `development` are held back from the release build (`phrasebook/channels.py`)
- [x] Language-agnostic framework with packs and editions
- [x] Framework separated from the content, with a localisable interface
