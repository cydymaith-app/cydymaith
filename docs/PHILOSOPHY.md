# Philosophy

Cydymaith am iaith is a companion for watching along. Keep it open beside the news, the weather, the sport, or a programme on culture, music or poetry, and look up the Welsh as it goes by.

## Mobile first

The site is a companion held in one hand while something plays: the news, the weather, the sport. People glance at it for the meaning of what was just said, so it is designed for a phone first and widened for bigger screens after.

- **One thumb.** Every control is a large touch target, and the main moves (go in, go back, settings) are within reach. Going in is a tap on a tile. Going back is a button at the top, or a swipe.
- **Quick to find.** Topics are a few large tiles with an icon and a name in both languages, not a long menu. A person should find the word they heard in a few taps.
- **Readable at a glance.** Large type, strong contrast and a choice of colour palettes, including ones for colour blindness. The first language and the second are always shown together.
- **Nothing to wait for.** Pages are small, work offline once installed, and never block on the network.
- **Phone first in the code.** The base styles are for a phone, and wider screens add to them (`min-width`), so a large screen never hides a small one's needs.
- Keyboards, screen readers and wide screens are supported too, but they are never allowed to make the phone harder to use.

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

## Where this bites today

- Fonts are requested from Google Fonts, which tells a third party about every visit. This breaks the no-tracking promise and is a first-priority fix (see `TODO.md`).
- The PWA must not use push notifications.
- The site is hosted on GitHub Pages, which keeps ordinary server logs. The app adds nothing to that, but the promise should say so plainly in the README.
