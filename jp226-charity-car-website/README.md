# JP226 Charity Car Website

Created by JP226Prints.

Builds a fundraising website for a charity themed car or team, such as a charity rally, drive, 4WD adventure or car show entry. It is based on the Car Website guide in JP226Prints Prompt Studio.

## What it does

1. Asks for the team story, event details, the charity's official donation page, sponsors and photos.
2. Writes a one-page brief for you to approve.
3. Builds a fast, accessible one-page site from a ready template, in your livery colours, with light and dark modes.
4. Checks the site for general problems and for fundraising problems, then looks at it on desktop and phone.
5. Gives you a hosted preview and a zip of the files, plus a list of anything still to fill in.

## Fundraising rules built in

- The donate button goes to the charity's own official donation page. The site never takes payments or personal financial details.
- Money figures always carry an "as at" date.
- Nothing is invented: no made-up totals, sponsors, quotes or endorsements.
- Sponsors, the charity's logo and people in photos need permission first.
- The footer says who runs the page and where donations go.

The checker will not pass the site while the donation link is missing or still a placeholder.

## Install

Add the `.skill` file to Claude as a skill. The optional checks need Python 3 and Chromium with Playwright, which the Claude workspace already has.

## Usage

```
> build a website for our charity rally team
> we need a fundraising page for our 4WD adventure car
> /jp226-charity-car-website
```

Have these ready if you can: the charity's official donation link, your team story, event dates, the car's details, sponsor names and logos (with their agreement), and photos.

## Files

- `SKILL.md`: the instructions Claude follows
- `assets/template/index.html`: the starting page
- `references/`: brief template, fundraising rules, image preparation, publishing options
- `scripts/check_site.py`: general quality check
- `scripts/check_charity_site.py`: fundraising checks
- `scripts/screenshot.py`: desktop and phone screenshots

## Troubleshooting

**The checker says the donation link is a placeholder.** Paste in the charity's official donation page address and run it again.

**I do not have photos yet.** The site is built with labelled stand-ins, and the missing photos are listed for you.

**The contact form does not send email.** Static sites cannot send email. Use a public contact link, or a separate form service.

**Is this legal advice?** No. Check the charity's guidelines and your state or territory's fundraising rules.

## Licence

MIT. Use, change and share freely.

Author: JP226Prints
