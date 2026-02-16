# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

VoiceAI is a dual-language (English/Chinese) AI assistant that integrates voice capabilities using Doubao (豆包) SaaS services. The project aims to be a reusable voice component for other applications.

VoiceAI 是一个双语（英文/中文）AI 助手，集成语音功能，使用豆包 SaaS 服务。该项目旨在作为其他应用程序的可复用语音组件。

## Project Structure

```
VoiceAI/
├── backend/          # Node.js + Express backend
├── frontend/         # React + TypeScript frontend
├── Doubao_Token.txt  # Doubao API token (keep secret, never commit)
└── README.md         # Bilingual documentation
```

## Tech Stack

### Frontend
- React 18 with TypeScript
- Vite (build tool)
- Tailwind CSS
- Zustand (state management)

### Backend
- Node.js + Express
- Socket.IO (real-time audio streaming)
- SQLite or PostgreSQL (session storage)

### External Services
- Doubao Voice API (STT/TTS)
- Doubao Chat API

## Development Commands

### Backend
```bash
cd backend
npm install
npm run dev        # Start development server
npm run build      # Build for production
```

### Frontend
```bash
cd frontend
npm install
npm run dev        # Start Vite dev server
npm run build      # Build for production
```

## Key Architecture Points

1. **Dual-language Support** | 双语支持
   - All UI text and messages must support both English and Chinese
   - API responses should handle bilingual content appropriately

2. **Real-time Audio Streaming** | 实时音频流
   - Socket.IO is used for bidirectional audio streaming
   - Frontend records audio chunks and streams to backend
   - Backend processes through Doubao API and streams TTS response back

3. **Session Management** | 会话管理
   - Each conversation session has unique ID and message history
   - Stored in SQLite/PostgreSQL with timestamp and metadata

4. **API Integration** | API 集成
   - Doubao Voice API handles speech-to-text (STT) and text-to-speech (TTS)
   - Doubao Chat API processes conversations with memory

## Important Notes

- **Never commit** `Doubao_Token.txt` or any API credentials
- Keep README bilingual when updating
- The project is designed as a reusable component - aim for clean APIs between frontend and backend
