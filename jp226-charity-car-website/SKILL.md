---
name: jp226-charity-car-website
description: Plans and builds a fundraising website for a charity themed car or team, such as a charity rally, drive, 4WD adventure or car show entry. Collects the team story, event details, official donation link, sponsors and photos, then builds a fast, accessible one-page site from a ready template with honest, dated fundraising figures and a link to the charity's own donation page. Use when the user wants a website for a charity car, rally team, fundraising vehicle or sponsored drive, says "build our team website", "make a site for our charity car", "we need a donation page for our rally team", or asks how to go from brief to live website. Triggers on "/jp226-charity-car-website".
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Python 3 and Chromium (Playwright) are needed for the optional checks.
metadata:
  version: "v1.01"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  tags: "charity, fundraising, car, rally, website, html, jp226"
---

# JP226 Charity Car Website

Created by JP226Prints.

Free to use. A good cause, if you choose: please consider supporting Variety - the Children's Charity through our team page: https://www.variety4wdqld.com.au/t/thefastandthefossilized

This note is about this skill only. Do not add it to anything the skill produces for other people.

Takes a charity themed car or team from "we need a website" to a live, trustworthy fundraising page. It follows a seven-step path: collect the material, prepare the images, choose how to publish, build and revise, publish, check the live site, and keep it current.

The method is based on the Car Website guide in JP226Prints Prompt Studio (jp226creativestudio.au).

## What it builds

A one-page site from `assets/template/index.html` with these sections: hero with a donate button, fundraising progress (optional), team story, the car, the event, sponsors, gallery, updates, how to help, and contact. It can grow into a few pages if the team has a lot to say. It is plain HTML and CSS, so the files are portable and can go on any ordinary web host.

## Fundraising rules that always apply

People give money because they trust the page. These rules protect that trust, and they matter more than the design. Read `references/fundraising-integrity.md` for the full list and wording.

1. **Donations go to the charity, not the team.** The donate button links to the charity's own official donation page, supplied by the user. Never guess or invent a link. Never build a payment form, and never ask for card, bank or account details.
2. **Dated figures only.** Show an amount raised only with an "as at" date and only if the user supplied it. No live counters that are not real.
3. **No invented content.** No made-up totals, sponsors, testimonials, endorsements, awards or charity quotes.
4. **Permission first.** List a sponsor only if the user confirms the sponsor agreed. Use the charity's name and logo only as far as the user confirms it is allowed. Do not copy the charity's branding style so the team page looks official.
5. **Say who is who.** The footer says the page is run by the team and that donations are made directly to the charity. Wording such as "independent fundraising team" is used only if the user confirms it is true.
6. **Careful claims.** Statements like "100% of donations go to charity" or "tax deductible" are included only if the user confirms the charity says so. Otherwise leave them out.
7. **People's privacy.** Ask before using photos of identifiable people, especially children. Use only the contact details the user chooses to publish.

If the user asks for something that breaks these rules, explain why in one or two sentences, and offer the honest version.

## Workflow

### Step 1: Collect the material

Run a short interview. Use AskUserQuestion, up to four questions at a time, with 2 to 4 options each. Run no more than three rounds. Ask for facts and files you cannot invent.

| Topic | What to find out |
|---|---|
| Team | Team name, who is in it, the story: why they are doing this |
| Charity | Charity name, the official donation page URL, whether the charity has approved the page or its name and logo |
| Event | Event name, dates, route or location, how people can follow along |
| Car | Make, model, year, the theme or livery, anything special about it |
| Money | Fundraising target, the current amount and its date, or "no figure yet" |
| Sponsors | Who, with confirmation each agreed to be listed, and their logo files |
| Assets | Hero photo, car photos, team photos, logos. Ask the user to attach the real files |
| Contact and social | The public contact link or address and social pages they want shown |
| Look | Livery colours, light or dark, tone (friendly, bold, cheeky), examples they like |
| Publishing | Domain name, where it will be hosted, who updates it and when |

Offer sensible defaults when the user is unsure and say what you picked. If the user cannot answer a charity question, mark it `[NEEDED: ...]` and carry on. Never fill a charity fact from memory.

Write the answers into a one-page brief using `references/charity-brief-template.md`. Show it to the user and ask them to approve or correct it. Save it as `brief.md` and include it in the final zip.

In an unattended run, take the most reasonable reading, say which assumptions you made at the top of your reply, and mark gaps as `[NEEDED]`.

### Step 2: Prepare the images

