import React from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login.jsx'
import Dashboard from './pages/Dashboard.jsx'
import RiskList from './pages/RiskList.jsx'
import RiskDetail from './pages/RiskDetail.jsx'

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('token')
  return token ? children : <Navigate to="/login" />
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
        <Route path="/risks" element={<ProtectedRoute><RiskList /></ProtectedRoute>} />
        <Route path="/risks/:id" element={<ProtectedRoute><RiskDetail /></ProtectedRoute>} />
      </Routes>
    </Router>
  )
}

export default App