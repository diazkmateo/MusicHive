import axios from 'axios';

const API_URL = 'http://localhost:8000';
console.log('API_URL configurada como:', API_URL); // Debug

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
    console.log('Configuración de la petición:', {
        baseURL: config.baseURL,
        url: config.url,
        method: config.method,
        headers: config.headers,
        data: config.data
    }); // Debug
    return config;
});

// Servicios de autenticación
export const authService = {
    login: async (email: string, password: string) => {
        const response = await api.post('/usuario/login', { email, password });
        return response.data;
    },
    register: async (userData: any) => {
        console.log('Intentando registrar usuario con datos:', userData); // Debug
        console.log('URL completa:', API_URL + '/usuario'); // Debug
        const response = await api.post('/usuario', userData);
        return response.data;
    },
    logout: () => {
        localStorage.removeItem('token');
    }
};

// Servicios de música
export const musicService = {
    // Artistas
    getArtists: () => api.get('/artista').then(res => res.data),
    getArtist: (id: number) => api.get(`/artista/${id}`).then(res => res.data),
    createArtist: (artistData: any) => api.post('/artista', artistData).then(res => res.data),
    
    // Álbumes
    getAlbums: () => api.get('/album').then(res => res.data),
    getAlbum: (id: number) => api.get(`/album/${id}`).then(res => res.data),
    createAlbum: (albumData: any) => api.post('/album', albumData).then(res => res.data),
    getArtistAlbums: (artistId: number) => api.get(`/album/artista/${artistId}`).then(res => res.data),
    
    // Canciones
    getSongs: () => api.get('/cancion').then(res => res.data),
    getSong: (id: number) => api.get(`/cancion/${id}`).then(res => res.data),
    createSong: (songData: any) => api.post('/cancion', songData).then(res => res.data),
    getAlbumSongs: (albumId: number) => api.get(`/cancion/album/${albumId}`).then(res => res.data),
    
    // Géneros
    getGenres: () => api.get('/genero').then(res => res.data),
    getGenre: (id: number) => api.get(`/genero/${id}`).then(res => res.data),
    createGenre: (genreData: any) => api.post('/genero', genreData).then(res => res.data),
};

// Servicios de usuario
export const userService = {
    // Usuarios
    login: (credentials: { email: string; password: string }) => 
        api.post('/usuario/login', credentials).then(res => res.data),
    register: (userData: any) => api.post('/usuario', userData).then(res => res.data),
    getProfile: () => api.get('/usuario/perfil').then(res => res.data),
    updateProfile: (userData: any) => api.put('/usuario/perfil', userData).then(res => res.data),
    
    // Colecciones
    getCollections: () => api.get('/coleccion').then(res => res.data),
    createCollection: (collectionData: any) => api.post('/coleccion', collectionData).then(res => res.data),
    addSongToCollection: (collectionId: number, songId: number) => 
        api.post(`/coleccion/${collectionId}/cancion/${songId}`).then(res => res.data),
    
    // Ratings y Reviews
    rateSong: (songId: number, rating: number) => 
        api.post(`/rating/cancion/${songId}`, { rating }).then(res => res.data),
    reviewSong: (songId: number, review: string) => 
        api.post(`/review/cancion/${songId}`, { review }).then(res => res.data),
}; 