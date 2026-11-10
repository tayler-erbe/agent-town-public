#!/usr/bin/env python3
"""Rebuild design/ and built/ from the portfolio's canonical pages.

    python tools/build_pages.py <path to a tayler-portfolio checkout>

The portfolio pages (agent-town-system-design.html, agent-city.html) are the source of truth. This script keeps
their hero and sections, swaps the portfolio's nav and footer for this site's, points portfolio links at
taylererbe.com, rewrites image paths to this repo's assets/shots/, and drops the portfolio chat widget.
index.html is hand-written and not touched. Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://taylererbe.com/"
PORTFOLIO_PAGES = ("index", "skyrule", "agent-city", "agent-architecture", "agent-town-system-design")


def nav(prefix: str, current: str) -> str:
    def li(href, label, key, secondary=False):
        cur = ' aria-current="page"' if key == current else ""
        cls = ' class="nav-secondary"' if secondary else ""
        return f'      <li{cls}><a href="{href}"{cur}>{label}</a></li>'
    return "\n".join([
        '  <nav class="site-nav" aria-label="Site">',
        f'    <a href="{prefix or "./"}" class="nav-logo">Agent Town</a>',
        '    <ul class="site-nav-links">',
        li(f"{prefix}design/", "System design", "design"),
        li(f"{prefix}built/", "How it was built", "built"),
        li(f"{SITE}agent-architecture.html", "The agents", "", True),
        li("https://github.com/tayler-erbe/agent-town-public", "GitHub", "", True),
        li(SITE, "Portfolio", ""),
        '    </ul>',
        '  </nav>',
    ])


def footer(prefix: str) -> str:
    return "\n".join([
        '  <footer class="site-footer">',
        '    <div class="site-footer-meta">',
        '      <p>Agent Town &middot; a personal project by Tayler Erbe</p>',
        '    </div>',
        '    <ul class="site-footer-links">',
        f'      <li><a href="{prefix or "./"}">Agent Town</a></li>',
        f'      <li><a href="{prefix}design/">System design</a></li>',
        f'      <li><a href="{prefix}built/">How it was built</a></li>',
        f'      <li><a href="{SITE}">Portfolio</a></li>',
        '      <li><a href="https://github.com/tayler-erbe" target="_blank" rel="noopener">GitHub</a></li>',
        '      <li><a href="https://linkedin.com/in/tayler-erbe-194374141" target="_blank" rel="noopener">LinkedIn</a></li>',
        '    </ul>',
        '  </footer>',
    ])


def head(title: str, desc: str, prefix: str) -> str:
    return "\n".join([
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '  <meta charset="UTF-8" />',
        '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
        f"  <title>{title}</title>",
        f'  <meta name="description" content="{desc}" />',
        f'  <link rel="stylesheet" href="{prefix}assets/site.css" />',
        f'  <link rel="stylesheet" href="{prefix}assets/town.css" />',
        "</head>",
        "<body>",
        "",
    ])


def body_of(html: str) -> str:
    """The page from the hero to the last section, without the portfolio's nav, back link and footer."""
    start = html.index('<div class="hero">')
    end = html.index('<div class="back-section">')
    return "  " + html[start:end].rstrip() + "\n"


def relink(body: str, prefix: str, local: dict[str, str]) -> str:
    for page, target in local.items():
        body = body.replace(f'href="{page}', f'href="{prefix}{target}')
    pages = "|".join(PORTFOLIO_PAGES)
    body = re.sub(rf'href="((?:{pages})\.html[^"]*|resume\.pdf)"', lambda m: f'href="{SITE}{m.group(1)}"', body)
    body = body.replace('src="assets/shots/agent-city/', f'src="{prefix}assets/shots/')
    body = body.replace('href="assets/shots/agent-city/', f'href="{prefix}assets/shots/')
    body = body.replace('src="assets/shots/agent-city-kissaten-dj.jpg"', f'src="{prefix}assets/shots/cafe-dj-wide.jpg"')
    return body


def page(src: Path, out: Path, title: str, desc: str, current: str, local: dict[str, str]) -> None:
    html = src.read_text(encoding="utf-8").replace("\r\n", "\n")
    body = relink(body_of(html), "../", local)
    text = head(title, desc, "../") + nav("../", current) + "\n\n" + body + "\n" + footer("../") + "\n\n</body>\n</html>\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    print("wrote", out.relative_to(ROOT))


def main() -> None:
    portfolio = Path(sys.argv[1])
    local = {"agent-town-system-design.html": "design/", "agent-city.html": "built/"}
    page(portfolio / "agent-town-system-design.html", ROOT / "design" / "index.html",
         "Agent Town &middot; System Design",
         "End-to-end system design of Agent Town: where its data comes from, how one server turns it into a snapshot, "
         "how a command reaches the job queue, the design decisions, and what is measured, live, built and not built.",
         "design", local)
    page(portfolio / "agent-city.html", ROOT / "built" / "index.html",
         "Agent Town &middot; How It Was Built",
         "How Agent Town was built: from a basic 2D town to a pixel city, concept art and a 3D town in the browser, "
         "with the tools, the trial and error, and the progression in pictures.",
         "built", local)


if __name__ == "__main__":
    main()
