import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../services/api'

export default function Login() {
  const [form, setForm] = useState({ username: '', password: '' })
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await login(form)
      localStorage.setItem('token', res.data.token)
      navigate('/')
    } catch {
      setError('Invalid username or password')
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h1 className="text-2xl font-bold text-center mb-6" style={{color: '#1B4F8A'}}>
          Tool-107 Risk Heatmap
        </h1>
        {error && <p className="text-red-500 mb-4">{error}</p>}
        <input className="w-full border p-2 mb-4 rounded"
          placeholder="Username"
          value={form.username}
          onChange={e => setForm({...form, username: e.target.value})} />
        <input className="w-full border p-2 mb-4 rounded"
          type="password" placeholder="Password"
          value={form.password}
          onChange={e => setForm({...form, password: e.target.value})} />
        <button onClick={handleSubmit}
          className="w-full text-white p-2 rounded"
          style={{backgroundColor: '#1B4F8A'}}>
          Login
        </button>
      </div>
    </div>
  )
}