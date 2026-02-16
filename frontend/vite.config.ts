import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    '@components': path.resolve(__dirname, './src/components'),
    '@hooks': path.resolve(__dirname, './src/hooks'),
    '@rtvi': path.resolve(__dirname, './node_modules/@realtime-ai/rtvi-client'),
    '@pipecat': path.resolve(__dirname, './node_modules/pipecat-ai'),
    'openai': path.resolve(__dirname, './node_modules/openai'),
    'react': path.resolve(__dirname, './node_modules/react'),
    'react-dom': path.resolve(__dirname, './node_modules/react-dom'),
    'loguru': path.resolve(__dirname, './node_modules/loguru'),
    'aiohttp': path.resolve(__dirname, './node_modules/aiohttp'),
      'python-dotenv': path.resolve(__dirname, './node_modules/python-dotenv'),
    'websockets': path.resolve(__dirname, './node_modules/websockets'),
      'openai': path.resolve(__dirname, './node_modules/openai'),
      'pipecat-ai': path.resolve(__dirname, './node_modules/pipecat-ai'),
      'daily-transport': path.resolve(__dirname, './node_modules/@daily-co/daily-transport'),
      '@pipecat': path.resolve(__dirname, './node_modules/pipecat-ai'),
      '@realtime-ai': path.resolve(__dirname, './node_modules/@realtime-ai/rtvi-client'),
    }
  },
  server: {
    port: 3000,
    host: true,
  },
})
