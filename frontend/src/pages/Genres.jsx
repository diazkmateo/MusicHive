import { useState, useEffect } from 'react';
import { musicService } from '../services/musicService';

export default function Genres() {
  const [genres, setGenres] = useState([]);
  const [formData, setFormData] = useState({
    nombre_genero: ''
  });
  const [editing, setEditing] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadGenres();
  }, []);

  const loadGenres = async () => {
    try {
      const data = await musicService.getGeneros();
      setGenres(data);
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
        await musicService.updateGenero(editing, formData);
      } else {
        await musicService.createGenero(formData);
      }
      await loadGenres();
      resetForm();
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al guardar el género');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (genre) => {
    setEditing(genre.id_genero);
    setFormData({
      nombre_genero: genre.nombre_genero
    });
  };

  const handleDelete = async (id) => {
    if (!window.confirm('¿Estás seguro de que quieres eliminar este género?')) return;
    
    try {
      await musicService.deleteGenero(id);
      await loadGenres();
    } catch (err) {
      setError('Error al eliminar el género');
    }
  };

  const resetForm = () => {
    setFormData({
      nombre_genero: ''
    });
    setEditing(null);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-8">Gestión de Géneros</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-semibold mb-4">
          {editing ? 'Editar Género' : 'Nuevo Género'}
        </h2>
        
        <div className="grid grid-cols-1 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nombre del Género *
            </label>
            <input
              type="text"
              name="nombre_genero"
              value={formData.nombre_genero}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-md"
            />
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
                Acciones
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {genres.map((genre) => (
              <tr key={genre.id_genero}>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="text-sm font-medium text-gray-900">
                    {genre.nombre_genero}
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button
                    onClick={() => handleEdit(genre)}
                    className="text-indigo-600 hover:text-indigo-900 mr-4"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(genre.id_genero)}
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