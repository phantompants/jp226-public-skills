# Build Checklist

Tick every item before delivering.

## Brief

- [ ] The brief was approved, or the assumptions were stated for an unattended run
- [ ] Every fact on the site came from the user
- [ ] Every gap is marked `[NEEDED: ...]` and listed in the reply

## Content

- [ ] One main action, shown in the first screen and again at the end
- [ ] No invented reviews, awards, statistics, staff, prices or addresses
- [ ] Plain English, short sentences, Australian/British spelling
- [ ] No lorem ipsum

## Structure and accessibility

- [ ] `lang` set, `title` and `meta description` present
- [ ] One `h1`, headings in order
- [ ] Alt text on every image
- [ ] Contrast of at least 4.5 to 1 in light and dark
- [ ] Visible keyboard focus
- [ ] Links and buttons say what they do
- [ ] `prefers-reduced-motion` respected

## Layout

- [ ] Works at 390 px wide with no sideways scrolling
- [ ] Looked at the desktop and phone screenshots
- [ ] No overlapping or cut-off text

## Links and features

- [ ] `tel:` and `mailto:` links use the real details
- [ ] No form unless a form service is named in the brief
- [ ] No claim that payments or email sending work without a real service

## Delivery

- [ ] `check_site.py` shows no errors
- [ ] Published as an artifact and sent as a zip with `brief.md`
- [ ] Zip named `[site-name]-site-v[version].zip`
