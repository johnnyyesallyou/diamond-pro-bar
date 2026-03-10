import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  site: 'https://johnnyyesallyou.github.io',
  base: '/diamond-pro-bar',
  vite: {
    ssr: {
      external: ['svgo']
    }
  }
});
