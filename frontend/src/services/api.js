import axios from 'axios'

const api = axios.create({
  baseURL: '/api'
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

export const login = (data) => api.post('/auth/login', data)
export const register = (data) => api.post('/auth/register', data)
export const getRisks = (page = 0) => api.get(`/risks?page=${page}`)
export const getRisk = (id) => api.get(`/risks/${id}`)
export const createRisk = (data) => api.post('/risks', data)
export const updateRisk = (id, data) => api.put(`/risks/${id}`, data)
export const deleteRisk = (id) => api.delete(`/risks/${id}`)
export const searchRisks = (q) => api.get(`/risks/search?q=${q}`)
export const getStats = () => api.get('/risks/stats')

export default api