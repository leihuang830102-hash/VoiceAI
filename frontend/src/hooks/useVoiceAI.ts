/**
 * VoiceAI Custom Hooks
 * VoiceAI 自定义 Hook
 */

import { useState, useEffect } from 'react'

export interface VoiceAIState {
  connected: boolean
  transcribing: string
  llmProvider: 'doubao' | 'glm'
}

export function useVoiceAI() {
  const [state, setState] = useState<VoiceAIState>({
    connected: false,
    transcribing: '等待输入... | Waiting for input...',
    llmProvider: (localStorage.getItem('llm_provider') as 'doubao' | 'glm') || 'doubao',
  })

  const setConnected = (connected: boolean) => {
    setState(prev => ({ ...prev, connected }))
  }

  const setTranscribing = (transcribing: string) => {
    setState(prev => ({ ...prev, transcribing }))
  }

  const setLlmProvider = (provider: 'doubao' | 'glm') => {
    setState(prev => ({ ...prev, llmProvider: provider }))
    localStorage.setItem('llm_provider', provider)
  }

  return {
    state,
    setConnected,
    setTranscribing,
    setLlmProvider,
  }
}
