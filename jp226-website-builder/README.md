# JP226 Website Builder

Helps you work out what you want from a website, writes it up as a short brief, then builds the site.

## What it does

1. Asks a few focused questions: purpose, audience, the one thing visitors should do, pages, and feel.
2. Writes a one-page brief and asks you to approve it.
3. Builds a responsive, accessible site (single page or a few pages) in plain HTML and CSS.
4. Checks the site and looks at it on desktop and phone, in light and dark.
5. Gives you a hosted preview page and a zip of the files.

It never invents facts, reviews or prices. Anything it does not know is marked `[NEEDED: ...]` so you can see what is left to supply.

## Install

Add the `.skill` file to Claude as a skill. The optional checks need Python 3 and Chromium with Playwright, which the Claude workspace already has.

## Usage

```
> I need a website for my mobile coffee cart
> help me plan a landing page for a charity 4WD event
> /jp226-website-builder
```

Expect two or three rounds of short questions, then a brief to approve, then the site.

## What it can and cannot build

| It can | It cannot |
|---|---|
| Landing pages, portfolios, small business sites, event pages | Take payments or logins without a connected service |
| Contact links, galleries, FAQ sections, map links | Send email from a form without a form service |
| Light and dark colour schemes, mobile layouts | Run a database or a server |

When a feature needs a service, the skill says so and suggests one.

## Files

- `SKILL.md`: the instructions Claude follows
- `references/`: question bank, brief template, build checklist
- `scripts/check_site.py`: static quality check
- `scripts/screenshot.py`: desktop and phone screenshots

## Troubleshooting

**The questions feel like too many.** Say "use sensible defaults" and it will choose, and list its choices in the brief.

**The form does not send email.** Static pages cannot send email on their own. Use contact links, or connect a form service.

**Screenshots fail.** Playwright or Chromium is missing. The site is still built; only the visual check is skipped.

## Licence

MIT. Use, change and share freely.

Author: JP226Prints
