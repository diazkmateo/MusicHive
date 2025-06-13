import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar el token de autenticación
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Interceptor para manejar errores
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Servicio de autenticación y usuario
export const userService = {
  login: (credentials) => api.post('/usuario/login', {
    email: credentials.email,
    password: credentials.password
  }).then(response => {
    // Asegurarnos de que la respuesta tenga el formato correcto
    if (response.data && response.data.token && response.data.user) {
      return response;
    }
    throw new Error('Formato de respuesta inválido');
  }),
  register: (userData) => api.post('/usuario', {
    nombre_usuario: userData.username,
    email: userData.email,
    password: userData.password,
    rol_id: 1  // Por defecto, asignamos el rol de usuario normal
  }),
  getProfile: () => api.get('/usuario/perfil'),
  updateProfile: (userData) => api.put('/usuario/perfil', userData),
  logout: () => {
    localStorage.removeItem('token');
    window.location.href = '/login';
  }
};

// Servicio de música
export const musicService = {
  // Álbumes
  getAlbums: () => api.get('/album'),
  getAlbum: (id) => api.get(`/album/${id}`),
  createAlbum: (albumData) => api.post('/album', albumData),
  updateAlbum: (id, albumData) => api.put(`/album/${id}`, albumData),
  deleteAlbum: (id) => api.delete(`/album/${id}`),

  // Canciones
  getSongs: () => api.get('/cancion'),
  getSong: (id) => api.get(`/cancion/${id}`),
  createSong: (songData) => api.post('/cancion', songData),
  updateSong: (id, songData) => api.put(`/cancion/${id}`, songData),
  deleteSong: (id) => api.delete(`/cancion/${id}`),

  // Artistas
  getArtists: () => api.get('/artista'),
  getArtist: (id) => api.get(`/artista/${id}`),
  createArtist: (artistData) => api.post('/artista', artistData),
  updateArtist: (id, artistData) => api.put(`/artista/${id}`, artistData),
  deleteArtist: (id) => api.delete(`/artista/${id}`),

  // Géneros
  getGenres: () => api.get('/genero'),
  getGenre: (id) => api.get(`/genero/${id}`),
  createGenre: (genreData) => api.post('/genero', genreData),
  updateGenre: (id, genreData) => api.put(`/genero/${id}`, genreData),
  deleteGenre: (id) => api.delete(`/genero/${id}`)
};

// Servicio de colecciones
export const collectionService = {
  getCollections: () => api.get('/coleccion'),
  getCollection: (id) => api.get(`/coleccion/${id}`),
  createCollection: (collectionData) => api.post('/coleccion', collectionData),
  updateCollection: (id, collectionData) => api.put(`/coleccion/${id}`, collectionData),
  deleteCollection: (id) => api.delete(`/coleccion/${id}`),
  addSongToCollection: (collectionId, songId) => 
    api.post(`/coleccion_canciones`, { coleccion_id: collectionId, cancion_id: songId }),
  removeSongFromCollection: (collectionId, songId) => 
    api.delete(`/coleccion_canciones/${collectionId}/${songId}`)
};

// Servicios de Reviews y Ratings
export const reviewService = {
  getReviews: () => api.get('/review'),
  getReview: (id) => api.get(`/review/${id}`),
  createReview: (reviewData) => api.post('/review', reviewData),
  updateReview: (id, reviewData) => api.put(`/review/${id}`, reviewData),
  deleteReview: (id) => api.delete(`/review/${id}`),
};

export const ratingService = {
  getRatings: () => api.get('/rating'),
  getRating: (id) => api.get(`/rating/${id}`),
  createRating: (ratingData) => api.post('/rating', ratingData),
  updateRating: (id, ratingData) => api.put(`/rating/${id}`, ratingData),
  deleteRating: (id) => api.delete(`/rating/${id}`),
};

export default api; 