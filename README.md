# VoiceAI | 语音AI助手

An AI assistant built with voice services from Doubao (豆包) and Zhipu GLM (智谱 GLM), designed as a reusable voice component for other applications.

基于豆包语音服务和智谱 GLM 大模型构建的 AI 助手，作为可复用的语音组件用于其他应用程序。支持切换使用豆包或智谱 GLM 作为后端 LLM。

---

## Tech Stack | 技术栈

### Backend | 后端
- **Pipecat** - Real-time voice AI framework | 实时语音 AI 框架
- **Python 3.12+** - Runtime | 运行环境
- **RTVI Protocol** - Real-Time Voice Interaction standard | 实时语音交互标准
- **SQLite** - Session and conversation history storage | 会话和对话历史存储

### Integrations | 集成服务

#### Voice Services | 语音服务
- **Doubao Realtime Voice API** - End-to-end voice-to-voice model | 端到端语音到语音模型
- **Doubao STT API** - Speech-to-Text | 语音转文字
- **Doubao TTS API** - Text-to-Speech | 文字转语音

#### LLM Services | 大语言模型服务（可切换）
- **Doubao Chat API** - AI conversation processing | 豆包对话处理
- **Zhipu GLM API** (OpenAI Compatible) - AI conversation processing | 智谱 GLM 对话处理（OpenAI 兼容）

#### Note | 说明
Users can switch between Doubao and Zhipu GLM as the backend LLM. Both support OpenAI-compatible API interface.

用户可以切换使用豆包或智谱 GLM 作为后端 LLM。两者都支持 OpenAI 兼容 API 接口。

### Frontend | 前端
- **React 18** - UI framework | UI 框架
- **TypeScript** - Type safety | 类型安全
- **Vite** - Build tool | 构建工具
- **Tailwind CSS** - Styling | 样式
- **@realtime-ai/rtvi-client** - RTVI client SDK | RTVI 客户端 SDK

---

## Architecture | 架构

```
┌─────────────────────────────────────────────────────┐
│                   Frontend Clients                        │
│         Web | React | iOS | Android | ESP32             │
└──────────────────┬──────────────────────────────────────────┘
                   │ (RTVI Protocol)
         ┌─────────▼─────────┐
         │     Pipecat       │
         │  Server Framework  │
         │  (Python + RTVI)  │
         └────────┬──────────┘
                  │
     ┌────────────┼────────────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────────────┐  ┌─────────┐
│ Doubao  │  │    LLM Service   │  │ Doubao  │
│   STT   │  │ (Switchable)    │  │   TTS   │
└─────────┘  │ Doubao / GLM   │  └─────────┘
               └─────────────────┘
```

**LLM Options | LLM 选项:**
- **Doubao Chat API** - 豆包对话 API
- **Zhipu GLM API** - 智谱 GLM (OpenAI Compatible) | 可通过配置切换

---

## Why Pipecat? | 为什么选择 Pipecat?

| Feature | Description | 说明 |
|----------|-------------|------|
| 🎯 **RTVI Standard** | Open standard for real-time voice interaction | 实时语音交互开源标准 |
| 🧩 **Modular** | Composable pipeline architecture | 可组合管道架构 |
| 🌐 **Multi-platform** | Web, React, Mobile, ESP32 clients | Web、移动端、ESP32 客户端 |
| 🔌 **Pluggable** | Easy to integrate Doubao/GLM services | 易于集成豆包/智谱服务 |
| 📊 **Active** | Large community, well-documented | 活跃社区，文档完善 |

---

## Implementation Plan | 实现方案

### Phase 1: Pipecat Server Setup | 阶段一：Pipecat 服务器搭建

- [ ] Install Pipecat framework and dependencies
  [ ] 安装 Pipecat 框架和依赖
- [ ] Set up RTVIProcessor with Doubao STT service
  [ ] 搭建 RTVIProcessor 并集成豆包 STT 服务
- [ ] Set up Doubao TTS service
  [ ] 搭建豆包 TTS 服务
- [ ] Configure pipeline (transport → RTVI → STT → LLM → TTS)
  [ ] 配置管道（传输层 → RTVI → STT → LLM → TTS）
- [ ] Set up SQLite database for session storage
  [ ] 搭建 SQLite 数据库用于会话存储

### Phase 2: Doubao API Integration | 阶段二：豆包 API 集成

- [ ] Implement Doubao Realtime Voice API client
  [ ] 实现豆包实时语音 API 客户端
- [ ] Implement Doubao STT (Speech-to-Text) service
  [ ] 实现豆包 STT 服务
- [ ] Implement Doubao TTS (Text-to-Speech) service
  [ ] 实现豆包 TTS 服务
- [ ] Add authentication with API key
  [ ] 添加 API 密钥认证

### Phase 3: Zhipu GLM Integration | 阶段三：智谱 GLM 集成

- [ ] Implement Zhipu GLM LLM service (OpenAI Compatible)
  [ ] 实现智谱 GLM LLM 服务（OpenAI 兼容）
- [ ] Support GLM models (GLM-4, GLM-4.6v, GLM-4.7)
  [ ] 支持 GLM 模型（GLM-4、GLM-4.6v、GLM-4.7）
- [ ] Implement LLM switch configuration
  [ ] 实现 LLM 切换配置
