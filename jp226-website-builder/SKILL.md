---
name: jp226-website-builder
description: Helps the user work out what they want from a website, writes it up as a short brief, then builds the site. Use when the user wants a website, landing page, portfolio, shop front, event page or small business site, says "build me a website", "I need a site for my business", "help me plan a website", "make a landing page", or is unsure what their site should say or look like. Interviews first, then builds a responsive, accessible site and delivers it as a hosted page plus a downloadable zip. Triggers on "/jp226-website-builder".
compatibility: Claude 3.5+ (Desktop, claude.ai, Claude Code). Python 3 and Chromium (Playwright) are needed for the optional checks.
metadata:
  version: "v1.00"
  author: "JP226Prints"
  created: "2026-10-10"
  updated: "2026-10-10"
  governance: "Personal (JP226Prints) + GitHub"
  status: "Active"
  tags: "website, web-design, brief, landing-page, html, jp226"
---

# JP226 Website Builder

Works out what the user really wants from a website, records it as a one-page brief, then builds the site from that brief. The brief comes first because most disappointing sites come from a vague idea, not poor code.

## The shape of the job

1. **Define**: a short, friendly interview. Output: a one-page brief the user approves.
2. **Build**: a responsive, accessible site made from the brief.
3. **Check**: automatic checks and screenshots on desktop and phone.
4. **Deliver**: a hosted page with a link, plus a zip of the files.
5. **Refine**: change the site from the user's feedback and keep the brief up to date.

Do not skip step 1, even when the request sounds clear. A request like "make me a site for my bakery" still needs the audience, the one thing a visitor should do, and the real content.

## Step 1: Define what they want

Read `references/discovery-questions.md` first. It holds the full question bank, grouped by topic.

### How to ask

- Use AskUserQuestion with up to four questions at a time. Offer 2 to 4 sensible options each. The user can always type their own answer.
- Run at most three rounds. Start with the questions that change the design most: purpose, audience, the one action, and the pages.
- Ask for facts you cannot invent: business name, what they sell or do, contact details, opening hours, prices, links. Never make these up.
- If the user has a logo, photos, a colour, a competitor they like, or an existing site, ask them to attach or link it. Look at what they give you.
- If the user cannot answer a question, offer a default, say what you picked, and move on.

### The five things the brief must settle

| Topic | The question behind it |
|---|---|
| Purpose | What is this site for, in one sentence? |
| Audience | Who visits, and what are they trying to do? |
| Action | What is the one thing a visitor should do? (call, book, buy, enquire, read, sign up) |
| Content | What pages and sections, and what words and images do they actually have? |
| Feel | What should it look and sound like? Any colours, examples, or things to avoid? |

Then cover the practical details: features (contact form, gallery, map, shop link), the domain and hosting situation, and deadlines. Features that need a server (taking payments, user accounts, a database) cannot be built in a static page. Say so plainly and suggest a way: a payment link, an embedded booking service, or a form service. Do not pretend a form will email anyone unless a real form service is connected.

### Write the brief

Fill in `references/brief-template.md`. Keep it to one page. Mark anything missing as `[NEEDED: what]` so nothing is invented. Show the brief to the user in the reply and ask them to approve or correct it. Save it as `brief.md` and include it in the final zip.

If the user is not there to answer (a scheduled or unattended run), take the most reasonable reading of the request, say at the top which assumptions you made, mark gaps as `[NEEDED]`, and carry on.

## Step 2: Build

Build only after the brief is approved, or the assumptions are stated for an unattended run.

### Choose the build type

| Situation | Build |
|---|---|
| One to five short sections, nothing to maintain | One self-contained `index.html` |
| Several real pages (about, services, contact) | A small multi-page site: `index.html`, other `.html` pages, one shared `styles.css`, optional `script.js` |
| Needs a server, logins, or payments | Explain the limit. Build the static front end and name the service to connect |

### Design and quality rules

