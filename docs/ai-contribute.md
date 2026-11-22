# Point your AI at Swapatron

**You do not have to start alone. Hand this project to your AI assistant and let it help you contribute.**

Any AI assistant that can read a web page or a GitHub repository can do this. Chat assistants, coding assistants, and agents all work.

> **Nothing is decided yet.** Your AI should treat every design, rule, and date as a proposal. The project's briefing for AI, [AGENTS.md](../AGENTS.md), says so too.

## The one-line prompt

Copy this, paste it into your AI, and add a sentence about what you like doing:

> Read AGENTS.md at github.com/Fishers-Founders-United/Swapatron5000 and help me contribute. I am good at: ______.

If your AI cannot browse, paste the contents of [AGENTS.md](../AGENTS.md) and [llms.txt](../llms.txt) into the chat first.

## Prompts for each door

Replace the blanks, and keep what is useful.

| Door | Prompt |
|---|---|
| **Ask list** | "Read ASKS.md in the Swapatron5000 repo. I am working on ______. Help me write one specific ask for a part: what, how many, and what I am building. Do not include my address or any personal details." |
| **Drawing** | "Read hardware/designs/WANTED.md. Pick a view that suits me and help me make a simple SVG or a sketch brief, using the example concept as a base. Label every assumption." |
| **UI and UX** | "Read ux/WANTED.md and ux/README.md. Help me design one screen for ______. Make it work on a phone, with big buttons, no login, and plain words a ten year old could read." |
| **Camera** | "Read integrations/camera/README.md. Help me write a short brief on whether the box should have a camera at all, and what the privacy risks and alternatives are." |
| **Inventory** | "Read integrations/inventory/README.md. Help me sketch the simplest possible took and left flow, using a QR code and a form." |
| **Solar and power** | "Read integrations/solar/README.md. Help me start a power budget with every assumption labelled. Remind me that a qualified person must review anything with a battery." |
| **Safety** | "Read integrations/safety/README.md. Help me list what could go wrong with an outdoor box that kids use, and what a sensor or a weekly check could catch." |
| **Security** | "Read integrations/security/README.md. Help me start a simple threat model: who might misuse the box, and how." |
| **Discovery** | "Read integrations/discovery/README.md. Help me sketch how a person, and then a device, could find the box and see what is in it." |
| **Kit wishlist** | "Read bom/KITS.md. I own these parts: ______. Match them to the kit wishlist and help me write a pledge." |
| **Not sure** | "Read docs/start-here.md. Ask me three questions, then suggest the door and the first small step that suits me." |

## What your AI should do

- **Read first, write second.** [AGENTS.md](../AGENTS.md) comes before anything else.
- **Make small things.** A sketch, a paragraph, a list. Not a rewrite of the project.
- **Show you everything before it is posted.** Your AI should never open an issue, a pull request, or a comment for you without showing you the text first.
- **Label assumptions.** No invented prices, part numbers, dates, measurements, or names.
- **Keep it plain.** Short words, short sentences, and no jargon without a translation.

## What you must do

- **Read it and own it.** You are the contributor. Check the facts, and fix what is wrong.
- **Say it was AI-assisted.** Add "AI-assisted" at the top of your issue or pull request. It is not a mark of shame. It helps reviewers know what to double-check.
- **Make sure you can license it.** Everything here is share-alike: CERN-OHL-S-2.0 for hardware, AGPL-3.0-or-later for software, and CC-BY-SA-4.0 for docs and artwork. Do not submit text, code, or images you cannot license this way. See [LICENSE.md](../LICENSE.md).
- **Keep private things private.** Do not paste passwords, keys, addresses, phone numbers, emails, or anything about a child into your AI or into a public issue.
- **Get a qualified human to review** anything about batteries, mains power, structure, locks, or children before it is built. An AI can draft it. It can not sign off on it.

## What AI is good at here, and what it is not

| Good for | Not good for |
|---|---|
| Turning a messy idea into a clear brief | Deciding what the community wants |
| Drafting a first power budget, with the maths shown | Certifying that a battery design is safe |
| Explaining a term in plain English | Knowing what parts are in a drawer in Fishers |
| Checking a doc for confusing words | Replacing a person who has done the job |
| Drawing a rough SVG to react to | Making a structural drawing someone can build from |

If your AI sounds sure about something safety related, check it with a person.

## Share what worked

Found a prompt that works well? Open an [idea](../../../issues/new?template=idea.yml) with the title "Prompt: " and paste it. Good prompts go in this page.
