# Welsh review checklist

All Welsh in `content/cydymaith/` was written from memory by an AI model and has **not** been checked by a fluent speaker. Review before any public announcement.

## How to review

1. Read each page in `dist/` (or the deployed site) and mark each section below.
2. Fix entries directly in `content/cydymaith/packs/cy/pages/<slug>.json`, or open a "Welsh correction" issue.
3. Record the reviewer and date in the table at the end.

## Check these first

Entries where the author is least certain:

| Page | English | Welsh as written | Question |
|---|---|---|---|
| sky | It's fine | `Mae hi'n braf` | Does `braf` stay unmutated after predicative `yn`? |
| when | Evening | `Min nos` | Is this the right word for "evening" in a forecast? `gyda'r nos` appears in the note, and `yr hwyr` may be an alternative. |
| rain | Thunderstorm | `Storm fellt a tharanau` | Is there a more usual single term? |
| food-drink | Milk | `Llaeth` (south) and `Llefrith` (north) | Confirm the spelling `llefrith` and which region each form belongs to. `llaeth` is also the standard literary word, so a "standard" variety may be wanted. |
| sky, rain, snow-ice, wind, temperature, warnings, when, where, patterns, talk | Page titles (the weather pages were regrouped again by the content-tree review: the forecast first, rain and snow split, sentences gathered on one page, talk moved to Everyday) | `Yr awyr a gwelededd`, `Glaw a stormydd`, `Eira a rhew`, `Gwynt`, `Tymheredd`, `Y rhagolygon`, `Pryd`, `Ble`, `Patrymau`, `Sôn am y tywydd` | All first drafts. Check each, and whether `Pryd` and `Ble` read well as tile names. |
| warnings, rain, snow-ice, wind, temperature, when, where, patterns | New section titles | `Y tywydd a'r rhagolygon`, `Lefelau rhybudd`, `Rhybuddion am`, `Mellt a tharanau`, `Rhew ac iâ`, `Cryfder y gwynt`, `Tymheredd a lleithder`, `Y dyddiau i ddod`, `Rhannau'r dydd`, `Ardaloedd`, `Mae hi'n …`, `Beth sy'n digwydd`, `Bydd hi'n …`, `Bydd …`, `Enwi'r gwynt`, `Pa mor eang` | First drafts. `Beth sy'n digwydd` and `Pa mor eang` are the least certain. |
| patterns | Sentence patterns | the *mae hi'n* mutation note, now written once on the "It is…" section, and a new matching note on "It will be…" | The 33 sentences moved here from the sky, rain, wind and temperature pages. Check the new *bydd hi'n* note, and that each sentence sits under the right pattern. |
| wind | A south-westerly wind | `Bydd gwynt de-orllewinol` (the forecast sentence) beside `Gwynt de-orllewinol` (the phrase) | The two now sit on one page. Confirm both. |
| geography | Places, Beyond Wales | the town and country names (Geography is now released) | Moved from the weather pages. Check the spellings (`Caerdydd`, `Abertawe`, `Casnewydd`, `Wrecsam`, `Caergybi`). |
| food-drink | Page, section and group titles | `Bwyd a diod`, `Diodydd`, `Geiriau bob dydd` | Check wording. |
| geography | Group, page and section titles | `Daearyddiaeth` (group), `Lleoedd` (the page, was `Daearyddiaeth`), `Trefi a dinasoedd` (was `Lleoedd`), `Y tu hwnt i Gymru` | Now released (it was held back). The titles are from the navigation mockup, so confirm them. |
| news, sport | Group, page and section titles | `Newyddion`, `Chwaraeon` | Held back from the release until reviewed. Confirm them, and `Chwaraeon` for "Sports" against `Chwaraeon` for "Sport". |
| place-name-elements | Page, section titles and all 46 elements, their meanings and the example names in the notes | `Elfennau enwau lleoedd`; `Aneddiadau ac adeiladau`, `Dŵr`, `Bryniau a chreigiau`, `Cymoedd a chaeau`, `Ffyrdd a chroesfannau`, `Geiriau disgrifio`; elements such as `llan`, `aber`, `caer`, `ffordd`, `heol`, `llys`, `maes`, `pont`, `porth` | Written from memory, with no source cleared (see the sources logged in `docs/TODO.md`). Check each meaning and each example name. Least certain: `heol` as "common in south Wales", `Casnewydd` from `castell` (`cas`), `Penarth` as `pen` + `garth`, `betws` as "prayer house, chapel", and the explanation of why the spelling changes. Add the regional forms (varieties) where an element is local. |

