import { useState, useEffect } from 'react';
import { musicService } from '../services/musicService';

export default function Songs() {
  const [songs, setSongs] = useState([]);
  const [albums, setAlbums] = useState([]);
  const [artists, setArtists] = useState([]);
  const [formData, setFormData] = useState({
    nombre_cancion: '',
    duracion_segundos: '',
    numero_pista: '',
    album_id: '',
    artista_id: ''
  });
  const [editing, setEditing] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadSongs();
    loadAlbums();
    loadArtists();
  }, []);

  const loadSongs = async () => {
    try {
      const data = await musicService.getSongs();
      setSongs(data);
    } catch (err) {
      setError('Error al cargar las canciones');
    }
  };

  const loadAlbums = async () => {
    try {
      const data = await musicService.getAlbums();
      setAlbums(data);
    } catch (err) {
      setError('Error al cargar los álbumes');
    }
  };

  const loadArtists = async () => {
    try {
      const data = await musicService.getArtists();
      setArtists(data);
    } catch (err) {
      setError('Error al cargar los artistas');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (editing) {
        await musicService.updateSong(editing, formData);
      } else {
        await musicService.createSong(formData);
      }
      await loadSongs();
      resetForm();
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al guardar la canción');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (song) => {
    setEditing(song.id_cancion);
    setFormData({
      nombre_cancion: song.nombre_cancion,
      duracion_segundos: song.duracion_segundos,
      numero_pista: song.numero_pista,
      album_id: song.album_id,
      artista_id: song.artista_id
    });
  };

  const handleDelete = async (id) => {
    if (!window.confirm('¿Estás seguro de que quieres eliminar esta canción?')) return;
    
    try {
      await musicService.deleteSong(id);
      await loadSongs();
    } catch (err) {
      setError('Error al eliminar la canción');
    }
  };

  const resetForm = () => {
    setFormData({
      nombre_cancion: '',
      duracion_segundos: '',
      numero_pista: '',
      album_id: '',
      artista_id: ''
    });
    setEditing(null);
  };

  const formatDuration = (seconds) => {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Gestión de Canciones</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editing ? 'Editar Canción' : 'Nueva Canción'}
        </h2>
        
        <div className="grid grid-cols-1 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nombre de la Canción *
            </label>
            <input
              type="text"
              name="nombre_cancion"
              value={formData.nombre_cancion}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Duración (segundos) *
            </label>
            <input
              type="number"
              name="duracion_segundos"
              value={formData.duracion_segundos}
              onChange={handleChange}
              required
              min="0"
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Número de Pista *
            </label>
            <input
              type="number"
              name="numero_pista"
              value={formData.numero_pista}
              onChange={handleChange}
              required
              min="1"
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Álbum *
            </label>
            <select
              name="album_id"
              value={formData.album_id}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            >
              <option value="">Seleccionar álbum</option>
              {albums.map(album => (
                <option key={album.id_album} value={album.id_album}>
                  {album.nombre_album}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Artista *
            </label>
            <select
              name="artista_id"
              value={formData.artista_id}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            >
              <option value="">Seleccionar artista</option>
              {artists.map(artista => (
                <option key={artista.id_artista} value={artista.id_artista}>
                  {artista.nombre_artista}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div className="mt-4 flex justify-end space-x-2">
          {editing && (
            <button
              type="button"
              onClick={resetForm}
              className="px-4 py-2 text-gray-600 hover:text-gray-800"
            >
              Cancelar
            </button>
          )}
          <button
            type="submit"
            disabled={loading}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? 'Guardando...' : editing ? 'Actualizar' : 'Crear'}
          </button>
        </div>
      </form>

      <div className="bg-white rounded-lg shadow-md overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Nombre
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Álbum
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Artista
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Duración
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Pista
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Acciones
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {songs.map((song) => (
              <tr key={song.id_cancion}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">
                    {song.nombre_cancion}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {song.album?.nombre_album || '-'}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {song.artista?.nombre_artista || '-'}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {formatDuration(song.duracion_segundos)}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {song.numero_pista}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button
                    onClick={() => handleEdit(song)}
                    className="text-indigo-600 hover:text-indigo-900 mr-4"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(song.id_cancion)}
                    className="text-red-600 hover:text-red-900"
                  >
                    Eliminar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
} 