- [ ] Add API key authentication for GLM
  [ ] 添加 GLM API 密钥认证

### Phase 4: Frontend Setup | 阶段四：前端搭建

- [ ] Initialize Vite + React + TypeScript project
  [ ] 初始化 Vite + React + TypeScript 项目
- [ ] Install @realtime-ai/rtvi-client SDK
  [ ] 安装 RTVI 客户端 SDK
- [ ] Build chat interface with message history
  [ ] 构建带消息历史的聊天界面
- [ ] Implement RTVI VoiceClient connection
  [ ] 实现 RTVI VoiceClient 连接
- [ ] Add LLM selector UI (Doubao/GLM)
  [ ] 添加 LLM 选择器界面（豆包/GLM）
- [ ] Add voice input and output controls
  [ ] 添加语音输入和输出控制
- [ ] Session list and management UI
  [ ] 会话列表和管理界面

### Phase 5: RTVI Integration | 阶段五：RTVI 集成

- [ ] Configure RTVI services (vad, stt, llm, tts)
  [ ] 配置 RTVI 服务（VAD、STT、LLM、TTS）
- [ ] Handle RTVI events (speaking state, transcriptions)
  [ ] 处理 RTVI 事件（说话状态、转录）
- [ ] Implement interruption handling
  [ ] 实现打断处理
- [ ] Add metrics and error handling
  [ ] 添加指标和错误处理

### Phase 6: Testing & Polish | 阶段六：测试与完善

- [ ] Test end-to-end voice conversation with Doubao
  [ ] 测试端到端语音对话（豆包）
- [ ] Test end-to-end voice conversation with GLM
  [ ] 测试端到端语音对话（GLM）
- [ ] Test LLM switching between Doubao and GLM
  [ ] 测试 LLM 切换（豆包 ↔ GLM）
- [ ] Style with Tailwind CSS
  [ ] 使用 Tailwind CSS 样式
- [ ] Add bilingual support (EN/ZH)
  [ ] 添加双语支持（英文/中文）
- [ ] Performance optimization
  [ ] 性能优化

---

## Project Structure | 项目结构

```
VoiceAI/
├── backend/
│   ├── src/
│   │   ├── pipecat/
│   │   │   ├── doubao_stt.py      # Doubao STT service
│   │   │   ├── doubao_tts.py      # Doubao TTS service
│   │   │   ├── glm_llm.py         # Zhipu GLM LLM service (OpenAI Compatible)
│   │   │   └── pipeline.py        # Pipecat pipeline setup
│   │   ├── rtvi/
│   │   │   ├── processor.py       # RTVI processor
│   │   │   └── observer.py        # RTVI observer
│   │   ├── db/
│   │   │   └── sessions.py       # Session storage
│   │   └── server.py            # Server entry
│   ├── requirements.txt
│   └── .env                  # API keys (keep secret)
├── frontend/
│   ├── src/
│   │   ├── components/          # UI components | UI 组件
│   │   ├── hooks/              # Custom hooks | 自定义钩子
│   │   └── App.tsx
│   ├── package.json
│   └── .env                  # API keys (keep secret)
└── README.md
```

---

## Development | 开发

### Backend | 后端
```bash
cd backend
pip install -e .
uv sync
python src/server.py
```

### Frontend | 前端
```bash
cd frontend
npm install
npm run dev
```

---

## Notes | 说明

This project serves as a reference implementation for integrating voice capabilities into applications using Doubao's and Zhipu GLM's SaaS services with Pipecat framework.

本项目作为参考实现，展示如何使用 Pipecat 框架、豆包 SaaS 服务和智谱 GLM 将语音功能集成到应用程序中。支持切换使用豆包或智谱 GLM 作为后端 LLM。

**LLM Switching | LLM 切换:**
- 通过前端配置选择使用 Doubao 或 Zhipu GLM
- 豆包提供端到端实时语音模型（更低延迟）
- 智谱 GLM 提供多种模型选择（GLM-4、GLM-4.6v、GLM-4.7 等）
- 两者都支持 OpenAI 兼容 API，易于切换

---

## API References | API 参考

### Doubao API | 豆包 API

- [豆包端到端实时语音大模型](https://www.volcengine.com/docs/6561/1594356) - Real-time voice-to-voice
- [豆包语音合成大模型](https://www.volcengine.com/docs/6561/1257584) - TTS service
- [豆包语音识别](https://www.volcengine.com/docs/6561/1354868) - STT service

### Zhipu GLM API | 智谱 GLM API

- [智谱 GLM 开放平台](https://open.bigmodel.cn/) - Open platform
- [OpenAI API 兼容](https://docs.bigmodel.cn/cn/guide/develop/openai/introduction) - OpenAI compatible interface
- [HTTP API 调用](https://docs.bigmodel.cn/cn/guide/develop/http/introduction) - HTTP API documentation

**Supported Models | 支持的模型:**
- GLM-4 - 基座大模型
- GLM-4.6v - 视觉模型
- GLM-4.7 - 支持深度思考（reasoning）

---

## Resources | 资源

- [Pipecat Documentation](https://docs.pipecat.ai/) - 实时语音 AI 框架文档
- [RTVI Standard](https://github.com/rtvi-ai) - 实时语音交互标准
- [Pipecat GitHub](https://github.com/pipecat-ai/pipecat) - Pipecat 源码
