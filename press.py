#!/usr/bin/env python3
"""
press.py — the Complexity Insights publishing press.

Turns markdown files in /content/writings/ into finished articles in
/writings/, regenerates the writings index, and keeps the artistic
numbering (№ 001, § 01…) consistent — automatically.

Usage:
    python3 press.py            # build everything
    python3 press.py --check    # build and report, exit 1 on warnings

Writing a post:
    1. Create content/writings/my-post-slug.md with front matter (see below)
    2. python3 press.py
    3. git add -A && git commit && git push   (Cloudflare deploys)

Front matter reference (only title is required):
    ---
    title: The equilibrium *assumption.*     # *phrase* renders italic-accent
    subtitle: One-sentence dek shown under the headline.
    description: Meta description for search/social (defaults to subtitle).
    topic: Complexity economics              # kicker, top-left
    category: Essay                          # Essay / Research note / Case study
    date: 2026-06-10
    number: 5                                # optional — auto-assigned by date order
    draft: true                              # skip this file when building
    references:
      - "Arthur, W. B. (2021). *Foundations of complexity economics.* Nature Reviews Physics."
    related:
      - tag: "Portfolio · № 001"
        title: "Banking deserts in America."
        href: /projects/banking-deserts-article.html
        desc: Optional one-line description.
    ---

Body conventions:
    - First paragraph automatically becomes the lead (drop cap).
    - ## headings get § 01, § 02… numbering and appear in the table of contents.
      Use *one italic phrase* per heading for the accent color.
    - > blockquotes render as pull quotes.
    - ![Caption text](/images/writings/slug/fig.png) renders as a numbered
      figure (FIG. 01) with the caption below.
    - ```python fenced code renders as a dark code block with a language tag.
    - ::: takeaway Key insight — some label
      **Bold first sentence becomes the box headline.** Rest is body text.
      :::
    - Raw HTML passes through untouched — for one-off interactive figures.
"""

import argparse
import datetime
import html as html_lib
import os
import re
import sys

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(ROOT, "content", "writings")
OUTPUT_DIR = os.path.join(ROOT, "writings")
TEMPLATE_DIR = os.path.join(ROOT, "templates")
SITE_URL = "https://complexityinsights.com"

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print(f"  ⚠ {msg}")


# ---------------------------------------------------------------- helpers

def slugify(text):
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text or "section"


def inline_md(text):
    """Render inline markdown (for titles/references) without <p> wrapper."""
    out = markdown.markdown(text)
    out = re.sub(r"^<p>|</p>$", "", out.strip())
    return out


def strip_tags(text):
    return html_lib.unescape(re.sub(r"<[^>]+>", "", text))


# ------------------------------------------------------- body processing

def preprocess_takeaways(md_text):
    """::: takeaway Label ... ::: → takeaway box HTML before markdown runs."""

    def repl(m):
        label, body = m.group(1).strip(), m.group(2).strip()
        head_m = re.match(r"\*\*(.+?)\*\*\s*", body)
        if head_m:
            head = head_m.group(1)
            rest = body[head_m.end():].strip()
        else:
            head, rest = "", body
        out = ['<div class="takeaway">']
        out.append(f'  <div class="t-label">{label}</div>')
        if head:
            out.append(f"  <h4>{inline_md(head)}</h4>")
        if rest:
            out.append(f"  <p>{inline_md(rest)}</p>")
        out.append("</div>")
        return "\n".join(out)

    return re.sub(r"^::: *takeaway +(.+?)\n(.*?)\n:::\s*$", repl,
                  md_text, flags=re.S | re.M)


def render_body(md_text, slug):
    """Markdown → article HTML in the house style."""
    md_text = preprocess_takeaways(md_text)

    converter = markdown.Markdown(
        extensions=["fenced_code", "tables", "md_in_html"]
    )
    body = converter.convert(md_text)

    # -- first paragraph becomes the lead (only if it's a plain paragraph)
    body = re.sub(r"^<p>", '<p class="lead">', body, count=1)

    # -- h2: auto id + § numbering + TOC capture
    toc = []
    counter = {"n": 0}

    def h2_repl(m):
        counter["n"] += 1
        text = m.group(1)
        hid = slugify(text)
        toc.append({"id": hid, "text": strip_tags(text)})
        return (f'<h2 id="{hid}" data-num="§ {counter["n"]:02d}">{text}</h2>')

    body = re.sub(r"<h2>(.*?)</h2>", h2_repl, body, flags=re.S)

    # -- blockquote → pull quote (unwrap single inner <p>)
    def bq_repl(m):
        inner = m.group(1).strip()
        inner = re.sub(r"^<p>|</p>$", "", inner)
        return f'<blockquote class="pullquote">{inner}</blockquote>'

    body = re.sub(r"<blockquote>\s*(.*?)\s*</blockquote>", bq_repl,
                  body, flags=re.S)

    # -- fenced code → house code block with language tag
    def code_repl(m):
        lang = (m.group(1) or "").upper() or "CODE"
        return (f'<div class="code-block" data-lang="{lang}">'
                f"<pre>{m.group(2)}</pre></div>")

    body = re.sub(
        r'<pre><code(?: class="language-(\w+)")?>(.*?)</code></pre>',
        code_repl, body, flags=re.S)

    # -- standalone images → numbered figures
    fig = {"n": 0}

    def img_repl(m):
        fig["n"] += 1
        src, alt = m.group("src"), m.group("alt")
        if not alt:
            warn(f"{slug}: figure {src} has no caption (alt text)")
        return (
            '<figure class="demo">\n'
            '  <div class="fig-caption">\n'
            f'    <span><span class="tag">FIG. {fig["n"]:02d}</span></span>\n'
            "  </div>\n"
            f'  <img src="{src}" alt="{html_lib.escape(alt)}" loading="lazy" />\n'
            f"  <figcaption>Figure {fig['n']}. {alt}</figcaption>\n"
            "</figure>"
        )

    body = re.sub(
        r'<p><img alt="(?P<alt>[^"]*)" src="(?P<src>[^"]+)"\s*/?></p>',
        img_repl, body)

    return body, toc


