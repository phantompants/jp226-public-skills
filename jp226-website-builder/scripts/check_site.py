#!/usr/bin/env python3
"""
Static quality check for a small website (a folder of .html files).

Author: JP226Prints
Version: v1.00

Usage:
    python3 check_site.py <site_dir_or_html_file>

Findings:
    ERROR  must fix before delivery
    WARN   should fix or consciously accept
    INFO   for the user to action (for example placeholders to fill)

Exit codes: 0 no errors, 1 one or more errors.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

MAX_BYTES = 16 * 1024 * 1024
LOREM = re.compile(r"lorem ipsum|dolor sit amet", re.I)
PLACEHOLDER = re.compile(r"\[(?:NEEDED|YOUR|ADD|INSERT)[^\]]*\]", re.I)
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:", "sms:")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.doctype = False
        self.html_lang = None
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.headings = []
        self.imgs_no_alt = 0
        self.imgs = 0
        self.bad_links = 0
        self.external = set()
        self.forms = []
        self.text = []
        self._skip = 0

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype"):
            self.doctype = True

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key.lower()] = a.get("content", "")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings.append(int(tag[1]))
        elif tag == "img":
            self.imgs += 1
            if "alt" not in a:
                self.imgs_no_alt += 1
        elif tag == "a":
            href = (a.get("href") or "").strip()
            if href in ("", "#"):
                self.bad_links += 1
        elif tag == "form":
            self.forms.append(a.get("action", ""))
        elif tag in ("script", "style"):
            self._skip += 1
        for attr in ("src", "href"):
            val = a.get(attr, "")
            if val.startswith(("http://", "https://", "//")) and tag != "a":
                host = re.sub(r"^(?:https?:)?//", "", val).split("/")[0]
                self.external.add(host)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._skip:
            self.text.append(data)


def check_page(path, out):
    raw = path.read_bytes()
    rel = path.name
    if len(raw) > MAX_BYTES:
        out.append(("ERROR", f"{rel}: over 16 MB"))
    text = raw.decode("utf-8", errors="replace")
    p = Page()
    p.feed(text)

    if not p.doctype:
        out.append(("ERROR", f"{rel}: missing <!doctype html>"))
    if not p.html_lang:
        out.append(("ERROR", f"{rel}: <html> has no lang attribute"))
    if not p.title.strip():
        out.append(("ERROR", f"{rel}: missing or empty <title>"))
    if "viewport" not in p.meta:
        out.append(("ERROR", f"{rel}: missing viewport meta tag "
                             "(page will not work on phones)"))
    if not p.meta.get("description", "").strip():
        out.append(("WARN", f"{rel}: missing meta description"))
    if "og:title" not in p.meta:
        out.append(("WARN", f"{rel}: no Open Graph title for sharing"))

    h1 = p.headings.count(1)
    if h1 == 0:
        out.append(("ERROR", f"{rel}: no h1 heading"))
    elif h1 > 1:
        out.append(("WARN", f"{rel}: {h1} h1 headings; use one"))
    prev = 0
    for level in p.headings:
        if prev and level > prev + 1:
            out.append(("WARN", f"{rel}: heading jumps from h{prev} to "
                                f"h{level}"))
            break
        prev = level

    if p.imgs_no_alt:
        out.append(("ERROR", f"{rel}: {p.imgs_no_alt} of {p.imgs} images "
                             "have no alt attribute"))
    if p.bad_links:
        out.append(("WARN", f"{rel}: {p.bad_links} links with empty or "
                            "'#' href"))
    for action in p.forms:
        if not action.strip() or action.strip() == "#":
            out.append(("WARN", f"{rel}: a form has no real action; it "
                                "will not send anything"))
    if p.external:
        out.append(("INFO", f"{rel}: loads from {', '.join(sorted(p.external))}"))

    body_text = " ".join(p.text)
    if LOREM.search(body_text):
        out.append(("ERROR", f"{rel}: contains lorem ipsum"))
    holes = PLACEHOLDER.findall(text)
    if holes:
        uniq = sorted(set(h.strip() for h in holes))
        out.append(("INFO", f"{rel}: {len(holes)} placeholder(s) to fill: "
                            + "; ".join(uniq[:8])
                            + (" ..." if len(uniq) > 8 else "")))
    return p


def check_links(root, pages, out):
    """Check relative links point at files that exist."""
    for path in pages:
        text = path.read_text(encoding="utf-8", errors="replace")
        text = re.sub(r"<!--.*?-->", "", text, flags=re.S)  # ignore comments
        for m in re.finditer(r'(?:href|src)\s*=\s*"([^"]+)"', text):
            ref = m.group(1).strip()
            if (ref.startswith(("#", "http://", "https://", "//"))
                    or ref.lower().startswith(SKIP_SCHEMES)):
                continue
            target = (path.parent / ref.split("#")[0].split("?")[0])
            if ref.split("#")[0] and not target.exists():
                out.append(("ERROR", f"{path.name}: broken link to '{ref}'"))


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    target = Path(sys.argv[1])
    if target.is_file():
        pages, root = [target], target.parent
    elif target.is_dir():
        pages, root = sorted(target.rglob("*.html")), target
    else:
        print(f"ERROR: not found: {target}")
        return 1
    if not pages:
        print("ERROR: no .html files found")
        return 1

    out = []
    for page in pages:
        check_page(page, out)
    check_links(root, pages, out)

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for level, msg in sorted(out, key=lambda x: order[x[0]]):
        print(f"{level:<6} {msg}")
    errs = sum(1 for lvl, _ in out if lvl == "ERROR")
    warns = sum(1 for lvl, _ in out if lvl == "WARN")
    print(f"\nPages: {len(pages)}  Errors: {errs}  Warnings: {warns}")
    print("RESULT: " + ("FAILED" if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
