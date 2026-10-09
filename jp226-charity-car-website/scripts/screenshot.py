#!/usr/bin/env python3
"""
Take desktop and phone screenshots of a page and report sideways scrolling.

Author: JP226Prints
Version: v1.00

Usage:
    python3 screenshot.py <page.html> <output_dir>

Writes <folder>-<page>-<desktop|phone>-<light|dark>.png into the output folder.
Needs Playwright with Chromium (already installed in the Claude workspace).
Exit codes: 0 fine, 1 sideways scrolling found or the page failed to load.
"""

import sys
from pathlib import Path

VIEWS = [("desktop", 1280, 800), ("phone", 390, 844)]


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    page_path = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2])
    if not page_path.is_file():
        print(f"ERROR: not found: {page_path}")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("ERROR: Playwright is not installed.")
        return 1

    problems = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for scheme in ("light", "dark"):
            for label, width, height in VIEWS:
                ctx = browser.new_context(
                    viewport={"width": width, "height": height},
                    color_scheme=scheme)
                page = ctx.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.goto(page_path.as_uri(), wait_until="load")
                overflow = page.evaluate(
                    "document.documentElement.scrollWidth - "
                    "document.documentElement.clientWidth")
                name = f"{page_path.parent.name}-{page_path.stem}-{label}-{scheme}.png"
                page.screenshot(path=str(out_dir / name), full_page=True)
                status = "ok"
                if overflow > 1:
                    status = f"SIDEWAYS SCROLL by {overflow}px"
                    problems += 1
                if errors:
                    status += f"; script errors: {errors[0][:80]}"
                    problems += 1
                print(f"{name}: {status}")
                ctx.close()
        browser.close()

    print("RESULT: " + ("ISSUES FOUND" if problems else "OK"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
