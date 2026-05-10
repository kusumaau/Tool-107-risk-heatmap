import React, { useEffect, useState } from 'react'
import { getStats } from '../services/api'
import { useNavigate } from 'react-router-dom'

export default function Dashboard() {
  const [stats, setStats] = useState({})
  const navigate = useNavigate()

  useEffect(() => {
    getStats().then(r => setStats(r.data)).catch(console.error)
  }, [])

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold" style={{color: '#1B4F8A'}}>
          Risk Heatmap Dashboard
        </h1>
        <button onClick={() => { localStorage.removeItem('token'); navigate('/login') }}
          className="bg-red-500 text-white px-4 py-2 rounded">
          Logout
        </button>
      </div>
      <div className="grid grid-cols-4 gap-4 mb-8">
        {[
          { label: 'Total Risks', value: stats.total, color: '#1B4F8A' },
          { label: 'Open', value: stats.open, color: '#e74c3c' },
          { label: 'In Progress', value: stats.inProgress, color: '#f39c12' },
          { label: 'Closed', value: stats.closed, color: '#27ae60' }
        ].map((k, i) => (
          <div key={i} className="bg-white rounded shadow p-6 text-center">
            <p className="text-gray-500">{k.label}</p>
            <p className="text-4xl font-bold" style={{color: k.color}}>{k.value ?? 0}</p>
          </div>
        ))}
      </div>
      <button onClick={() => navigate('/risks')}
        className="text-white px-6 py-3 rounded"
        style={{backgroundColor: '#1B4F8A'}}>
        View All Risks
      </button>
    </div>
  )
}