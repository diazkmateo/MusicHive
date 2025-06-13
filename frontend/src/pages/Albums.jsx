import { useState, useEffect } from 'react';
import { musicService } from '../services/musicService';

export default function Albums() {
  const [albums, setAlbums] = useState([]);
  const [artists, setArtists] = useState([]);
  const [generos, setGeneros] = useState([]);
  const [formData, setFormData] = useState({
    nombre_album: '',
    fecha_salida_album: '',
    artista_id: '',
    genero_id: ''
  });
  const [editing, setEditing] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadAlbums();
    loadArtists();
    loadGeneros();
  }, []);

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

  const loadGeneros = async () => {
    try {
      const data = await musicService.getGeneros();
      setGeneros(data);
    } catch (err) {
      setError('Error al cargar los géneros');
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
        await musicService.updateAlbum(editing, formData);
      } else {
        await musicService.createAlbum(formData);
      }
      await loadAlbums();
      resetForm();
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al guardar el álbum');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (album) => {
    setEditing(album.id_album);
    setFormData({
      nombre_album: album.nombre_album,
      fecha_salida_album: album.fecha_salida_album,
      artista_id: album.artista_id,
      genero_id: album.genero_id
    });
  };

  const handleDelete = async (id) => {
    if (!window.confirm('¿Estás seguro de que quieres eliminar este álbum?')) return;
    
    try {
      await musicService.deleteAlbum(id);
      await loadAlbums();
    } catch (err) {
      setError('Error al eliminar el álbum');
    }
  };

  const resetForm = () => {
    setFormData({
      nombre_album: '',
      fecha_salida_album: '',
      artista_id: '',
      genero_id: ''
    });
    setEditing(null);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Gestión de Álbumes</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editing ? 'Editar Álbum' : 'Nuevo Álbum'}
        </h2>
        
        <div className="grid grid-cols-1 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nombre del Álbum *
            </label>
            <input
              type="text"
              name="nombre_album"
              value={formData.nombre_album}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Fecha de Salida
            </label>
            <input
              type="date"
              name="fecha_salida_album"
              value={formData.fecha_salida_album}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded-md"
            />
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

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Género
            </label>
            <select
              name="genero_id"
              value={formData.genero_id}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded-md"
            >
              <option value="">Seleccionar género</option>
              {generos.map(genero => (
                <option key={genero.id_genero} value={genero.id_genero}>
                  {genero.nombre_genero}
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
                Artista
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Género
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Fecha de Salida
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Acciones
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {albums.map((album) => (
              <tr key={album.id_album}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">
                    {album.nombre_album}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {album.artista?.nombre_artista || '-'}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {album.genero?.nombre_genero || '-'}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm text-gray-500">
                    {album.fecha_salida_album || '-'}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button
                    onClick={() => handleEdit(album)}
                    className="text-indigo-600 hover:text-indigo-900 mr-4"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(album.id_album)}
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