Read `references/image-prep.md`. Attached files are the only photos you can use, so ask the user to attach the real files. A description of a photo is not a photo. Keep originals untouched, make web copies at a sensible size, give files descriptive names, and write alt text for each image. Recommend the free tools GIMP (cropping), Inkscape (vector logos) and Squoosh (compressing).

If no photos are available yet, build with labelled stand-in blocks and list the missing photos for the user. Do not hotlink stock photos.

### Step 3: Choose the path

Offer the two paths and recommend one:

| Path | Good for | Trade-off |
|---|---|---|
| Plain HTML and CSS (this skill's default) | Portable files, free or cheap hosting, full control | The user updates files, or asks Claude to |
| An AI or drag-and-drop website builder | Editing in a browser, no files to manage | Ongoing cost, less portable |

Read `references/publishing-options.md` for hosting choices. Default to plain HTML and CSS with a hosted preview here and a zip to take away.

### Step 4: Build from the template

1. Copy `assets/template/index.html` to `/home/claude/site/[team-slug]/index.html`. Put web-ready images in `/home/claude/site/[team-slug]/images/`.
2. Before editing the design, load the `frontend-design` skill and follow it, so the page has a real look and not a bland default. Keep the structure, accessibility and integrity features of the template.
3. Replace every `[NEEDED: ...]` with the user's real content, or leave it in place if the content is missing so it shows on the checks.
4. Set the livery colours in the `:root` variables at the top of the stylesheet. Check text contrast stays at 4.5 to 1 or better in light and dark.
5. Delete sections the user does not need (for example Fundraising progress when there is no figure). Do not leave empty sections.
6. Replace image stand-ins with real `<img>` tags, each with alt text, width and height.
7. Keep the donate button in the first screen and again under How to help. Both point to the charity's official page.
8. Keep the footer notice, adjusted to the facts the user confirmed.

Write in plain English, short sentences, Australian spelling. Keep the team's voice, but keep the facts accurate.

### Step 5: Check

Run all three scripts and fix what they find.

```bash
python3 scripts/check_site.py /home/claude/site/[team-slug]
python3 scripts/check_charity_site.py /home/claude/site/[team-slug]
python3 scripts/screenshot.py /home/claude/site/[team-slug]/index.html /home/claude/site/shots
```

`check_site.py` finds general problems: language, title, headings, alt text, broken links, lorem ipsum. `check_charity_site.py` finds fundraising problems: a missing or unfilled donation link, any payment-style form fields, undated money figures, missing footer notice, and claims that need the charity's confirmation. `screenshot.py` shows the page on desktop and phone, in light and dark.

The scripts cannot judge colour contrast or whether the copy is true. Look at the screenshots yourself, in light and dark, and read every number and name on the page against the brief. Fix, then run the checks again. The site is not ready while `check_charity_site.py` shows an error.

### Step 6: Deliver

1. Publish a hosted preview with the Artifact tool. For a multi-file site, publish `index.html` with the images through `files`. Do not paste the link in the reply.
2. Zip the site folder with `brief.md` and send it with SendUserFile as `[team-slug]-site-v1.zip`.
3. In the reply, give one line on what was built, then the list of remaining `[NEEDED]` items, then a reminder that the user must confirm every donation, sponsor and charity statement themselves before going live.

### Step 7: Publish and check the live site

The user publishes the files. Walk them through it from `references/publishing-options.md`. Key points to say plainly:

- A static host cannot run a server-side contact form. Use a public contact link, or a separate form service.
- A domain name is usually a separate yearly cost, even when hosting is free.
- If the files go in a public repository, everything in it is public.
- If the site starts selling things or taking sponsorship payments, check the host's terms first.

After it goes live, ask the user to test every donation, sponsor and social link on their phone, and check the fundraising date.

### Step 8: Keep it current

After each milestone (a sponsor confirmed, the car finished, the event starting, the final total), update the page. Change the dated figure, update the Updates section, and republish to the same preview address. Bump the zip version (`v1.01`, `v1.02`). Keep a backup of the source files. After the event, add a thank-you and the final total with its date.

## What this skill will not do

- Take donations, payments or personal financial details.
- Make a page look like the charity's own official site.
- State amounts, sponsors, endorsements or tax claims the user has not confirmed.
- Use photos the user has not supplied or does not have the right to use.

## Reference files

- `references/charity-brief-template.md`: the one-page brief.
- `references/fundraising-integrity.md`: the full rules, safe wording, and things to avoid.
- `references/image-prep.md`: preparing photos and logos.
- `references/publishing-options.md`: hosting, domains, and keeping the site current.
- `assets/template/index.html`: the starting page.
