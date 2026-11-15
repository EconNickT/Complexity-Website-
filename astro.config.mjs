import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Pages that must never be listed in the sitemap, even if they exist.
const SITEMAP_EXCLUDE = ['banking-deserts', 'example-network-analysis'];

export default defineConfig({
  site: 'https://complexityinsights.com',
  trailingSlash: 'always',
  compressHTML: false, // keep hand-written pages byte-for-byte as authored
  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !SITEMAP_EXCLUDE.some((part) => page.includes(part)),
    }),
  ],
  markdown: {
    shikiConfig: { theme: 'vitesse-dark' },
  },
});
