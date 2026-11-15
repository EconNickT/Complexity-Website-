/* ==============================================================
   CONTENT SCHEMAS — the rules every writing and project must follow.
   If a file breaks a rule (e.g. a misspelled field, a bad date),
   the build stops and names the file, so mistakes never go live.
   Keep the fields here in sync with .pages.yml (the editor config).
   ============================================================== */
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// The editor saves an untouched optional field as "" or null — treat both as "not set".
const blank = (v: unknown) => (v === '' || v === null ? undefined : v);
const text = z.preprocess(blank, z.string().trim().optional());
const date = z.preprocess(blank, z.coerce.date().optional());
const url = z.preprocess(blank, z.string().url().optional());
const tags = z.preprocess((v) => v ?? [], z.array(z.string().trim().min(1)));

const shared = {
  title: z.string().trim().min(1), // wrap one phrase in *asterisks* for the italic accent
  summary: z.string().trim().min(1),
  tags,
  aiUse: text, // how AI was (or wasn't) used — shown at the foot of the page
  cover: text, // image path, e.g. /images/uploads/chart.png
  coverAlt: text,
  draft: z.boolean().default(true), // new pieces stay hidden until this is switched off
};

const writings = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/writings' }),
  schema: z.object({
    ...shared,
    date, // original publish date — required once the piece has body text
    category: text, // e.g. Working paper, Essay
    originalUrl: url, // where it first appeared (e.g. Substack)
    stat: z
      .preprocess(
        (v: any) => (v && v.value ? v : undefined),
        z.object({ value: z.string(), label: z.string().default('') }).optional(),
      ),
  }),
});

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    ...shared,
    date, // start or publish date — required once the project has body text
    status: z.enum(['In progress', 'Complete', 'Ongoing', 'Paused']).default('In progress'),
    links: z
      .preprocess((v) => v ?? {}, z.object({ code: url, paper: url, data: url }))
      .default({}),
  }),
});

export const collections = { writings, projects };
