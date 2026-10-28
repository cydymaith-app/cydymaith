# Forecast words: synthesis and placement plan

The words collected from S4C broadcasts (uploads 1 to 12, October 2026; upload 12 is in section 10: *Y Dyddiau Nesaf*, *Dros Nos* and one *Newyddion* storm report), checked against the content as it stands after the Temperature regroup (commit `ed15e9f`), with duplicates removed and each word given one home.

**Update, 27 October 2026:** the weather cards now hold forecast phrases in place of these single words, and The forecast card (`warnings`) is gone: its warnings are phrases on the cards, its pressure is on Change and movement. The tables below record where each word was placed on 26 October; the words live on inside the phrases (see `REVIEW.md`).

**Status: carried out on 26 October 2026, except what is shelved (section 9).** Where the content differs from the tables below: *Fine spells* is its own row (not a form on *dry spells*), and Faint is split so that *Rhyw*, *Hyd at* and *Rhwng … a …* sit in a held section, *O gwmpas rhif / Around a figure*, until the units page is written. Pressure sits second on The forecast page, and *Rheoli* is on Other verbs. Nothing here is in the app yet. Every Welsh word and gloss is a draft until a fluent speaker has checked it (see `REVIEW.md`). The raw lists per upload are in the memory file `broadcast-words-to-collect.md`.

## How to read the tables

| Action | Meaning |
|---|---|
| **New** | a new row |
| **Form** | an "also heard as" form on an existing row (searchable, no new row) |
| **Move** | an existing held-back row moved to a better home |
| **Have** | already in the content as heard; no change |

Upload numbers are in brackets, for example (7, 10).

## Summary

- After removing duplicates, names and items already in the content, the plan has:
  - 60 new rows;
  - 10 new forms on existing rows;
  - about 17 held-back rows moved to a better home.
- Many new rows carry their own heard forms as well (*also* in the tables).
- Shelved (section 9): 51 rows, kept so nothing is lost.
  - Travel;
  - the new sentence patterns on How it's said;
  - Short forms and On screen;
  - additions to Agor a chau and Cyflwyno pwynt;
  - Sequence.
- Already in the content as heard: about 70, including everything heard about temperature. The updated Temperature page needs no new rows from the broadcasts.
- Two new homes are proposed:
  - an **Impacts** page (the sea, damage);
  - a **Pressure** section on The forecast.
- The **When** page becomes **Time and date**, reached from the forecast as a related page.
- How it's said goes from 15 sections to 12 (6 released, 6 held), because the change and movement sections and pressure move off it.

## 1. Already in the content (no change)

Grouped by page:

- **Sky:** *heulwen*, *awyr las*, *llwydaidd*, *sefydlog*, *ansefydlog*, *cyfnewidiol*, *sych*, *braf*.
- **Rain:** *glaw trwm*, *cawodydd*, *wlyb*, *glaw*, *storm*.
- **Wind:** *gwyntoedd cryfion*, *awel*, *gymedrol*, *hyrddiadau*, *milltir yr awr*.
- **Temperature:** *ar ei uchaf*, *ar ei isaf*, *uchaf*.
- **The forecast:** *tywydd*, *Y Swyddfa Dywydd*, *posibilrwydd*, *rhybudd melyn*, *mewn grym*.
- **When:** *heddiw*, *heno*, *dros nos*, *hanner nos*, *penwythnos*, the days with *ddydd*, *tymor*, *hanner tymor*, *cynta'r tymor*.
- **Where:** *de-orllewin*, *dwyrain*, *gogledd*, *wlad*, *ar yr arfordir*.
- **How it's said:** *ardaloedd*.
- **Already held back on How it's said** (placed below, not repeated here): *digon*, *rhai*, *ychydig*, *eraill*, *rhyw*, *hyd at*, *rhwng*, *ar y cyfan*, *ond*, *hefyd*, *yn ystod y dydd*, *erbyn*, *tan*, *bore fory*, *nos yfory*, *canol*, *diwrnod*, *cyrraedd*, *lledu*, *ar draws*, *cilio*, *gwasgedd uchel*, *gwasgedd isel*, *noswaith dda*, *o ran*, *yn ogystal â*, *dyna pryd*, *golygu*, *hwnnw*, *cymylu*, *datblygu*, *syrthio*, *cryfhau*, *chwythu*, *newid*, *amrywio*, *effeithio*, *dod i rym*, *uwch*, *ysgafnach*, *nag*.

### One overlap from the Temperature update

*Sych* (`dry`) now has two homes: Sky › Sun and cloud, and Temperature › How humid. The Welsh is written twice, so it can drift.

- **Decided:** keep both. Each scale needs it as an end point: no rain on Sky, the dry end on Temperature. Add a test that the two texts match, in both packs.

