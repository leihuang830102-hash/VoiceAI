/**
 * LLM Selector Component
 * LLM 选择器组件
 */

export interface LLMSelectorProps {
  provider: 'doubao' | 'glm'
  onProviderChange: (provider: 'doubao' | 'glm') => void
}

export function LLMSelector({ provider, onProviderChange }: LLMSelectorProps) {
  return (
    <select
      value={provider}
      onChange={(e) => onProviderChange(e.target.value as 'doubao' | 'glm')}
      className="px-4 py-2 rounded-md border border-gray-300 bg-white focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    >
      <option value="doubao">豆包 | Doubao</option>
      <option value="glm">智谱 GLM | Zhipu GLM</option>
    </select>
  )
}
