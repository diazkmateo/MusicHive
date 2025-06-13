import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const musicService = {
  // Artistas
  getArtists: async () => {
    console.log('GET /artistas');
    const response = await axios.get(`${API_URL}/artistas`);
    console.log('Respuesta GET /artistas:', response.data);
    return response.data;
  },

  createArtist: async (artist) => {
    console.log('POST /artistas', artist);
    try {
      const response = await axios.post(`${API_URL}/artistas`, artist);
      console.log('Respuesta POST /artistas:', response.data);
      return response.data;
    } catch (error) {
      console.error('Error en POST /artistas:', error.response?.data || error.message);
      throw error;
    }
  },

  updateArtist: async (id, artist) => {
    console.log(`PUT /artistas/${id}`, artist);
    try {
      const response = await axios.put(`${API_URL}/artistas/${id}`, artist);
      console.log('Respuesta PUT /artistas:', response.data);
      return response.data;
    } catch (error) {
      console.error('Error en PUT /artistas:', error.response?.data || error.message);
      throw error;
    }
  },

  deleteArtist: async (id) => {
    console.log(`DELETE /artistas/${id}`);
    try {
      const response = await axios.delete(`${API_URL}/artistas/${id}`);
      console.log('Respuesta DELETE /artistas:', response.data);
      return response.data;
    } catch (error) {
      console.error('Error en DELETE /artistas:', error.response?.data || error.message);
      throw error;
    }
  },

  // Álbumes
  getAlbums: async () => {
    const response = await axios.get(`${API_URL}/albums`);
    return response.data;
  },

  createAlbum: async (album) => {
    const response = await axios.post(`${API_URL}/albums`, album);
    return response.data;
  },

  updateAlbum: async (id, album) => {
    const response = await axios.put(`${API_URL}/albums/${id}`, album);
    return response.data;
  },

  deleteAlbum: async (id) => {
    const response = await axios.delete(`${API_URL}/albums/${id}`);
    return response.data;
  },

  // Canciones
  getSongs: async () => {
    const response = await axios.get(`${API_URL}/canciones`);
    return response.data;
  },

  createSong: async (song) => {
    const response = await axios.post(`${API_URL}/canciones`, song);
    return response.data;
  },

  updateSong: async (id, song) => {
    const response = await axios.put(`${API_URL}/canciones/${id}`, song);
    return response.data;
  },

  deleteSong: async (id) => {
    const response = await axios.delete(`${API_URL}/canciones/${id}`);
    return response.data;
  },

  // Géneros
  getGenres: async () => {
    const response = await axios.get(`${API_URL}/generos`);
    return response.data;
  },

  createGenre: async (genre) => {
    const response = await axios.post(`${API_URL}/generos`, genre);
    return response.data;
  },

  updateGenre: async (id, genre) => {
    const response = await axios.put(`${API_URL}/generos/${id}`, genre);
    return response.data;
  },

  deleteGenre: async (id) => {
    const response = await axios.delete(`${API_URL}/generos/${id}`);
    return response.data;
  },

  // Colecciones
  getCollections: async () => {
    const response = await axios.get(`${API_URL}/colecciones`);
    return response.data;
  },

  createCollection: async (collection) => {
    const response = await axios.post(`${API_URL}/colecciones`, collection);
    return response.data;
  },

  updateCollection: async (id, collection) => {
    const response = await axios.put(`${API_URL}/colecciones/${id}`, collection);
    return response.data;
  },

  deleteCollection: async (id) => {
    const response = await axios.delete(`${API_URL}/colecciones/${id}`);
    return response.data;
  }
}; 