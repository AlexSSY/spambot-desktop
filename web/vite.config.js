import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:5000',  // Proxy API requests to Flask backend
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src') // Define @ as src/
    }
  }
})
