# UI and UX wanted

**You do not need to code to start. A sketch on paper is a real contribution.**

Pick a screen or a surface, sketch it, and share it. Use the [screen brief template](templates/screen-brief.md) if you want a structure, or just draw.

## Principles to design for

- **Phone first.** Most people will arrive from a QR code on a phone
- **No login to use the box.** Taking and leaving a part must never need an account
- **Five seconds.** A visitor should know what this is in five seconds
- **Plain words.** A ten year old should be able to read it
- **Works with poor signal.** Light pages, large buttons
- **Kind to beginners.** No jargon without a translation. See [Swapatron-speak](../docs/swapatron-speak.md)
- **Everyone can use it.** Big text, good contrast, and no color-only meaning

## What is wanted

| # | Screen or surface | What it does | Status |
|---|---|---|---|
| 1 | QR landing page | What a person sees after scanning the code on the box | A first version exists in `index.html`. Needs testing and polish |
| 2 | Took and left form | Two taps to say what you took or left | Needs owner |
| 3 | "What is in the box" view | A friendly list from the inventory | Needs owner |
| 4 | Wishlist view | A friendly view of what the box needs. Draws on `bom/BOM.csv` | Needs owner |
| 5 | Ask board | Browse open asks, and fill one | Needs owner |
| 6 | Box status page | Is it healthy? When was it last checked? For stewards | Needs owner |
| 7 | Weekly check checklist | The steward's list, on a phone, with big buttons | Needs owner |
| 8 | Sign and bin labels | Print design, pictures and words | Needs owner |
| 9 | Kid mode | A simpler, more playful view, with a parent's help | Needs owner |
| 10 | The Contributors Wall | Make it feel like a celebration | Exists. Needs ideas |
| 11 | This repository's front door | Where did you get lost? | Always open |
| 12 | Map of boxes | Where every Swapatron is, if the network happens | Later |

## How to contribute

- **Sketch it.** Paper is fine. Photograph it and [share it as a brief](../../../issues/new?template=start-a-brief.yml)
- **Wireframe it.** Any tool. Export a PNG or an SVG
- **Build a clickable page.** One self-contained HTML file, with no outside dependencies, in [screens/](screens/README.md)
- **Test one.** Try a screen on a real person who has never seen it, and write down where they got stuck. That is a very valuable contribution

## Rules for builds

- One HTML file per screen, no tracking, no outside fonts or scripts
- Nothing that collects personal data
- Works with no login
- Say if an AI helped
