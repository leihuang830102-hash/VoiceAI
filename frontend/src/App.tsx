/**
 * VoiceAI Frontend Entry
 * VoiceAI 前端入口
 */

import { useState, useEffect } from 'react'
import { VoiceClient } from '@realtime-ai/rtvi-client'
import './index.css'

export default function App() {
  const [connected, setConnected] = useState(false)
  const [transcription, setTranscription] = useState('')
  const [llmProvider, setLlmProvider] = useState<'doubao' | 'glm'>('doubao')

  useEffect(() => {
    // Load LLM provider preference from localStorage
    const savedProvider = localStorage.getItem('llm_provider') as 'doubao' | 'glm' || 'doubao'
    if (savedProvider) {
      setLlmProvider(savedProvider)
    }
  }, [])

  const handleConnect = async () => {
    try {
      const voiceClient = new VoiceClient({
        baseUrl: 'http://localhost:8787', // TODO: Update with actual server URL
        enableMic: true,
        callbacks: {
          onConnected: () => setConnected(true),
          onDisconnected: () => {
            setConnected(false)
            setTranscription('Connection lost')
          },
          onUserStartedSpeaking: () => console.log('User started speaking'),
          onUserStoppedSpeaking: () => console.log('User stopped speaking'),
          onBotStartedSpeaking: () => console.log('Bot started speaking'),
          onBotStoppedSpeaking: () => console.log('Bot stopped speaking'),
          onUserTranscription: (text) => setTranscription(text),
          onBotTranscription: (text) => setTranscription(text),
          onError: (error) => console.error('RTVI Error:', error),
        },
      })

      await voiceClient.start()

      // Save LLM preference
      localStorage.setItem('llm_provider', llmProvider)
    } catch (error) {
      console.error('Failed to connect:', error)
      setTranscription(`Error: ${error.message}`)
    }
  }

  const handleDisconnect = () => {
    setConnected(false)
    setTranscription('')
  }

  const handleLlmChange = (provider: 'doubao' | 'glm') => {
    setLlmProvider(provider)
    localStorage.setItem('llm_provider', provider)
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="max-w-4xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-6">VoiceAI | 语音AI助手</h1>

        {/* LLM Selector */}
        <div className="mb-6 p-4 bg-gray-800 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">LLM Provider | LLM 提供商</h2>
          <div className="flex gap-4">
            <button
              className={`px-4 py-2 rounded-md ${
                llmProvider === 'doubao'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-600 text-white hover:bg-blue-500'
              }`}
              onClick={() => handleLlmChange('doubao')}
            >
              豆包 | Doubao
            </button>
            <button
              className={`px-4 py-2 rounded-md ${
                llmProvider === 'glm'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-600 text-white hover:bg-blue-500'
              }`}
              onClick={() => handleLlmChange('glm')}
            >
              智谱 GLM | Zhipu GLM
            </button>
          </div>
        </div>

        {/* Connection Status */}
        <div className="mb-6 p-4 bg-gray-800 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <div className={`w-3 h-3 rounded-full ${
                connected ? 'bg-green-500' : 'bg-gray-500'
              }`}></div>
              <span className="ml-3">
                {connected ? '已连接 | Connected' : '未连接 | Disconnected'}
              </span>
            </div>
            <div className="flex gap-2">
              {!connected ? (
                <button
                  className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
                  onClick={handleConnect}
                >
                  连接 | Connect
                </button>
              ) : (
                <button
                  className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700"
                  onClick={handleDisconnect}
                >
                  断开 | Disconnect
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Transcription Display */}
        <div className="mb-6 p-4 bg-gray-800 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">转录 | Transcription</h2>
          <div className="bg-black text-green-400 p-4 rounded font-mono">
            {transcription || '等待输入... | Waiting for input...'}
          </div>
        </div>

        {/* Instructions */}
        <div className="text-sm text-gray-400">
          <p className="mb-2">
            • 点击 "连接" 开始语音对话<br/>
            • Click "Connect" to start voice conversation
          </p>
          <p>
            • 点击 "断开" 结束连接<br/>
            • Click "Disconnect" to end connection
          </p>
        </div>
      </div>
    </div>
  )
}
