# Complexity Insights — website

The site at [complexityinsights.com](https://complexityinsights.com). It is built with
[Astro](https://astro.build) and hosted on Cloudflare Pages. Writings and projects are
plain text files; the list pages, tag pages, RSS feed and sitemap build themselves from them.

## Where things live

| Folder | What it is |
| --- | --- |
| `src/content/writings/` | One file per writing. **This is where articles live.** |
| `src/content/projects/` | One file per project. |
| `src/pages/` | The pages. Home, About and the Projects golf scene are hand-made; the rest build from content. |
| `src/layouts/`, `src/components/`, `src/styles/site.css` | The shared design (v4.2) for article, project and list pages. |
| `public/` | Files served as-is: images, brand marks, favicon, `robots.txt`. Uploaded images go to `public/images/uploads/`. |
| `.pages.yml` | Settings for the writing editor (Pages CMS). |
| `archive/` | Old versions and retired files. Not published. Safe to ignore. |

## How to write and publish

### One-time setup of the editor

1. Go to [app.pagescms.org](https://app.pagescms.org) and choose **Sign in with GitHub**.
2. When asked, **install the Pages CMS GitHub App** on your account. Choose
   **Only select repositories** and pick `Complexity-Website-`.
3. Back in Pages CMS, open the `Complexity-Website-` repository and make sure the branch
   shown at the top is `main`.

You will see **Writings** and **Projects** in the sidebar.

### Writing

1. Open **Writings** (or **Projects**) and press **Add an entry**.
2. Fill in the title, summary, date and tags. Write in the **Body** box — it works like
   Substack's editor: headings, bold, links, quotes, lists, tables, and images (drag one
   in, or use the image button; it is saved into the repo for you).
3. Leave **Draft** switched **on** and press **Save**. Save as often as you like.

Small conventions that the design picks up automatically:

- Wrap one phrase of a title in `*asterisks*` to set it in italics.
- A line of *italics* directly under an image becomes its caption.
- A quote block becomes a pull quote.

### Previewing

- The editor shows your formatting as you write.
- To see a draft in the real site design, run the site on your computer (see below) and
  open the piece there — drafts are visible locally and carry a "Draft" label.

### Publishing

Switch **Draft** off and press **Save**. Cloudflare rebuilds the site and the piece is
live in a minute or two. It then appears on its list page, its tag pages, the RSS feed
and the sitemap with no further steps. To unpublish, switch **Draft** back on.

### What the fields do

| Field | Notes |
| --- | --- |
| Title, Summary | Required. The summary is also the search and share-card text. |
| Publish date | The original publish date. Required before a piece with text can go live. |
| Tags | Each tag gets a page at `/tags/<tag>/`. |
| Original URL | Writings only. Shows "Originally published at…" at the foot. |
| AI use | A note shown at the foot of the page. Leave empty to hide it. |
| Status, Links | Projects only. Links are Code, Paper and Data. |
| Draft | On = hidden everywhere on the live site. New entries start as drafts. |

**A piece with an empty body has no page of its own.** A writing is then listed under
"In the pipeline" (or, if it has an Original URL, its card links there). A project is
shown as an "On the tee" card. Add body text and it gets a page automatically.

### Pieces with interactive charts

Charts need a little code, so those pieces are `.mdx` files and are edited as code, not
in the editor. Copy any `.md` file in `src/content/`, rename it to end in `.mdx`, and you
can place HTML and scripts directly in the text. Add `class="wide"` to a chart's container
to let it extend past the text column.

## Adding a piece without the editor

Create a file in `src/content/writings/` named after the address you want
(`my-new-essay.md` becomes `/writings/my-new-essay/`):

```markdown
---
title: A plain title with an *italic phrase.*
summary: One or two sentences.
date: 2026-11-15
category: Essay
tags:
  - Econometrics
aiUse: No AI was used in the analysis or writing.
draft: true
---
The text starts here.
```

Projects are the same, in `src/content/projects/`, with `status` and optional `links`
(`code`, `paper`, `data`) instead of `category`.

If a field is misspelled or a date is invalid, the build stops and names the file, so a
mistake cannot reach the live site.

## Running the site on your computer

You need [Node.js](https://nodejs.org) version 22.23.4 or newer.

```bash
npm install
```

```bash
npm run dev
```

Then open the address it prints (usually `http://localhost:4321`). Drafts are visible here.
To produce the exact files Cloudflare will publish, run `npm run build`; they land in `dist/`.

## Cloudflare Pages build settings

| Setting | Value |
| --- | --- |
| Framework preset | Astro |
| Build command | `npm run build` |
| Build output directory | `dist` |
| Root directory | *(leave empty)* |

The Node.js version is set by the `.node-version` file in this repo; no environment
variable is needed. Old addresses that moved are listed in `public/_redirects`.
