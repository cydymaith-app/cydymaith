# Philosophy

Cydymaith am iaith is a companion for watching along. Keep it open beside the news, the weather, the sport, or a programme on culture, music or poetry, and look up the Welsh as it goes by.

## Technoleg Dda

The founding principle is **Technoleg Dda**, "good technology", after Hywel Dda, whose laws were remembered for their fairness: *technology should serve the person using it, and ask nothing in return*. The promises below are its rules. The full statement, and the test every change must pass, are in [TECHNOLEG-DDA.md](TECHNOLEG-DDA.md).

## Mobile first

The site is a companion held in one hand while something plays: the news, the weather, the sport. People glance at it for the meaning of what was just said, so it is designed for a phone first and widened for bigger screens after.

- **One thumb.** Every control is a large touch target, and the main moves (go in, go back, settings) are within reach. Going in is a tap on a tile. Going back is a button at the top, or a swipe.
- **Quick to find.** Topics are a few large tiles with an icon and a name in both languages, not a long menu. A person should find the word they heard in a few taps.
- **Readable at a glance.** Large type, strong contrast and a choice of colour palettes, including ones for colour blindness. The first language and the second are always shown together.
- **Nothing to wait for.** Pages are small, work offline once installed, and never block on the network.
- **Phone first in the code.** The base styles are for a phone, and wider screens add to them (`min-width`), so a large screen never hides a small one's needs.
- Keyboards, screen readers and wide screens are supported too, but they are never allowed to make the phone harder to use.

## Help where you need it

Part of promise 7 (*People first*) in [TECHNOLEG-DDA.md](TECHNOLEG-DDA.md). A person who meets a control they do not understand should be able to find out right there, in a few seconds, without leaving what they were doing or hunting through a manual.

- **Help sits beside the thing.** Every feature has a short explanation, reached from the feature itself (a question-mark icon that opens it in a small overlay). The same text is also in the help book under About, so there is one source and no copies.
- **Help is asked for, never pushed.** No tours, pop-ups, tips or "did you know". The icons stay hidden until the person turns them on.
- **Short and plain.** What it does, where it is, how to use it by touch and by keyboard, and what it saves on the device. In both languages of the pair.
- **Problems can be reported from the same place.** The same icon that explains a feature can start a report about it, in the person's own mail app. The app sends nothing itself.
- **Every new feature brings its help.** A feature is not finished until its help text exists. The `app-help` skill checks this.

## An unobtrusive interface

Not a promise of its own: it follows from promises 1 to 5 and is stated under promise 4 (*No nagging*) in [TECHNOLEG-DDA.md](TECHNOLEG-DDA.md). The app is something to glance at while something else holds the attention, so it keeps out of the way.

- **The content comes first.** Words and phrases are the page. Controls are small, quiet and in the same place on every screen (the narrow bar at the side).
- **Nothing moves, flashes or interrupts.** No banners, badges, pop-ups, autoplay or prompts to install, rate, share or sign up. Motion is limited to the slide between pages, and goes away when the device asks for reduced motion.
- **Extras stay hidden until wanted.** Edit order, help and reports are switched on by the person and switched off again. The default screen is the plain one.
- **Few things on screen.** A new control has to earn its place. If a feature can live in Settings or behind a button, it does not go on the page.
- **Quiet defaults, loud choices.** The app follows the device's light or dark setting and its reduced-motion setting, without being asked, and keeps the choices a person makes.

## Promises

- **No sign-up and no accounts.** Nobody is ever asked who they are.
- **No tracking.** No analytics, no cookies, no fingerprinting, and no third-party requests that reveal a visit.
- **No ads.**
- **No payments.** Nothing is sold, gated or upsold.
- **No AI.** The app never calls an AI service or a language model, and makes no API calls. This is about what the app does when it runs, not about how it was written. Every translation still has to be checked by hand by a fluent speaker.
- **No addictive features.** No streaks, scores, badges, nudges or notifications. The site never asks the person to come back.
- **Preferences stay on the device.** Theme and direction live in the browser's own storage and are never sent anywhere.
- **Works offline and without scripts where possible.** Pages are static HTML first. Scripts only add conveniences.

## Rules that follow

1. A feature that needs a server, an account or a network call to a third party is out of scope unless it can be redesigned to run without one.
2. A feature that works by bringing people back is out of scope. A feature that helps them while they are here is in scope.
3. Be honest about accuracy. Unreviewed Welsh is marked as such until a fluent speaker has checked it.
4. Vocabulary and phrases, not other people's work. Topics such as music and poetry cover the words people need to follow along, not song lyrics or poems, which are protected by copyright.
5. Keep it small. Plain files, no dependencies, easy for anyone to read, fork and host.
6. Open assets only. Fonts, icons, code and translations must carry a permissive licence or be in the public domain. See [ASSETS.md](ASSETS.md).
7. Phrases and patterns, not gazetteers. The app teaches how Welsh is said, not what places exist. There are no lists of place names: no towns, rivers, mountains, counties or countries kept as rows of names, because a list would have to hold everything to be honest, and that is a gazetteer, not a companion.
   - A place is named inside the phrase it was heard in, where it teaches something: a mutation (*Yng Nghaerfyrddin*, *Yn Nyffryn Conwy*), a pattern (*Ar hyd Môr Hafren*), or forecast use (*Afon Clwyd yn uchel yn Rhuddlan*).
   - The place-name elements (*aber*, *llan*, *glan*, *pen*) are the exception and are needed: they teach how names are built, so a learner can read almost any name on a sign or a forecast map. Their examples name places only to show an element at work.
   - A name seen on a broadcast is a reason to add the phrase around it, never the name on its own.

## Where this bites today

- Fonts are requested from Google Fonts, which tells a third party about every visit. This breaks the no-tracking promise and is a first-priority fix (see `TODO.md`).
- The PWA must not use push notifications.
- The site is hosted on GitHub Pages, which keeps ordinary server logs. The app adds nothing to that, but the promise should say so plainly in the README.
