import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
const backendPath = '../pokemontcg'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/static/vite/',
  server: {
    watch: {
      ignored: []
    }
  },
  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: backendPath + '/core/static/vite/',
    rollupOptions: {
      input: {
        vue_pokemon_detail: './src/apps/pokemon_detail/pokemon_detail.js',
      }
    }
  }
})