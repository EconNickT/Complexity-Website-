/* RSS FEED — /rss.xml. Every published writing and project that has a page.
   Drafts are excluded here unconditionally, even on preview builds. */
import rss from '@astrojs/rss';
import { getWritings, getProjects, hasPage, titleText, SITE } from '../lib/content';

export async function GET(context) {
  const entries = [...(await getWritings()), ...(await getProjects())]
    .filter((e) => hasPage(e) && !e.data.draft && e.data.date)
    .sort((a, b) => b.data.date - a.data.date);
  return rss({
    title: SITE.name,
    description:
      'Working papers, essays, and research projects from Complexity Insights — econometrics and complexity economics by Nicholas Thomas.',
    site: context.site,
    items: entries.map((e) => ({
      title: titleText(e.data.title),
      description: e.data.summary,
      pubDate: e.data.date,
      link: `/${e.collection}/${e.id}/`,
      categories: e.data.tags,
    })),
  });
}