# ------------------------------------------------------------- articles

def load_articles():
    articles = []
    if not os.path.isdir(CONTENT_DIR):
        sys.exit(f"No content directory at {CONTENT_DIR}")
    for fn in sorted(os.listdir(CONTENT_DIR)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(CONTENT_DIR, fn)
        raw = open(path, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            warn(f"{fn}: missing front matter — skipped")
            continue
        meta = yaml.safe_load(m.group(1)) or {}
        if meta.get("draft"):
            print(f"  · {fn}: draft, skipped")
            continue
        if "title" not in meta:
            warn(f"{fn}: no title — skipped")
            continue

        slug = meta.get("slug") or os.path.splitext(fn)[0]
        date = meta.get("date") or datetime.date.today()
        if isinstance(date, str):
            date = datetime.date.fromisoformat(date)

        body_md = m.group(2)
        word_count = len(re.sub(r"<[^>]+>", "", body_md).split())

        articles.append({
            "slug": slug,
            "meta": meta,
            "body_md": body_md,
            "date": date,
            "title_html": inline_md(str(meta["title"])),
            "title_text": strip_tags(inline_md(str(meta["title"]))),
            "subtitle": meta.get("subtitle", ""),
            "description": meta.get("description") or meta.get("subtitle", ""),
            "topic": meta.get("topic", "Research"),
            "category": meta.get("category", "Essay"),
            "read_minutes": max(1, round(word_count / 200)),
        })

    # № numbering: explicit `number:` wins; otherwise chronological order
    articles.sort(key=lambda a: (a["date"], a["slug"]))
    taken = {a["meta"]["number"] for a in articles if "number" in a["meta"]}
    n = 1
    for a in articles:
        if "number" in a["meta"]:
            a["number"] = f"{int(a['meta']['number']):03d}"
        else:
            while n in taken:
                n += 1
            a["number"] = f"{n:03d}"
            taken.add(n)
    return articles


def build():
    articles = load_articles()
    tpl_article = env.get_template("writing.html")
    tpl_index = env.get_template("writings_index.html")
    year = datetime.date.today().year

    for i, a in enumerate(articles):
        content, toc = render_body(a["body_md"], a["slug"])
        out_dir = os.path.join(OUTPUT_DIR, a["slug"])
        os.makedirs(out_dir, exist_ok=True)
        html_out = tpl_article.render(
            content=content,
            toc=toc,
            slug=a["slug"],
            title_html=a["title_html"],
            title_text=a["title_text"],
            subtitle=a["subtitle"],
            description=a["description"],
            topic=a["topic"],
            category=a["category"],
            number=a["number"],
            date_iso=a["date"].isoformat(),
            date_display=a["date"].strftime("%b %d · %Y"),
            read_minutes=a["read_minutes"],
            references=[inline_md(r) for r in a["meta"].get("references", [])],
            related=a["meta"].get("related", []),
            prev=articles[i - 1] if i > 0 else None,
            next=articles[i + 1] if i < len(articles) - 1 else None,
            year=year,
        )
        with open(os.path.join(out_dir, "index.html"), "w",
                  encoding="utf-8") as f:
            f.write(html_out)
        print(f"  ✓ writings/{a['slug']}/  (№ {a['number']}, "
              f"{a['read_minutes']} min)")

    # newest first on the index
    index_html = tpl_index.render(
        articles=list(reversed(articles)), year=year)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w",
              encoding="utf-8") as f:
        f.write(index_html)
    print(f"  ✓ writings/index.html  ({len(articles)} articles)")
    return articles


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the writings section.")
    parser.add_argument("--check", action="store_true",
                        help="exit nonzero if any warnings were raised")
    args = parser.parse_args()

    print("press.py — building writings…")
    build()
    if WARNINGS:
        print(f"\n{len(WARNINGS)} warning(s).")
        if args.check:
            sys.exit(1)
    print("Done.")