Before writing any HTML, load the `frontend-design` skill (and `artifact-design` if the site will be published as an artifact) and follow it. Then apply these rules:

1. Mobile first. It must work at 390 px wide with no sideways scrolling.
2. One clear action. The main call to action appears in the first screen and again at the end.
3. Real content only. Use the user's words and facts. Where something is missing, show a clearly marked placeholder, such as `[Your opening hours here]`, never made-up text.
4. No fake social proof. Never invent reviews, testimonials, awards, client logos, statistics or staff. Leave a labelled empty slot or leave the section out.
5. Accessible by default: one `h1`, ordered headings, `lang` set, alt text on every image, text contrast of at least 4.5 to 1, visible keyboard focus, buttons and links that say what they do, and `prefers-reduced-motion` respected.
6. Light and dark: define colours as variables and give the dark scheme its own values. Give `body` an explicit background.
7. Plain English copy. Short sentences. Australian/British spelling unless the user says otherwise.
8. No external dependencies unless needed. Inline the styles. If a library is truly needed, load a pinned version from a trusted CDN. System fonts are fine; use a web font only if the brief asks for a particular look.
9. Basic search and sharing tags: `title`, `meta description`, and Open Graph title and description.
10. Images: use the user's own. For stand-ins, use plain CSS shapes or simple inline SVG, labelled as stand-ins. Do not hotlink random stock photos.
11. Contact: use `mailto:` and `tel:` links with the user's real details. For a form, only build one if a form service is named in the brief; otherwise show the contact links.
12. Keep the page under about 300 KB without user images.

If the site is for something regulated (health, finance, legal, children), add a line to the brief about what claims the user is allowed to make, and keep copy factual and modest.

### Build in stages

Outline the structure first (sections in order, what each one is for), then build the page, then fill the copy. Put the build in `/home/claude/site/[site-name]/`.

## Step 3: Check

Run both helper scripts and fix what they find.

```bash
python3 scripts/check_site.py /home/claude/site/[site-name]
python3 scripts/screenshot.py /home/claude/site/[site-name]/index.html /home/claude/site/shots
```

`check_site.py` finds missing titles, alt text, language, viewport tag, heading problems, empty links, leftover placeholders and lorem ipsum. `screenshot.py` takes full-page pictures at desktop and phone widths and reports any sideways scrolling.

The scripts cannot judge colour contrast or the quality of the copy. Look at the screenshots yourself with Read, in both light and dark, and watch for links that fall back to the browser's default blue on a dark background. Check that the first screen shows what the business is and what to do next, text is readable, nothing overlaps, and the phone view is tidy. Fix what you see, then run the checks again. List any remaining `[NEEDED]` placeholders for the user.

## Step 4: Deliver

1. **Hosted page.** Publish with the Artifact tool. For a single page, publish the HTML. For a multi-page site, publish `index.html` with the other files through `files`. Do not paste the link in the reply; the card carries it.
2. **Downloadable files.** Zip the site folder, including `brief.md`, and send it with SendUserFile as `[site-name]-site-v1.zip`.
3. **Reply** with: one line on what the site is, the list of remaining `[NEEDED]` items, and one suggested next step (for example, "add your real photos").

Mention hosting only if the user asked: the zip can be uploaded to any ordinary web host, and the hosted page is a preview that is private until they share it.

## Step 5: Refine

When the user gives feedback, change the site, rerun the checks, and republish to the same artifact URL. Update `brief.md` if a decision changed. Bump the site version in the zip name (`v1.01`, `v1.02`).

## What this skill will not do

- Build a site that pretends to be another person, business or official body.
- Invent reviews, credentials, prices, addresses or legal claims.
- Collect passwords, card numbers or other sensitive details through a form.
- Promise that a form sends email, or that payments work, without a real service connected.

## Reference files

- `references/discovery-questions.md`: the full question bank.
- `references/brief-template.md`: the one-page brief.
- `references/build-checklist.md`: the pre-delivery checklist.
