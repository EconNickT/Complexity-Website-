/* ==============================================================
   ONE PLACE that decides what is public.
   Every list, page, tag page, the RSS feed and the sitemap get
   their entries from here — so a draft can never leak through one
   of them by accident.
   ============================================================== */
import { getCollection, type CollectionEntry } from 'astro:content';

export const SITE = {
  name: 'Complexity Insights',
  url: 'https://complexityinsights.com',
  author: 'Nicholas Thomas',
  twitter: '@EconNickT',
  defaultShareImage: '/images/share/default.png',
};

/* Drafts show ONLY when running locally (npm run dev) or on the
   private "preview" branch build. Never on the live site. */
export const SHOW_DRAFTS =
  import.meta.env.DEV || process.env.CF_PAGES_BRANCH === 'preview';

export type Kind = 'writings' | 'projects';
export type Entry = CollectionEntry<'writings'> | CollectionEntry<'projects'>;

/** A piece gets its own page only once it has body text. */
export const hasPage = (e: Entry) =>
  (e.body ?? "").replace(/<!--[\s\S]*?-->/g, "").trim().length > 0;

/** Where a card for this piece should link (or null: listed, not clickable). */
export function hrefFor(e: Entry): string | null {
  if (hasPage(e)) return `/${e.collection}/${e.id}/`;
  if (e.collection === 'writings' && e.data.originalUrl) return e.data.originalUrl;
  return null;
}

const byNewest = (a: Entry, b: Entry) =>
  (b.data.date?.getTime() ?? -Infinity) - (a.data.date?.getTime() ?? -Infinity) ||
  a.data.title.localeCompare(b.data.title);

async function load<K extends Kind>(kind: K) {
  const all = await getCollection(kind, (e) => SHOW_DRAFTS || !e.data.draft);
  for (const e of all) {
    if (hasPage(e) && !e.data.draft && !e.data.date) {
      throw new Error(
        `"${e.data.title}" (src/content/${kind}/${e.id}) has body text and is not a draft, but has no date. Add its publish date, or set draft: true.`,
      );
    }
  }
  return all.sort(byNewest);
}

export const getWritings = () => load('writings');
export const getProjects = () => load('projects');

/* ---------- small formatting helpers ---------- */

const esc = (s: string) =>
  s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

/** "Did the merger *hurt consumers?*" → HTML with the starred phrase in italics. */
export const titleHtml = (t: string) => esc(t).replace(/\*(.+?)\*/g, '<em>$1</em>');
/** Same title as plain text (for browser tabs, feeds, share cards). */
export const titleText = (t: string) => t.replace(/\*(.+?)\*/g, '$1');

export const tagSlug = (t: string) =>
  t.toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

export const formatDate = (d: Date) =>
  d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });

export const isoDate = (d: Date) => d.toISOString().slice(0, 10);

export function readingMinutes(body: string | undefined) {
  const words = (body ?? '').replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 230));
}

/** Every tag in use across writings and projects, with the pieces that carry it. */
export async function getTags() {
  const all: Entry[] = [...(await getWritings()), ...(await getProjects())];
  const map = new Map<string, { name: string; entries: Entry[] }>();
  for (const e of all) {
    for (const t of e.data.tags) {
      const slug = tagSlug(t);
      if (!slug) continue;
      if (!map.has(slug)) map.set(slug, { name: t, entries: [] });
      map.get(slug)!.entries.push(e);
    }
  }
  return [...map.entries()]
    .map(([slug, v]) => ({ slug, name: v.name, entries: v.entries.sort(byNewest) }))
    .sort((a, b) => a.name.localeCompare(b.name));
}
