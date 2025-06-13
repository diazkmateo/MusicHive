import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { musicService } from '../services/musicService';

export default function Collections() {
  const { user } = useAuth();
  const [collections, setCollections] = useState([]);
  const [songs, setSongs] = useState([]);
  const [formData, setFormData] = useState({
    nombre_coleccion: '',
    descripcion: '',
    canciones_seleccionadas: []
  });
  const [editing, setEditing] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (user) {
      loadCollections();
      loadSongs();
    }
  }, [user]);

  const loadCollections = async () => {
    try {
      const data = await musicService.getCollections();
      setCollections(data);
    } catch (err) {
      setError('Error al cargar las colecciones');
    }
  };

  const loadSongs = async () => {
    try {
      const data = await musicService.getSongs();
      setSongs(data);
    } catch (err) {
      setError('Error al cargar las canciones');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSongSelection = (songId) => {
    setFormData(prev => ({
      ...prev,
      canciones_seleccionadas: prev.canciones_seleccionadas.includes(songId)
        ? prev.canciones_seleccionadas.filter(id => id !== songId)
        : [...prev.canciones_seleccionadas, songId]
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      if (editing) {
        await musicService.updateCollection(editing, formData);
      } else {
        await musicService.createCollection(formData);
      }
      await loadCollections();
      resetForm();
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al guardar la colección');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (collection) => {
    setEditing(collection.id_coleccion);
    setFormData({
      nombre_coleccion: collection.nombre_coleccion,
      descripcion: collection.descripcion || '',
      canciones_seleccionadas: collection.canciones_asociadas?.map(c => c.cancion_id) || []
    });
  };

  const handleDelete = async (id) => {
    if (!window.confirm('¿Estás seguro de que quieres eliminar esta colección?')) return;
    
    try {
      await musicService.deleteCollection(id);
      await loadCollections();
    } catch (err) {
      setError('Error al eliminar la colección');
    }
  };

  const resetForm = () => {
    setFormData({
      nombre_coleccion: '',
      descripcion: '',
      canciones_seleccionadas: []
    });
    setEditing(null);
  };

  if (!user) {
    return (
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Gestión de Colecciones</h1>
        <div className="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded">
          Debes iniciar sesión para gestionar tus colecciones.
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Gestión de Colecciones</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editing ? 'Editar Colección' : 'Nueva Colección'}
        </h2>
        
        <div className="grid grid-cols-1 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nombre de la Colección *
            </label>
            <input
              type="text"
              name="nombre_coleccion"
              value={formData.nombre_coleccion}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Descripción
            </label>
            <textarea
              name="descripcion"
              value={formData.descripcion}
              onChange={handleChange}
              rows="4"
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Canciones
            </label>
            <div className="max-h-60 overflow-y-auto border rounded-md p-2">
              {songs.map(song => (
                <div key={song.id_cancion} className="flex items-center space-x-2 py-1">
                  <input
                    type="checkbox"
                    id={`song-${song.id_cancion}`}
                    checked={formData.canciones_seleccionadas.includes(song.id_cancion)}
                    onChange={() => handleSongSelection(song.id_cancion)}
                    className="rounded text-blue-600"
                  />
                  <label htmlFor={`song-${song.id_cancion}`} className="text-sm text-gray-700">
                    {song.nombre_cancion} - {song.artista?.nombre_artista}
                  </label>
                </div>
              ))}
            </div>
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
                Descripción
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Canciones
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Acciones
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {collections.map((collection) => (
              <tr key={collection.id_coleccion}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">
                    {collection.nombre_coleccion}
                  </div>
                </td>
                <td className="px-6 py-4">
                  <div className="text-sm text-gray-500">
                    {collection.descripcion || '-'}
                  </div>
                </td>
                <td className="px-6 py-4">
                  <div className="text-sm text-gray-500">
                    {collection.canciones_asociadas?.length || 0} canciones
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button
                    onClick={() => handleEdit(collection)}
                    className="text-indigo-600 hover:text-indigo-900 mr-4"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(collection.id_coleccion)}
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