## 2. Structure changes

Revised 26 October 2026 after the user's decisions. Shelved work is in section 9.

**Decided:**

- Title *Amser a dyddiad / Time and date*.
- A related tile only (no group link).
- Impacts shelved with Travel.
- Change and movement as a new page.
- *Sych* kept on both pages, with a test.
- Wind strength and *Y dyddiau i ddod* each one ordered section.

**Done:** the content is in, as drafts.

| Change | Sections | Status |
|---|---|---|
| **Newid a symud / Change and movement**, a new page in the weather group, moved off `patterns` | Y tywydd yn symud; **I ba gyfeiriad** (new); Newid (the current held `verbs`, retitled); **Berfau eraill** (new) | held |
| **Gwasgedd / Pressure**, a new section on The forecast (`warnings`), moved off `patterns` | Gwasgedd | held |
| **Amser a dyddiad / Time and date**: the `when` page, retitled | Y dyddiau i ddod; Rhannau'r dydd; Dyddiau'r wythnos; Tymhorau; **Cyn ac ar ôl** (new, held) | released |
| **Patrymau / How it's said** keeps its released sentence patterns and these sections | Pa mor eang; Faint; Geiriau cyswllt | as now |

### Time and date as a related page

- The weather group drops its `links` tile to `when`. The forecast page (`warnings`) gets `"related": ["when"]`, so a listener reaches Time and date in one tap from the forecast, and Back returns them there.
- The slug stays `when`, so no address changes.
- The page stays in Time and place, where other groups (News, Sport) will link to it.
- **Title (decided):** *Amser a dyddiad / Time and date*. This breaks the question pair *Pryd / Ble* (When / Where) in Time and place; accepted.
- **Later additions, in `TODO.md`:** the four seasons and the months, and the Sequence section (*Trefn*) from section 9.

### Pressure

- No existing section fits.
  - *Y tywydd a'r rhagolygon* would go to 14 rows.
  - Sky's *Golwg yr awyr* is about how the sky looks, not the chart.
- So pressure gets its own section on The forecast: the chart is part of the forecaster's explanation.
- The page goes from 3 sections to 4. Placed second, after *Y tywydd a'r rhagolygon*, because the chart comes before the detail and the warnings.

### Group order and addresses

- **Proposed group order:** Y rhagolygon, Yr awyr, Glaw, Eira, Gwynt, Tymheredd, Newid a symud, Patrymau, Ble (link). If Impacts comes back, it goes straight after the forecast, because a warning is written as a list of effects.
- **Addresses that change:** none of the released ones. Only held sections move, and they have never been published.
- How it's said goes from 15 sections to 12.
  - It keeps its 6 released sections.
  - It keeps Faint and Geiriau cyswllt, which get new rows.
  - It keeps Agor a chau, Cyflwyno pwynt and Cymharu, held as they are (their additions are shelved, section 9).
  - It keeps Geiriau amser, held, with the two words that wait for Sequence.

## 3. Placement, page by page

### The forecast (`warnings`)

**Y tywydd a'r rhagolygon** (9 rows). Order: the weather, then the forecast, then how certain it is.

| Welsh | English | Action |
|---|---|---|
| Tywydd garw | rough weather | New (7, 10) |
| Rhybuddio | to warn | New (11), next to *Rhybudd tywydd* |
| O bosib *also* o bosibl, yn bosib | possibly | New (7, 8, 11) |
| Yn debygol | likely | New (7) |

**Lefelau rhybudd** (6 rows). Order: the levels, then issuing, then in force.

| Welsh | English | Action |
|---|---|---|
| Cyhoeddi | to issue (a warning) | New (10) |
| Dod i rym | to come into force | Move from held Verbs (4, 10), next to *Mewn grym* |

**Gwasgedd / Pressure** (new section, held; moves from `patterns`; 5 rows). Order: the word, then high, then low.

| Welsh | English | Action |
|---|---|---|
| Gwasgedd *also* wasgedd | pressure | New (7) |
| Gwasgedd uchel | high pressure | Move from held `patterns` › Gwasgedd |
| Cefnlen o wasgedd uchel | a ridge of high pressure | New (7); the meaning of *cefnlen* is uncertain |
| Gwasgedd isel | low pressure | Move from held `patterns` › Gwasgedd |
| Ardal o wasgedd isel *also* ardal o wasgedd isel dwys | an area of (intense) low pressure | New (7); *dwys* (intense, deep) as a form, not a row |

*Rheoli* (to dominate, said of high pressure) goes to Berfau eraill.

**Rhybuddion am** (no new rows)

| Welsh | English | Action |
|---|---|---|
| *rhybudd melyn o wynt*, *rhybudd melyn am wynt* | yellow wind warning | Form on *Rhybudd am wynt* (6, 10) |

