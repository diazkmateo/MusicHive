import { createContext, useContext, useReducer, useEffect } from 'react';
import { userService, musicService, collectionService } from '../services/api';

const AppContext = createContext();

const initialState = {
  user: null,
  albums: [],
  songs: [],
  artists: [],
  genres: [],
  collections: [],
  loading: false,
  error: null,
};

function appReducer(state, action) {
  switch (action.type) {
    case 'SET_USER':
      return { ...state, user: action.payload };
    case 'SET_ALBUMS':
      return { ...state, albums: action.payload };
    case 'SET_SONGS':
      return { ...state, songs: action.payload };
    case 'SET_ARTISTS':
      return { ...state, artists: action.payload };
    case 'SET_GENRES':
      return { ...state, genres: action.payload };
    case 'SET_COLLECTIONS':
      return { ...state, collections: action.payload };
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    case 'ADD_ALBUM':
      return { ...state, albums: [...state.albums, action.payload] };
    case 'ADD_SONG':
      return { ...state, songs: [...state.songs, action.payload] };
    case 'ADD_ARTIST':
      return { ...state, artists: [...state.artists, action.payload] };
    case 'ADD_GENRE':
      return { ...state, genres: [...state.genres, action.payload] };
    case 'ADD_COLLECTION':
      return { ...state, collections: [...state.collections, action.payload] };
    case 'UPDATE_ALBUM':
      return {
        ...state,
        albums: state.albums.map(album =>
          album.id === action.payload.id ? action.payload : album
        ),
      };
    case 'UPDATE_SONG':
      return {
        ...state,
        songs: state.songs.map(song =>
          song.id === action.payload.id ? action.payload : song
        ),
      };
    case 'UPDATE_ARTIST':
      return {
        ...state,
        artists: state.artists.map(artist =>
          artist.id === action.payload.id ? action.payload : artist
        ),
      };
    case 'UPDATE_GENRE':
      return {
        ...state,
        genres: state.genres.map(genre =>
          genre.id === action.payload.id ? action.payload : genre
        ),
      };
    case 'UPDATE_COLLECTION':
      return {
        ...state,
        collections: state.collections.map(collection =>
          collection.id === action.payload.id ? action.payload : collection
        ),
      };
    case 'DELETE_ALBUM':
      return {
        ...state,
        albums: state.albums.filter(album => album.id !== action.payload),
      };
    case 'DELETE_SONG':
      return {
        ...state,
        songs: state.songs.filter(song => song.id !== action.payload),
      };
    case 'DELETE_ARTIST':
      return {
        ...state,
        artists: state.artists.filter(artist => artist.id !== action.payload),
      };
    case 'DELETE_GENRE':
      return {
        ...state,
        genres: state.genres.filter(genre => genre.id !== action.payload),
      };
    case 'DELETE_COLLECTION':
      return {
        ...state,
        collections: state.collections.filter(collection => collection.id !== action.payload),
      };
    default:
      return state;
  }
}

export function AppProvider({ children }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  // Cargar datos iniciales
  useEffect(() => {
    const loadInitialData = async () => {
      try {
        dispatch({ type: 'SET_LOADING', payload: true });
        
        // Cargar datos solo si el usuario está autenticado
        if (state.user) {
          const [albums, songs, artists, genres, collections] = await Promise.all([
            musicService.getAlbums(),
            musicService.getSongs(),
            musicService.getArtists(),
            musicService.getGenres(),
            collectionService.getCollections(),
          ]);

          dispatch({ type: 'SET_ALBUMS', payload: albums.data });
          dispatch({ type: 'SET_SONGS', payload: songs.data });
          dispatch({ type: 'SET_ARTISTS', payload: artists.data });
          dispatch({ type: 'SET_GENRES', payload: genres.data });
          dispatch({ type: 'SET_COLLECTIONS', payload: collections.data });
        }
      } catch (error) {
        dispatch({ type: 'SET_ERROR', payload: error.message });
      } finally {
        dispatch({ type: 'SET_LOADING', payload: false });
      }
    };

    loadInitialData();
  }, [state.user]);

  const value = {
    ...state,
    setUser: (user) => dispatch({ type: 'SET_USER', payload: user }),
    setError: (error) => dispatch({ type: 'SET_ERROR', payload: error }),
    addAlbum: (album) => dispatch({ type: 'ADD_ALBUM', payload: album }),
    addSong: (song) => dispatch({ type: 'ADD_SONG', payload: song }),
    addArtist: (artist) => dispatch({ type: 'ADD_ARTIST', payload: artist }),
    addGenre: (genre) => dispatch({ type: 'ADD_GENRE', payload: genre }),
    addCollection: (collection) => dispatch({ type: 'ADD_COLLECTION', payload: collection }),
    updateAlbum: (album) => dispatch({ type: 'UPDATE_ALBUM', payload: album }),
    updateSong: (song) => dispatch({ type: 'UPDATE_SONG', payload: song }),
    updateArtist: (artist) => dispatch({ type: 'UPDATE_ARTIST', payload: artist }),
    updateGenre: (genre) => dispatch({ type: 'UPDATE_GENRE', payload: genre }),
    updateCollection: (collection) => dispatch({ type: 'UPDATE_COLLECTION', payload: collection }),
    deleteAlbum: (id) => dispatch({ type: 'DELETE_ALBUM', payload: id }),
    deleteSong: (id) => dispatch({ type: 'DELETE_SONG', payload: id }),
    deleteArtist: (id) => dispatch({ type: 'DELETE_ARTIST', payload: id }),
    deleteGenre: (id) => dispatch({ type: 'DELETE_GENRE', payload: id }),
    deleteCollection: (id) => dispatch({ type: 'DELETE_COLLECTION', payload: id }),
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useApp() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp debe ser usado dentro de un AppProvider');
  }
  return context;
} 