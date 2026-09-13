import { useState, useEffect } from 'react'
import { Send, Settings, Plus, Trash2 } from 'lucide-react'
import axios from 'axios'
import './App.css'

interface Message {
  id: string
  content: string
  sender: 'user' | 'assistant'
  timestamp: Date
}

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [selectedModel, setSelectedModel] = useState('ollama')
  const [models, setModels] = useState<any[]>([])

  useEffect(() => {
    fetchAvailableModels()
  }, [])

  const fetchAvailableModels = async () => {
    try {
      const response = await axios.get(`${import.meta.env.REACT_APP_API_URL}/api/v1/models`)
      setModels(response.data.models || [])
    } catch (error) {
      console.error('Error fetching models:', error)
    }
  }

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!inputValue.trim()) return

    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      sender: 'user',
      timestamp: new Date(),
    }

    setMessages([...messages, userMessage])
    setInputValue('')
    setIsLoading(true)

    try {
      const response = await axios.post(
        `${import.meta.env.REACT_APP_API_URL}/api/v1/chat`,
        {
          message: inputValue,
          model: selectedModel,
        }
      )

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: response.data.response,
        sender: 'assistant',
        timestamp: new Date(),
      }

      setMessages((prev) => [...prev, assistantMessage])
    } catch (error) {
      console.error('Error sending message:', error)
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: 'حدث خطأ في الاتصال. يرجى المحاولة لاحقاً.',
        sender: 'assistant',
        timestamp: new Date(),
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const clearMessages = () => {
    setMessages([])
  }

  return (
    <div className="app-container">
      <div className="sidebar">
        <div className="sidebar-header">
          <h1>🤖 AI Assistant</h1>
        </div>
        <button className="new-chat-btn">
          <Plus size={20} /> محادثة جديدة
        </button>
        <div className="chat-history">
          {/* Chat history items will go here */}
        </div>
      </div>

      <div className="main-container">
        <div className="header">
          <div className="model-selector">
            <select
              value={selectedModel}
              onChange={(e) => setSelectedModel(e.target.value)}
              className="model-select"
            >
              {models.map((model) => (
                <option key={model.id} value={model.id}>
                  {model.name}
                </option>
              ))}
            </select>
          </div>
          <button className="settings-btn">
            <Settings size={20} />
          </button>
        </div>

        <div className="messages-container">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <h2>أهلاً وسهلاً!</h2>
              <p>ابدأ محادثة مع مساعد AI الذكي</p>
            </div>
          ) : (
            messages.map((message) => (
              <div key={message.id} className={`message ${message.sender}`}>
                <div className="message-content">{message.content}</div>
                <div className="message-time">
                  {message.timestamp.toLocaleTimeString()}
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message assistant">
              <div className="loading-indicator">جاري الرد...</div>
            </div>
          )}
        </div>

        <div className="input-area">
          <form onSubmit={handleSendMessage} className="input-form">
            <input
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="اكتب رسالتك هنا..."
              className="message-input"
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={isLoading || !inputValue.trim()}
              className="send-btn"
            >
              <Send size={20} />
            </button>
          </form>
          {messages.length > 0 && (
            <button onClick={clearMessages} className="clear-btn">
              <Trash2 size={16} /> مسح المحادثة
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

export default App