### Wind (`wind`)

**Cryfder y gwynt** grows to 12 rows (decided: one section, not split). That is over the guide, so order it for scanning: the noun and verb first, then calm to strongest, then measures.

| Welsh | English | Action |
|---|---|---|
| Chwythu | to blow | Move from held Verbs (3) |
| *gwynt cryf* | strong wind | Form on *Gwyntoedd cryfion* (8) |
| *hyrddio* | to gust | Form on *Hyrddiau* (7, 8) |
| Ar ei gryfaf *also* gryfa' | at its strongest | New (7, 8); the same pattern as *ar ei uchaf* on Temperature |

### Temperature (`temperature`)

- No new rows. Everything heard is already there after the regroup.
- *oerach* goes under Comparing, which is shelved (section 9).
- Figures such as `6C` go to the units page.
- The gaps the Temperature review raised (freezing, cool, sticky, heatwave) have not been heard on air yet.

### Time and date (`when`, retitled; a related page from The forecast)

**Y dyddiau i ddod** grows to 12 rows (decided: one section, not split), ordered nearest to furthest.

| Welsh | English | Action |
|---|---|---|
| Yr oriau nesaf *also* yr oriau sydd i ddod | the next few hours | New (10, 11) |
| *fory* | tomorrow | Form on *Yfory* (7, 8) |
| Bore fory *also* mewn at bore fory | tomorrow morning | Move from held Time words (11) |
| Nos yfory *also* nos fory | tomorrow night | Move from held Time words (4) |
| Y dyddiau nesaf | the next few days | New (1; the programme's title) |
| Gweddill yr wythnos | the rest of the week | New (11) |

**Rhannau'r dydd** (9 rows)

| Welsh | English | Action |
|---|---|---|
| Oriau mân | the small hours | New (8), after *Hanner nos* |
| Diwrnod | a day | Move from held Time words (4) |

**Cyn ac ar ôl / Before and after** (new, held; 9 rows). Order: stretches of time first, then points in time in sequence.

| Welsh | English | Action |
|---|---|---|
| Yn ystod *also* yn ystod y dydd, yn ystod y bore | during | Move (3, 5) |
| Dros *also* dros y penwythnos, dros yr oriau nesaf | over | New (10, 11) |
| Am gyfnod | for a while | New (7) |
| Cyn *also* cyn cymylu | before | New (3) |
| At *also* at heno | towards, by | New (3) |
| Erbyn *also* erbyn iddi wawrio, erbyn diwedd y prynhawn | by | Move (5, 7, 8) |
| Tan *also* tan dri o'r gloch y bore | until | Move (10) |
| Ar ôl | after | New (7) |
| O … ymlaen *also* o ganol yr wythnos ymlaen | from … onwards | New (7) |

- *Yn nes ymlaen* and *Canol* stay in the held `patterns` › Geiriau amser until the Sequence section is written (section 9).
- **Later, in `TODO.md`:** the four seasons in *Tymhorau*, a months section, and *Trefn / Sequence*.

### Where (`where`)

**Tirwedd** (8 rows)

| Welsh | English | Action |
|---|---|---|
| *arfordirol*, *rhannau arfordirol* | coastal | Form on *Ar yr arfordir* (10) |
| Yn y mewndiroedd *also* mewndiroedd | inland | New (10) |

- *yng ngorllewin y wlad* (8) is the best example heard of the nasal mutation. Use it in the mutation decoder, not as a row.

### How it's said (`patterns`): the sections still in the plan

The released sentence patterns get no new rows. The other planned additions are shelved (section 9).

**Geiriau cyswllt** (held; 10 rows)

| Welsh | English | Action |
|---|---|---|
| *a hefyd* | and also | Form on *Hefyd* (8) |
| Yn ogystal â | in addition to | Move from held Cyflwyno pwynt |
| Gan gynnwys | including | New (10) |
| Sef | namely | New (7) |
| Felly | so | New (7, 11) |
| Fel | like, as | New (7) |
| Unwaith yn rhagor | once again | New (7) |
| Gyda *also* hefo | with | New (10) |
| *Ar y cyfan* | | Move to Pa mor eang |
| *Wedyn* | | Stays here until *Trefn / Sequence* is written |

**Pa mor eang** (released; grows from 2 to 6 rows). Order: widest to narrowest.

| Welsh | English | Action |
|---|---|---|
| Ar y cyfan | on the whole | Move from held Linking (5, 9) |
| Y rhan fwyaf o *also* ran fwya' | most of | New (10) |
| Yn bennaf | mainly | New (10) |
| Lleoedd *also* llefydd | places | New (10) |

**Faint** (held; 10 rows). Order: least to most.

| Welsh | English | Action |
|---|---|---|
| Dim ond | only | New (8) |
| Ryw fymryn *also* fymryn | a little bit | New (5, 11) |
| *cyfnodau braf* | fine spells | Form on *Cyfnodau sych* (8) |
| *rhai o'r* | some of the | Form on *Rhai* (11) |
| Llawer o | a lot of | New (7) |
| Rhagor | more | New (7, 10) |
| *Rhyw*, *Hyd at*, *Rhwng … a …* | | Move to the units page when it is written |

### Change and movement (`change`, new page, held; these sections move off `patterns`)

**Y tywydd yn symud** (8 rows). Order: arriving, spreading, leaving.

| Welsh | English | Action |
|---|---|---|
| Taro *also* yn taro | to hit | New (8) |
| *ymledu* | to spread | Form on *Lledu* (8) |
| Ymestyn | to extend | New (10) |
| Gadael *also* i adael | to leave | New (4) |
| *Brafio*, *Tua'r dwyrain*, *Ar draws* | | Move to Newid and I ba gyfeiriad |

**I ba gyfeiriad / Which way** (new; 6 rows)

| Welsh | English | Action |
|---|---|---|
| Tua'r dwyrain | eastwards | Move from Y tywydd yn symud |
| I gyfeiriad y … | towards the … | New (8) |
| O gyfeiriad y … | from the direction of … | New (7) |
| Ar draws | across | Move from Y tywydd yn symud |
| Draw tuag at | over towards | New (10) |
| Ar y ffordd | on the way | New (7) |

**Newid** (the current held Verbs, retitled; 10 rows). Order: change, then stronger, then weaker, then the sky.

| Welsh | English | Action |
|---|---|---|
| Troi *also* troi'n | to turn | New (7, 8) |
| Gostegu | to ease, subside | New (7) |
| Tawelu | to calm down | New (7) |
| *cwympo* | to fall | Form on *Syrthio* (7) |
| Brafio | to brighten | Move from Y tywydd yn symud |
| Sefydlogi | to settle | New (11) |

This section keeps *Newid*, *Datblygu*, *Cryfhau*, *Syrthio* and *Cymylu*. *Chwythu*, *Effeithio*, *Dod i rym* and *Amrywio* go elsewhere.

**Berfau eraill / Other verbs** (new; 10 rows)

| Welsh | English | Action |
|---|---|---|
| Disgwyl | to expect | New (10) |
| Parhau | to continue | New (10) |
| Digwydd | to happen | New (10) |
| Amrywio | to vary | Move from Verbs (3) |
| Cyd-fynd *also* cyd-fynd hefo | to coincide | New (10) |
| Gweld *also* weld, welon | to see | New (10, 11) |
| Clywed | to hear | New (7) |
| Edrych | to look | New (11) |
| Rheoli | to dominate (of high pressure) | New (7) |
| Effeithio *also* yn cael ei effeithio | to affect | Move from held Verbs (5, 10, 11) |

## 4. Units and numbers (for the planned `units` page)

These wait for the units page in `TODO.md`. They are not written yet.

- **Speed:** *mya* as its own row (*Hyrddio 74mya*). It is read out in full: *saith deg pedwar milltir yr awr* (8). Also heard: *60*, *84 milltir yr awr* (10).
- **Temperature:** `6C`, `13C`, `16C` on screen, with no degree sign (8). How they are said is still to be heard.
- **Clock:** *chwech o'r gloch*, *tri o'r gloch y bore* (heard as *dri*), *hanner awr wedi naw* (10); *2.00yp*, where *yp* is *yn y prynhawn* (4); the 24-hour map label `16:0…` (8).
- **Around a figure:** *tua*, *rhyw*, *o gwmpas*, *hyd at*, *rhwng … a …* (5, 10).
- **Numbers:** *dwy* (*dwy storm*, the feminine form of two) (10); *tri*, *chwech*, *naw*, *saith deg pedwar*.

## 5. Places (for the Geography review)

**Decided 28 October 2026: no lists of place names** (rule 7 in `PHILOSOPHY.md`). The names below are kept only as a record of what was heard. One goes into the content only inside a heard phrase that teaches something, such as a mutation (*yng Nghaerfyrddin*), never as a row of its own. The place-name elements are the exception.

Geography already has *Caerdydd*, *Abertawe*, *Casnewydd*, *Wrecsam*, *Aberystwyth* and *Iwerddon* (7).

To check against an official source before use:

- *Llanelwy*, *Llanfair Dyffryn Clwyd*, *Aberaeron*, *Caernarfon*, *Harlech*, *Y Drenewydd*, *Aberporth*, *Tyddewi*, *Y Fenni*, *Y Rhyl*, *Llanpumsaint*, *Hwlffordd*, *Cemaes*, *Capel Curig*, *Corwen*, *Clunderwen*, *Prestatyn*, *Llanrwst*, *Aberteifi*, *Aberhonddu*, *Llanelli*, *Porth*, *Aberdaron*, *Llanwrtyd*.
- Counties and islands: *Sir Conwy*, *Ynys Môn* (10).

## 6. Left out

- Storm names: out of scope.
- Presenters' names and people named in captions.
- Title bars and social handles.
- Map figures that are numbers only.
- *Merch Cwmwl*: a caption, a name or a graphic label. Ask before using it.
- *pethe'n* as a row: it belongs in Short forms (shelved).

## 7. Questions for a fluent speaker

Add these to `REVIEW.md` when the plan is carried out.

1. *Cefnlen o wasgedd uchel*: is *cefnlen* "ridge" here?
2. *mewn at bore fory* (11): is the subtitle right, or was it *mewn i fore fory*?
3. *Ar y ffordd* (7): "on the way" (coming), or "on the road"?
4. *Gyda* or *efo* as the main form, given that *hefo* was heard in the north?
5. The new titles: *Newid a symud*, *I ba gyfeiriad*, *Berfau eraill*, *Gwasgedd*, *Amser a dyddiad*, *Cyn ac ar ôl*.
6. For the shelved work, when it comes back:
   - *Pwyll piau hi*: is it right to show *piau* as the main form and *bia* as heard?
   - *Llanast*: is it too informal to teach as "damage"?

## 8. Tiles check

Run on 26 October 2026, after the Temperature regroup.

- **Released content:** no problems, and 25 notes. Three of the notes are on the Temperature page:
  - *Poeth ac oer* joins two things. It is fine: the title names the two ends of the scale.
  - *Graddau a therfynau* joins two things, and the row *Tymheredd* repeats the page title. Both are fine: *Tymheredd* is a word worth learning, and it sits with the degrees.
- **Held content:** the 12 problems are the placeholder groups (Technology, News, Sport). They are not flagged until those groups are released.
- **Tree report:** *dry* has two homes (see section 1). Of the four small sections it flags, the plan fills Pa mor eang (2 to 6) and Gwasgedd (2 to 5). Agor a chau (2) and Cymharu (3) stay small, because their additions are shelved.
- **The proposed titles and lists, checked against the same rules (revised plan):**
  - No title repeats its parent's title exactly.
  - None is over 28 characters.
  - Siblings do not share a title.
  - The one new related tile (The forecast → Time and date) is not to the page itself, and the row stays at one tile.
- **Notes to expect:**
  - *Amser a dyddiad*, *Cyn ac ar ôl* and *Newid a symud* each join two things. All three predict their contents.
  - *Amser a dyddiad* sits in *Amser a lle* and starts with the same word. That is not a repeat, but it breaks the *Pryd / Ble* pair (see section 2).
  - *Berfau eraill* is a catch-all. Revisit it when more verbs arrive.
- **Levels:** the new rows are mostly single words (level 1) and frames (level 3). Run `python build.py --grades` after the change. Do not reorder to show a grade.

## 9. Shelved

Out of scope for now (decided 26 October 2026); the user may bring them back. The words are kept here so nothing is lost, and nothing below goes into the content. The held sections that already exist on `patterns` (Agor a chau, Cyflwyno pwynt, Cymharu) stay as they are, held back, with no new rows.

### Impacts and travel (decided 26 October 2026: shelve Impacts together with Travel)

One future page, *Effeithiau / Impacts*: the sea, damage and travel. It could become a related page for the weather (from The forecast), and other groups (News, Everyday) would want it too. *Effeithio* stays in the plan, in Berfau eraill.

**Y môr / The sea** (3 rows; grow before release: rough sea and swell have not been heard yet)

| Welsh | English | Action |
|---|---|---|
| Tonnau *also* ton | waves | New (11) |
| Llanw uchel *also* llanw | high tide | New (10) |
| Ar hyd y glannau *also* glannau | along the shores | New (11) |

**Difrod / Damage** (6 rows)

| Welsh | English | Action |
|---|---|---|
| Difrod | damage | New (7) |
| Llanast *also* peth llanast | a mess, havoc | New (11) |
| Achosi | to cause | New (7, 11) |
| Coed yn cwympo *also* coed | trees falling | New (7) |
| Toriad yn y cyflenwad trydan *also* cyflenwad, trydan | power cut | New (7) |


**Teithio / Travel** (7 rows)

| Welsh | English | Action |
|---|---|---|
| Teithio | to travel | New (8) |
| Teithwyr | travellers | New (7) |
| Trafferthion *also* drafferthion | troubles, disruption | New (7) |
| Anodd | difficult | New (8) |
| Ar rai ffyrdd *also* ffyrdd, ffordd | on some roads | New (8) |
| Trafnidiaeth gyhoeddus | public transport | New (11) |
| Mentro allan | to venture out | New (11) |

### How it's said: new sentence patterns

**Beth all ddigwydd / What could happen** (new, held; 6 rows)

| Welsh | English | Action |
|---|---|---|
| Mae disgwyl … *also* disgwyl | … is expected | New (10) |
| Bydd mwy o … | there will be more … | New (7) |
| Dylai hi … *also* ddylai | it should … | New (8) |
| Gallen ni weld … *also* gallwn, allwn, weld | we could see … | New (11) |
| Mae'n edrych fel pe bai … | it looks as if … | New (11) |
| Yn cael ei … | being …-ed | New (11) |

**Beth ddigwyddodd / What happened** (new, held; 3 rows; grow before release)

| Welsh | English | Action |
|---|---|---|
| Roedd hi'n … | it was … | New (7) |
| Mae … wedi … *also* 'di | … has … | New (7, 10) |
| Mi welon ni … *also* welon | we saw … | New (10) |

**Cymharu** (held; grows from 3 to 6 rows)

| Welsh | English | Action |
|---|---|---|
| *yn uwch* | higher | Form on *Uwch* (8) |
| Oerach | colder | New (8) |
| Sychach *also* troi'n sychach | drier | New (7, 8) |
| Yn fwy … *also* fwy | more … | New (5, 7) |

### Short forms and On screen

**Ffurfiau byr / Short forms** (new, held; 8 rows). This is the decoder for contractions, written once. The heard form is the text, and the gloss gives the full form.

| Heard | Full form | English | Upload |
|---|---|---|---|
| 'Dan ni | rydyn ni | we are | 10 |
| 'Dach chi | rydych chi | you are | 11 |
| Mae 'na, bydd 'na | mae yna, bydd yna | there is, there will be | 3, 5 |
| Sy'n | sydd yn | which is | 3 |
| 'Di | wedi | has | 7 |
| 'Ma, nesa 'ma | yma | here, this | 5, 7 |
| A'r | a + y | and the | 5 |
| Pethe, dechre, cynta' | pethau, dechrau, cyntaf | southern *-e* for *-au*; dropped *-f* | 5, 6 |

**Ar y sgrin / On screen** (new, held; 8 rows). The captions on the forecast map, seen word for word every night. This answers the open question from upload 9.

| Welsh | English | Upload |
|---|---|---|
| Sych ar y cyfan | dry overall | 7, 8, 9 |
| Sych a braf | dry and fine | 3 |
| Sychach ac yn wyntog | drier and windy | 8 |
| Glaw trwm a gwynt cryf | heavy rain and strong wind | 8 |
| Cyfnodau braf | fine spells | 8 |
| Glaw … cyn cymylu | rain … before clouding over | 3 |
| Rhybudd melyn o wynt | yellow wind warning | 6 |
| Hyrddio 74mya | gusting 74 mph | 7 |

### Opening and closing, introducing a point

**Agor a chau** (grows from 2 to 6 rows)

| Welsh | English | Action |
|---|---|---|
| Y neges *also* neges | the message | New (11) |
| Pwyll piau hi *also* pwyll bia hi | take care (caution is best) | New (11); *piau* is the standard spelling, *bia* is how it is said |
| Cymerwch ofal | take care | New (8) |
| Cofiwch … | remember … | New (8); *Cofiwch droi'r clociau awr yn ôl* as the example |

**Cyflwyno pwynt** (7 rows)

| Welsh | English | Action |
|---|---|---|
| Dyna pam | that's why | New (10, 11), next to *Dyna pryd* |
| Dyna faint | that's how much | New (10) |
| Fel hyn | like this | New (10) |
| *Yn ogystal â* | in addition to | Moves to Geiriau cyswllt (still in the plan) |

### Sequence (a later addition to Time and date; in `TODO.md`)

**Trefn / Sequence** (new; 8 rows; for the Time and date page). Order: earlier to later, then beginning, middle and end.

| Welsh | English | Action |
|---|---|---|
| Eisoes | already | New (7) |
| Yn gynharach | earlier | New (7) |
| Yn gyntaf | first | New (3) |
| Wedyn | then | Move from held Geiriau cyswllt |
| Yn nes ymlaen | later on | Move from held Geiriau amser |
| Dechrau *also* dechre, ddechre'r | the start | New (5) |
| Canol | the middle | Move from held Geiriau amser (4, 7) |
| Diwedd | the end | New (8) |

## 10. Upload 12 (S4C, 27 October 2026; 30 photos in two batches)

*Y Dyddiau Nesaf* and *Dros Nos*, with a river-flooding report (Rhuddlan, Dinas Powys, Afon Tywi) and a yellow wind warning until 03:00 on Tuesday. Subtitles and on-screen text. Nothing here is in the content yet. Placement is a suggestion.

### Placed (28 October 2026)

The words below were turned into forecast phrases, heard and lightly trimmed, and added to the content. The tables after this keep the words as collected.

- **Sky:** *Wedi bod yn ddiwrnod cymylog ar y cyfan*, *Haul a chawodydd*, *Haul ac ambell gawod*, *Rhai cyfnodau braf yn hwyrach yn y dydd*, *Sych am gyfnod dros nos*; *Niwlog yn y bore* (Fog and mist); *Mwy sefydlog erbyn dydd Mercher* (How the sky looks).
- **Rain:** *Mae yna risg o law*, *Ambell gawod yn gallu parhau*. A new **Flooding** card (*Llifogydd*): *Perygl o lifogydd* (moved from Rain), *Rhybudd llifogydd*, *Lefelau'r afonydd yn uchel*, *Ar ôl yr holl law 'na*, *Rhai wedi gweld llifogydd yn barod*, *Mae'r rhybuddion yn gallu newid yn gyson*, *Cadw golwg ar wefan Cyfoeth Naturiol Cymru*. Thunder and storms: *Mwy o dywydd garw i ddod*, *Y stormydd wedi clirio'r wlad erbyn hyn*. The rivers heard are flooding phrases: *Rhybudd llifogydd ar Afon Tywi*, *Afon Clwyd yn uchel yn Rhuddlan*.
- **Wind:** *Gwyntoedd yw'r prif beth heno*, *Y gwaetha o'r gwynt dros nos*, *Y gwynt yn hyrddio o gwmpas 40 milltir yr awr*, *Hyrddiad o 65 milltir yr awr yn bosib*, *Yn eang hyd at 50 milltir yr awr*; *Mae yna rybuddion mewn grym* (Warnings), with the form *tan dri o'r gloch bore fory*.
- **Temperature:** *Tymhereddau bach yn is yfory na heddiw*, *Nos yfory yn sychach*; forms *mi fydd hi'n troi'n sychach*, *a'r tymheredd yn 16 gradd ar ei uchaf*.
- **Change and movement, now released:** *Ffrynt yn cludo mwy o law*, *Yr isobariau ar y map yn agosáu*, *Band o law trwm yn symud tua'r dwyrain*, *Yn clirio ar y cyfan ar ôl hanner nos*, *Troi'n sychach ac yn brafiach yn ystod y dydd*; form *gwasgedd uchel yn dechrau rheoli*.
- **How it's said:** a new **Putting the place first** card (*Rhoi'r lle yn gyntaf*) with *Y gorllewin fydd yn gweld y gwaetha*, *Dros nos fydd yn gweld y gwaetha o'r gwynt*, *Y gogledd welodd orau'r heulwen heddiw*, *Gwasgedd uchel sy'n dechrau rheoli*; *Yn eang* (How widespread). In the held cards: *Is*, *Brafiach*, *Yn fwy*, *na* (Comparing); *Erbyn hyn*, *Yn barod*, *I ddod* (Time words); *Er bod*, *Achos* (Linking words); *Yr holl* (How much).
- **Geography:** the lists of towns and countries were removed on 28 October 2026 (no gazetteers). The towns heard on the forecast map (*Llannerch-y-medd*, *Sychdyn*, *Y Bala*, *Llangurig*, *Aberhonddu*, *Hwlffordd*) and *Caerfyrddin*, *Cydweli*, *Dinas Powys*, *Rhuddlan* are a record only. A new **In a place** card (*Yn …*) shows the sound changes after *yn*, with towns inside the phrase. Rivers are named in phrases: *Rhybudd llifogydd ar Afon Tywi*, *Afon Clwyd yn uchel yn Rhuddlan*, and Landscape has *Yn Nyffryn Conwy*, *Yn Nyffryn Clwyd* and *Ar hyd Môr Hafren* (the official Welsh name, JNCC).
- **Still shelved:** *cymerwch ofal*, *teithio* (Impacts and travel); *gwefan* and *manylion* alone (On screen); the units; *fa'ma* (with *Yma*, still held).

