#!/usr/bin/env python3
"""
Fundraising checks for a charity car or team website.

Author: JP226Prints
Version: v1.00

Usage:
    python3 check_charity_site.py <site_dir_or_html_file>

Looks at every .html file and reports:

    ERROR  must fix before the site goes live
    WARN   check with the team or the charity
    INFO   things still to fill in

Errors:
  - no donation link on the site
  - a donation link that is still a placeholder, is "#", or is not https
  - form fields that ask for card, bank or account details

Warnings:
  - a dollar amount with no "as at" or "as of" date on the same page
  - no footer notice saying where donations go
  - "100%" or "tax deductible" style claims (needs the charity's confirmation)
  - the word "official" used about the team (may imply endorsement)
  - links using plain http

Exit codes: 0 no errors, 1 one or more errors.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PAYMENT_FIELD = re.compile(
    r"card|cc-|cvv|cvc|expir|bsb|account[-_ ]?(number|no)|iban|routing",
    re.I)
PLACEHOLDER = re.compile(r"\[NEEDED[^\]]*\]", re.I)
MONEY = re.compile(r"\$\s?\d")
DATED = re.compile(r"\bas (at|of)\b", re.I)
NOTICE = re.compile(r"official donation page|donations (are|go) (made )?"
                    r"directly", re.I)
CLAIMS = [
    (re.compile(r"100\s?%", re.I),
     "'100%' claim: confirm with the charity before keeping it"),
    (re.compile(r"tax[- ]?deductible", re.I),
     "'tax deductible' claim: confirm with the charity before keeping it"),
]
OFFICIAL_TEAM = re.compile(r"\bofficial\b(?!\s+donation)", re.I)


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []          # (href, visible text)
        self.inputs = []         # attribute dicts
        self.text = []
        self._href = None
        self._buf = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a":
            self._href = (a.get("href") or "").strip()
            self._buf = []
        elif tag in ("input", "select", "textarea"):
            self.inputs.append(a)
        elif tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((self._href, " ".join(self._buf).strip()))
            self._href = None
        elif tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._skip:
            return
        self.text.append(data)
        if self._href is not None:
            self._buf.append(data.strip())


def is_donation_link(href, text):
    return bool(re.search(r"donat", href + " " + text, re.I))


def check_file(path, out):
    raw = path.read_text(encoding="utf-8", errors="replace")
    p = Page()
    p.feed(raw)
    name = path.name
    body = " ".join(p.text)

    donation = [(h, t) for h, t in p.links if is_donation_link(h, t)]
    if not donation:
        out.append(("ERROR", f"{name}: no donation link found"))
    for href, text in donation:
        label = text or href
        if PLACEHOLDER.search(href) or "NEEDED" in href.upper():
            out.append(("ERROR", f"{name}: donation link '{label}' still "
                                 "has a placeholder address"))
        elif href in ("", "#"):
            out.append(("ERROR", f"{name}: donation link '{label}' goes "
                                 "nowhere"))
        elif not href.lower().startswith("https://"):
            out.append(("ERROR", f"{name}: donation link '{label}' must "
                                 "use https and the charity's official "
                                 "page"))

    for attrs in p.inputs:
        blob = " ".join(str(attrs.get(k, "")) for k in
                        ("name", "id", "autocomplete", "placeholder",
                         "aria-label"))
        if PAYMENT_FIELD.search(blob):
            out.append(("ERROR", f"{name}: form field looks like it asks "
                                 f"for payment details ({blob.strip()[:40]})."
                                 " Remove it. Donations go to the charity's "
                                 "own page."))

    if MONEY.search(body) and not DATED.search(body):
        out.append(("WARN", f"{name}: shows a dollar amount but has no "
                            "'as at' date. Dated figures only."))
    if not NOTICE.search(body):
        out.append(("WARN", f"{name}: no notice saying donations go "
                            "directly to the charity's official donation "
                            "page"))
    for pattern, message in CLAIMS:
        if pattern.search(body):
            out.append(("WARN", f"{name}: {message}"))
    if OFFICIAL_TEAM.search(body):
        out.append(("WARN", f"{name}: uses 'official'. Make sure it does "
                            "not imply the charity endorses the team unless "
                            "that is confirmed"))
    for href, text in p.links:
        if href.lower().startswith("http://"):
            out.append(("WARN", f"{name}: link uses plain http: {href[:60]}"))

    holes = PLACEHOLDER.findall(raw)
    if holes:
        out.append(("INFO", f"{name}: {len(holes)} placeholder(s) still to "
                            "fill in"))


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    target = Path(sys.argv[1])
    if target.is_file():
        pages = [target]
    elif target.is_dir():
        pages = sorted(target.rglob("*.html"))
    else:
        print(f"ERROR: not found: {target}")
        return 1
    if not pages:
        print("ERROR: no .html files found")
        return 1

    out = []
    for page in pages:
        check_file(page, out)

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for level, msg in sorted(out, key=lambda x: order[x[0]]):
        print(f"{level:<6} {msg}")
    errs = sum(1 for lvl, _ in out if lvl == "ERROR")
    warns = sum(1 for lvl, _ in out if lvl == "WARN")
    print(f"\nPages: {len(pages)}  Errors: {errs}  Warnings: {warns}")
    print("RESULT: " + ("NOT READY TO GO LIVE" if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
