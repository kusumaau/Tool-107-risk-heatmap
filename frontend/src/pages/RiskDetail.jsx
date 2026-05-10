import React, { useEffect, useState } from 'react'
import { getRisk } from '../services/api'
import { useParams, useNavigate } from 'react-router-dom'

export default function RiskDetail() {
  const { id } = useParams()
  const [risk, setRisk] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    getRisk(id).then(r => setRisk(r.data)).catch(console.error)
  }, [id])

  if (!risk) return <p className="p-8">Loading...</p>

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <button onClick={() => navigate('/risks')}
        className="mb-4 text-blue-600 underline">← Back</button>
      <div className="bg-white rounded shadow p-6">
        <h1 className="text-2xl font-bold mb-4" style={{color: '#1B4F8A'}}>{risk.title}</h1>
        <div className="grid grid-cols-2 gap-4 mb-6">
          <div><span className="font-semibold">Status:</span> {risk.status}</div>
          <div><span className="font-semibold">Category:</span> {risk.category}</div>
          <div><span className="font-semibold">Likelihood:</span> {risk.likelihood}</div>
          <div><span className="font-semibold">Impact:</span> {risk.impact}</div>
          <div><span className="font-semibold">Risk Score:</span> {risk.riskScore}</div>
        </div>
        <div className="mb-4">
          <h2 className="font-bold text-lg mb-2">Description</h2>
          <p className="text-gray-700">{risk.description}</p>
        </div>
        {risk.aiDescription && (
          <div className="mb-4 bg-blue-50 p-4 rounded">
            <h2 className="font-bold text-lg mb-2" style={{color: '#1B4F8A'}}>
              AI Description
            </h2>
            <p className="text-gray-700 whitespace-pre-wrap">{risk.aiDescription}</p>
          </div>
        )}
        {risk.aiRecommendations && (
          <div className="mb-4 bg-green-50 p-4 rounded">
            <h2 className="font-bold text-lg mb-2 text-green-700">
              AI Recommendations
            </h2>
            <p className="text-gray-700 whitespace-pre-wrap">{risk.aiRecommendations}</p>
          </div>
        )}
        {risk.aiReport && (
          <div className="bg-yellow-50 p-4 rounded">
            <h2 className="font-bold text-lg mb-2 text-yellow-700">AI Report</h2>
            <p className="text-gray-700 whitespace-pre-wrap">{risk.aiReport}</p>
          </div>
        )}
      </div>
    </div>
  )
}