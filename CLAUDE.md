# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

VoiceAI is a dual-language (English/Chinese) AI assistant that integrates voice capabilities using Doubao (豆包) SaaS services. The project uses Pipecat framework with RTVI (Real-Time Voice Interaction) standard.

VoiceAI 是一个双语（英文/中文）AI 助手，集成语音功能，使用豆包 SaaS 服务。该项目使用 Pipecat 框架和 RTVI（实时语音交互）标准。

## Project Structure

```
VoiceAI/
├── backend/          # Pipecat server (Python)
├── frontend/         # React + TypeScript frontend with RTVI client
├── Doubao_Token.txt  # Doubao API token (keep secret, never commit)
└── README.md         # Bilingual documentation
```

## Tech Stack

### Frontend
- React 18 with TypeScript
- Vite (build tool)
- Tailwind CSS
- @realtime-ai/rtvi-client (RTVI SDK)

### Backend
- Pipecat framework (real-time voice AI)
- Python 3.12+
- RTVI (Real-Time Voice Interaction) protocol
- SQLite (session storage)

### External Services
- Doubao Realtime Voice API (end-to-end voice-to-voice)
- Doubao STT API (speech-to-text)
- Doubao TTS API (text-to-speech)
- Doubao Chat API (LLM)

## Development Commands

### Backend (Pipecat)
```bash
cd backend
pip install -e .
uv sync
python src/server.py        # Start Pipecat server
```

### Frontend
```bash
cd frontend
npm install
npm run dev        # Start Vite dev server
npm run build      # Build for production
```

## Key Architecture Points

1. **Pipecat Framework** | Pipecat 框架
   - Pipeline-based architecture for real-time voice processing
   - RTVIProcessor handles client-server communication
   - Modular services (STT, LLM, TTS) can be easily swapped

2. **RTVI Standard** | RTVI 标准
   - Open standard for real-time voice interaction
   - Defines events and services for client-server communication
   - Supports multiple client platforms (Web, React, iOS, Android, ESP32)

3. **Dual-language Support** | 双语支持
   - All UI text and messages must support both English and Chinese
   - Doubao Realtime Voice API supports both Chinese and English

4. **Session Management** | 会话管理
   - Each conversation session has unique ID and message history
   - Stored in SQLite with timestamp and metadata

5. **API Integration** | API 集成
   - Doubao Realtime Voice: Low-latency voice-to-voice conversations
   - Doubao STT: Speech recognition
   - Doubao TTS: Voice synthesis with emotion and tone prediction
   - Doubao Chat: LLM conversation processing

## Pipecat Pipeline Flow

```
Frontend (RTVI Client)
    ↓ (WebSocket)
RTVIProcessor
    ↓
Transport Input
    ↓
Doubao STT (Speech-to-Text)
    ↓
Doubao LLM (Conversation)
    ↓
Doubao TTS (Text-to-Speech)
    ↓
Transport Output
    ↓
RTVI Observer
    ↓ (Events)
Frontend (Audio Playback)
```

## RTVI Events

Key events to handle:
- `client-ready` - Client connected and ready
- `bot-ready` - Server ready to receive messages
- `user-started-speaking` / `user-stopped-speaking` - User speech state
- `bot-started-speaking` / `bot-stopped-speaking` - Bot speech state
- `user-transcription` / `bot-transcription` - Speech-to-text results
- `error` - Error handling

## Important Notes

- **Never commit** `Doubao_Token.txt` or any API credentials
- Keep README bilingual when updating
- Use `.env` files for API keys, never hardcode credentials
- Pipecat requires Python 3.10+ (3.12+ recommended)
- RTVI enables cross-platform compatibility - design frontend to work with Web, React Native, mobile, and ESP32

## Doubao API References

- [Realtime Voice API](https://www.volcengine.com/docs/6561/1594356)
- [TTS API](https://www.volcengine.com/docs/6561/1257584)
- [STT API](https://www.volcengine.com/docs/6561/1354868)
- [Chat API](https://www.volcengine.com/docs/82379)