| time-and-place | Group title | `Amser a lle` | First draft. Weather links to this group for When and Where. |
| sky, rain, wind, temperature, warnings, when, where | "Also heard as" forms | `cymylau`, `gymylog`, `cyfnodau heulog`, `law`, `cawod`, `ambell gawod`, `wlyb`, `lifogydd`, `wynt`, `wyntog`, `gynnes`, `boeth`, `dywydd`, `ddydd Llun` to `ddydd Sul`, `ngogledd`, `ne`, `ddwyrain`, `nwyrain`, `orllewin`, `ngorllewin`, `Nghymru` | The changed beginnings come from the mutation notes already on those pages; the plurals come from the old notes. Check each, and which of them a forecaster really says. `ambell gawod` is new. |
| patterns (held back) | Linking, time, movement, pressure and greeting words | `Ar y cyfan`, `Wedyn`, `Ond`, `Hefyd`, `Yn ystod y dydd`, `Erbyn`, `Tan`, `Yn nes ymlaen`, `Bore fory`, `Nos yfory`, `Clirio`, `Lledu`, `Symud`, `Brafio`, `Tua'r dwyrain`, `Ar draws`, `Gwasgedd uchel`, `Gwasgedd isel`, `Noswaith dda`, `Dyna'r tywydd`, `Ambell gawod`, `Cyfnodau sych`, `Hyd at`, `Rhwng … a …` | Written from memory as candidates and held back from the release (`status: development`) until checked. Compare with a recent Welsh forecast. `Brafio` is colloquial; confirm it and whether `Bore fory` should be `Bore yfory`. |
| patterns (held back) | Section titles | `Faint`, `Geiriau cyswllt`, `Geiriau amser`, `Y tywydd yn symud`, `Gwasgedd`, `Agor a chau` | First drafts. |
| sky, wind, temperature, warnings, when, where, patterns | Words heard on the S4C forecast | Released: `Heulwen`, `Awyr las`, `Llwydaidd`, `Sefydlog`, `Ansefydlog`, `Cyfnewidiol`, `Cymedrol` (heard `gymedrol`), `Ar ei uchaf`, `Ar ei isaf`, `Posibilrwydd`, `Hanner nos`, `Tymor`, `Hanner tymor`, `Cynta'r tymor`, `Gwlad` (heard `wlad`), `Ardaloedd`. Held back on How it's said (`status: development`): `Ychydig`, `Digon`, `Rhyw`, `Rhai`, `Eraill`, `Canol`, `Diwrnod`, `Cyrraedd`, `Cilio`, `O ran`, `Yn ogystal â`, `Dyna pryd`, `Golygu`, `Hwnnw`, `Cymylu`, `Datblygu`, `Syrthio`, `Cryfhau`, `Chwythu`, `Newid`, `Amrywio`, `Effeithio`, `Dod i rym`, `Uwch`, `Ysgafnach`, `Nag`. Also `hyrddiadau` as a form of `Hyrddiau`. | The Welsh spellings come from the subtitles; the English meanings are first drafts. Check each, the section titles `Golwg yr awyr`, `Tymhorau`, `Cyflwyno pwynt`, `Berfau`, `Cymharu`, and whether `Cynta'r tymor` is wanted. |
| all pages | Beginner-to-advanced grades (level 1, 2 or 3) | worked out from the median words per Welsh entry (`python3 build.py --grades`); one set by hand: the days of the week (`when`, `days`) to level 1 | Read the report as a learner would. Do single words come before the phrases built on them, and sentence patterns last? Is any section too easy or too hard for its level, or is a level set by hand wrongly? A level is a judgement about difficulty. |
| topic pages | The accessible name of the list of sections on a topic | `Ar y dudalen yma` (On this page) | Draft, from the machine translation `ar tudalen yma`, with the article and mutation added (`ar y dudalen`). Is `yma` or `hon` better? |
| rain, snow-ice, wind, patterns, where | The Related topics row heading | `Pynciau cysylltiedig` (Related topics) | Draft. Is it the right wording for a row of tiles that link to other topics? |
| settings | The Settings groups and headings | `Hygyrchedd a golwg` (Accessibility and appearance), `Modd gweld` (View mode, was `Golwg`), `Trefn a chynllun y teils` (Order and tile layout), `Cynllun y teils` (Tile layout) | Drafts. Are `Modd gweld`, `Hygyrchedd a golwg` and `Trefn a chynllun y teils` the right wording? |
| settings | The order setting: title, hint and three choices | `Trefn`, `Y symlaf yn gyntaf, neu'r mwyaf datblygedig yn gyntaf. Mae sgrin y gwnaethoch drefnu ei theils eich hun yn cadw eich trefn.`, `Arferol` (as written), `Y symlaf yn gyntaf`, `Y mwyaf datblygedig yn gyntaf` | Drafts. Is `Trefn` the right title, `Arferol` a good short label for the default (the longer `Rhagosodedig` was too wide for the control), and is the hint clear? |
| about page | The "no AI" promise (`Dim deallusrwydd artiffisial: nid yw'r ap byth yn galw ar wasanaeth AI na model iaith.`), and the title, section titles and every paragraph and list item of the About page, and the rail and trail label | `Ynglŷn â Chydymaith am iaith`, `Beth yw ei bwrpas`, `Sut mae'n gweithio`, `Ein haddewidion`, `Bod yn onest am y Gymraeg`, `Yr hyn nad ydyw`, `Amdanom ni`, and the paragraphs under them in `content/cydymaith/editions/cydymaith.json` | Written by an AI model as a draft and not checked. Check the grammar and register throughout, and whether `Amdanom ni` suits as a label. |
| palette | Names of the Yellow and green colour schemes | `Melyn a gwyrdd`, `Melyn a gwyrdd, diogel`, `Melyn a gwyrdd, cyferbyniad uchel` | First drafts, used in the settings page. |
| interface | The revised settings page | `Gosodiadau`, `Golwg`, `Hygyrchedd`, `Safonol`, `Lliwiau diogel`, `Cyferbyniad uchel`, `Cynlluniau lliw`, `{language}: ffurfiau rhanbarthol`, `Ynglŷn â'r ap` `Sut i ddefnyddio'r ap` (the how-to link) and the hints under each | Written by an AI model as drafts. Check the grammar and register, and `Safonol` / `Lliwiau diogel` as level names. The palette names `Coch a gwyrdd`, `Coch a gwyrdd, diogel` and `Glas a melyn, diogel` are new. |
| about page | Technoleg Dda: the founding statement, `Technoleg Dda`, the seven promises, the offline-install steps, the share and correction text, the open-source section and the held-back `Ble nesaf` section; the buttons `Rhannu` and `Cyswllt wedi'i gopïo` | `Dylai technoleg wasanaethu'r sawl sy'n ei defnyddio, heb ofyn dim yn ôl.` and the paragraphs and list items under `Technoleg Dda`, `Ei osod i'w ddefnyddio all-lein`, `Ei rannu`, `Ffynhonnell agored`, `Ble nesaf` in `editions/cydymaith.json` | Drafts. Least certain: the statement itself, the browser menu names in the install steps (`Gosod yr ap`, `Ychwanegu at y sgrin gartref`), and `Dim yn gudd` with its long sentence. |
| all | Regional labels | every `varieties` tag | Every N and S label needs checking entry by entry. |
| all | Mutation notes | boxes and intros | Check every explanation of soft and nasal mutation for accuracy. |
| interface | Site text | `content/cydymaith/packs/cy/pack.json` and `.../editions/cydymaith.json` | Check `Hafan`, `Prif ddewislen`, `Cymraeg`, `Llyfr ymadroddion`, `Ffynonellau`, the group title and `Ymadroddion bob dydd, Cymraeg i Saesneg` (the pair now runs Welsh to English). |
| interface | Edit order and tile layout | `Golygu'r drefn`, `Cadw'r drefn`, `Ailosod`, `Cynllun y teils` and the messages in `packs/cy/pack.json` (`arrange_*`, `reset_orders_*`) | First drafts. Check the labels and the spoken announcements (a screen reader reads `arrange_picked`, `arrange_moved` and `arrange_cancelled`). `Cadw'r drefn` is the Save button. |

## Questions of register

- Written standard Welsh is used throughout. Should spoken forms for the north and the south be offered alongside?
- The Met Office and BBC Cymru use set forecast vocabulary. Compare against a recent Welsh-language forecast.

## Sign-off

| Page | Reviewer | Date | Notes |
|---|---|---|---|
| warnings | | | |
| sky | | | |
| rain | | | |
| snow-ice | | | |
| wind | | | |
| temperature | | | |
| when | | | |
| where | | | |
| patterns | | | |
| talk | | | |