### New

| Welsh | English | Suggested home |
|---|---|---|
| Lefelau'r afonydd | river levels | Rain, with a flooding section |
| Afonydd | rivers (plural of *afon*) | with *lefelau* |
| Rhybudd llifogydd | flood warning | The forecast, next to *Rhybudd melyn* (*llifogydd* is already a form, softening to *lifogydd*) |
| Cyfoeth Naturiol Cymru | Natural Resources Wales: where to check flooding data and warnings (confirmed by the user; <https://cyfoethnaturiol.cymru/?lang=en>) | The forecast, next to *Y Swyddfa Dywydd*; one name, with a note on what it is for |
| Ffrynt | front | Pressure |
| Isobariau | isobars | Pressure |
| Agosau | to approach | Change and movement |
| Cludo (mwy o law) | to carry (more rain) | Change and movement |
| Band o law | a band of rain | Rain |
| Y gwaetha (o'r gwynt) | the worst (of the wind) | Wind, with *y gwaethaf* as the dictionary form |
| Prif (*y prif beth*) | main | How it's said |
| Risg o law | a risk of rain | Rain |
| Yn is (*yn is yfory na heddiw*) | lower | Temperature, pairs with *uwch* |
| Brafiach | finer | Sky, pairs with *sychach* |
| Erbyn hyn | by now | Time and date |
| Yn barod | already | Time and date, next to *eisoes* |
| Gwefan | website | On screen (shelved) |
| Manylion | details | On screen (shelved) |
| Cadw golwg ar | to keep an eye on | On screen (shelved) |
| Yn werth (heard *werth*) | worth | On screen (shelved) |
| Holl (*yr holl law 'na*) | all (the) | How it's said |
| Syndod (*does dim syndod*) | surprise (*it is no surprise*) | How it's said, patterns (shelved) |

### Form

| Welsh | English | On the row |
|---|---|---|
| Tymhereddau | temperatures | *Tymheredd* |
| Mi fydd hi | it will be (colloquial *mi*) | next to *Bydd* |
| Yn gyson | steadily, constantly | *Newid*; heard *yn gallu newid yn gyson* |
| Fa'ma | here; standard shorthand for *y fan yma* (confirmed by the user) | *Yma* (5), with *y fan yma* |
| Hyrddiad (o 65mya) | a gust | *Hyrddiadau* |
| Gymylog | cloudy, softened | *Cymylog* (already has the note) |

### Already in the content (Have)

*Heulwen*, *cymylog*, *niwlog*, *sych*, *sychach*, *cawodydd*, *ambell gawod*, *glaw trwm*, *cyfnodau braf*, *hyrddio*, *hyd at*, *o gwmpas*, *am gyfnod*, *erbyn*, *parhau*, *clirio*, *stormydd*, *ar y cyfan*, *dros nos*, *hanner nos*, *nos yfory*, *yfory*, *heno*, *i ddod*, *gwyntoedd*, *gwasgedd uchel*, *rheoli*, *sefydlog* (*yn fwy sefydlog*), *troi'n*, *mewn grym*, *rhybudd melyn*, *tua'r dwyrain*, *symud*, *ar ôl*, *hwyrach*, *gogledd*, *gorllewin*, *tymheredd*, *ar ei uchaf*. The map labels *Isel* and *Uchel* are the pressure words already held.

Heard again, already collected: *cymerwch ofal*, *teithio*, *'dach chi'n* (8, 10).

### Patterns (shelved with the sentence patterns)

- *Y gogledd welodd orau'r heulwen*, *dros nos fydd yn gweld y gwaetha*: the place or time put first, then *fydd yn gweld* (it will see). Welsh puts the emphasis first.
- *Does dim syndod felly fod rhai wedi gweld …*: it is no surprise that some have seen …
- *Er bod y stormydd wedi clirio'r wlad erbyn hyn*: although the storms have cleared the country by now.
- *… yn bosib, ond yn eang hyd at 50mya*: possible, but widely up to 50 mph.
- *Tymhereddau bach yn is yfory na heddiw*: a little lower tomorrow than today (*na* is *nag* before a vowel, noted in 3).

### Places (for the Geography review)

New: *Rhuddlan*, *Dinas Powys*, *Caerfyrddin*, *Cydweli*, *Sychdyn*, *Y Bala*, *Llangurig*, *Llannerch-y-medd*. Noted before: *Aberhonddu* (6), *Hwlffordd* (5), *Caerdydd*. The map also names *Afon Tywi* and *Ardal Cydweli*.

### Units and numbers (for the units page)

- *mya* with ranges and gusts: *40mya*, *45-50mya*, *50-65mya*, *65mya*, *50mya*; *16C ar ei uchaf*. Temperatures on the map are numbers in squares, wind speeds in circles with an arrow.
- *Tan ddydd Mawrth 03:00*: until Tuesday 03:00, a 24-hour time on the caption. *Tan dri o'r gloch bore fory* is how it is said.

### Left out

The presenters' names and the photo credits (*Llun: …*).

### Questions for a fluent speaker

1. *Y gorllewin fydd ym gweld* (16): is *ym* a typo for *yn*?
2. *Werth cadw golwg* (9): is it *Mae'n werth cadw golwg*, with the start dropped on screen?
