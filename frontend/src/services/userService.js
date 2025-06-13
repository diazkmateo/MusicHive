import axios from 'axios';

const API_URL = 'http://localhost:8000';

// Configurar axios para incluir el token en todas las peticiones
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const userService = {
  login: async (credentials) => {
    console.log('Enviando petición de login a:', `${API_URL}/usuario/login`);
    const response = await axios.post(`${API_URL}/usuario/login`, credentials);
    console.log('Respuesta completa del servidor:', response);
    return response.data;
  },

  register: async (userData) => {
    const response = await axios.post(`${API_URL}/usuario`, userData);
    return response.data;
  },

  getProfile: async () => {
    const response = await axios.get(`${API_URL}/usuario/me`);
    return response.data;
  },

  updateProfile: async (userData) => {
    const response = await axios.put(`${API_URL}/usuario/perfil`, userData);
    return response.data;
  },

  changePassword: async (passwordData) => {
    const response = await axios.put(`${API_URL}/usuario/password`, passwordData);
    return response.data;
  }
}; 