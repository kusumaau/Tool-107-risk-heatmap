import React, { useEffect, useState } from 'react'
import { getRisks, deleteRisk, searchRisks } from '../services/api'
import { useNavigate } from 'react-router-dom'

export default function RiskList() {
  const [risks, setRisks] = useState([])
  const [search, setSearch] = useState('')
  const [loading, setLoading] = useState(true)
  const navigate = useNavigate()

  useEffect(() => { fetchRisks() }, [])

  const fetchRisks = () => {
    setLoading(true)
    getRisks().then(r => {
      setRisks(r.data.content || [])
      setLoading(false)
    }).catch(() => setLoading(false))
  }

  const handleSearch = (e) => {
    setSearch(e.target.value)
    if (e.target.value.length > 2) {
      searchRisks(e.target.value).then(r => setRisks(r.data))
    } else if (e.target.value === '') {
      fetchRisks()
    }
  }

  const handleDelete = async (id) => {
    if (window.confirm('Delete this risk?')) {
      await deleteRisk(id)
      fetchRisks()
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold" style={{color: '#1B4F8A'}}>Risk Items</h1>
        <button onClick={() => navigate('/risks/new')}
          className="text-white px-4 py-2 rounded"
          style={{backgroundColor: '#1B4F8A'}}>
          + New Risk
        </button>
      </div>
      <input className="w-full border p-2 mb-4 rounded"
        placeholder="Search risks..."
        value={search} onChange={handleSearch} />
      {loading ? <p>Loading...</p> : risks.length === 0 ? (
        <p className="text-center text-gray-500">No risks found.</p>
      ) : (
        <table className="w-full bg-white rounded shadow">
          <thead style={{backgroundColor: '#1B4F8A', color: 'white'}}>
            <tr>
              {['ID', 'Title', 'Status', 'Category', 'Score', 'Actions'].map(h => (
                <th key={h} className="p-3 text-left">{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {risks.map(r => (
              <tr key={r.id} className="border-b hover:bg-gray-50">
                <td className="p-3">{r.id}</td>
                <td className="p-3">{r.title}</td>
                <td className="p-3">
                  <span className={`px-2 py-1 rounded text-xs ${
                    r.status === 'OPEN' ? 'bg-red-100 text-red-700' :
                    r.status === 'CLOSED' ? 'bg-green-100 text-green-700' :
                    'bg-yellow-100 text-yellow-700'}`}>
                    {r.status}
                  </span>
                </td>
                <td className="p-3">{r.category}</td>
                <td className="p-3">{r.riskScore}</td>
                <td className="p-3 flex gap-2">
                  <button onClick={() => navigate(`/risks/${r.id}`)}
                    className="bg-blue-500 text-white px-3 py-1 rounded text-sm">
                    View
                  </button>
                  <button onClick={() => handleDelete(r.id)}
                    className="bg-red-500 text-white px-3 py-1 rounded text-sm">
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  )
}