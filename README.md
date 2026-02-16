# VoiceAI | 语音AI助手

An AI assistant built with voice services from Doubao (豆包), designed as a reusable voice component for other applications.

基于豆包语音服务构建的 AI 助手，作为可复用的语音组件用于其他应用程序。

---

## Tech Stack | 技术栈

### Frontend | 前端
- **React 18** - UI framework | UI 框架
- **TypeScript** - Type safety | 类型安全
- **Vite** - Build tool | 构建工具
- **Tailwind CSS** - Styling | 样式
- **Zustand** - State management (sessions, memory) | 状态管理（会话、记忆）

### Backend | 后端
- **Node.js + Express** - API server | API 服务器
- **Socket.IO** - Real-time audio streaming | 实时音频流
- **SQLite/PostgreSQL** - Session and conversation history storage | 会话和对话历史存储

### Integrations | 集成服务
- **Doubao Voice API** - STT (Speech-to-Text) and TTS (Text-to-Speech) | 语音转文字和文字转语音
- **Doubao Chat API** - AI conversation processing | AI 对话处理

---

## Architecture | 架构

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Chat UI      │  │ Voice Input  │  │ Session List │      │
│  │ (Text Mode)  │  │ (Audio Mode) │  │ (History)    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────────────┘      │
│         │                 │                                │
│         └────────┬────────┘                                │
│                  │                                         │
│            ┌─────▼─────┐                                   │
│            │ API Client│                                   │
│            └─────┬─────┘                                   │
└──────────────────┼─────────────────────────────────────────┘
                   │
         ┌─────────▼─────────┐
         │   Backend API     │
         │   (Express +      │
         │    Socket.IO)     │
         └────────┬──────────┘
                  │
     ┌────────────┼────────────┐
     │            │            │
     ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│   DB    │  │ Doubao  │  │ Doubao  │
│(Sessions│  │  Voice  │  │  Chat   │
│ History)│  │   API   │  │   API   │
└─────────┘  └─────────┘  └─────────┘
```

---

## Implementation Plan | 实现方案

### Phase 1: Backend Foundation | 阶段一：后端基础

- [ ] Set up Express server with TypeScript
  [ ] 搭建 TypeScript Express 服务器
- [ ] Implement Doubao Voice API integration (STT/TTS)
  [ ] 实现豆包语音 API 集成（STT/TTS）
- [ ] Implement Doubao Chat API integration
  [ ] 实现豆包对话 API 集成
- [ ] Set up SQLite database for session storage
  [ ] 搭建 SQLite 数据库用于会话存储
- [ ] Create REST API endpoints
  [ ] 创建 REST API 端点

### Phase 2: Real-time Audio Streaming | 阶段二：实时音频流

- [ ] Configure Socket.IO for audio streaming
  [ ] 配置 Socket.IO 用于音频流传输
- [ ] Implement audio input streaming endpoint
  [ ] 实现音频输入流端点
- [ ] Implement audio output streaming endpoint
  [ ] 实现音频输出流端点
- [ ] Handle WebSocket connection lifecycle
  [ ] 处理 WebSocket 连接生命周期

### Phase 3: Frontend UI | 阶段三：前端界面

- [ ] Initialize Vite + React + TypeScript project
  [ ] 初始化 Vite + React + TypeScript 项目
- [ ] Build chat interface with message history
  [ ] 构建带消息历史的聊天界面
- [ ] Implement text input and send functionality
  [ ] 实现文本输入和发送功能
- [ ] Add voice input button and recording UI
  [ ] 添加语音输入按钮和录音界面
- [ ] Add voice output playback
  [ ] 添加语音输出播放
- [ ] Session list and management UI
  [ ] 会话列表和管理界面

### Phase 4: State Management | 阶段四：状态管理

- [ ] Set up Zustand store
  [ ] 搭建 Zustand 状态管理
- [ ] Manage current session state
  [ ] 管理当前会话状态
- [ ] Manage conversation history
  [ ] 管理对话历史
- [ ] Handle recording/playback states
  [ ] 处理录音/播放状态

### Phase 5: Integration & Polish | 阶段五：集成与完善

- [ ] Connect frontend to backend APIs
  [ ] 连接前端与后端 API
- [ ] Implement real-time audio streaming
  [ ] 实现实时音频流
- [ ] Add loading states and error handling
  [ ] 添加加载状态和错误处理
- [ ] Style with Tailwind CSS
  [ ] 使用 Tailwind CSS 样式
- [ ] Test with Doubao APIs
  [ ] 使用豆包 API 测试

---

## Project Structure | 项目结构

```
VoiceAI/
├── backend/
│   ├── src/
│   │   ├── api/           # API routes | API 路由
│   │   ├── services/      # Doubao API services | 豆包 API 服务
│   │   ├── db/            # Database setup | 数据库配置
│   │   └── index.ts       # Server entry | 服务入口
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── components/    # UI components | UI 组件
│   │   ├── store/         # Zustand stores | Zustand 状态管理
│   │   ├── hooks/         # Custom hooks | 自定义钩子
│   │   ├── api/           # API client | API 客户端
│   │   └── App.tsx
│   └── package.json
└── README.md
```

---

## Development | 开发

### Backend | 后端
```bash
cd backend
npm install
npm run dev
```

### Frontend | 前端
```bash
cd frontend
npm install
npm run dev
```

---

## Notes | 说明

This project serves as a reference implementation for integrating voice capabilities into applications using Doubao's SaaS services.

本项目作为参考实现，展示如何使用豆包 SaaS 服务将语音功能集成到应用程序中。
