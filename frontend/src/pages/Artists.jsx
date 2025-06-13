import { useState, useEffect } from 'react';
import { musicService } from '../services/musicService';

const Artists = () => {
  const [artists, setArtists] = useState([]);
  const [formData, setFormData] = useState({
    nombre_artista: '',
    fecha_formacion: '',
    pais_origen: ''
  });
  const [isEditing, setIsEditing] = useState(false);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadArtists();
  }, []);

  const loadArtists = async () => {
    try {
      console.log('Cargando artistas...');
      const data = await musicService.getArtists();
      console.log('Artistas cargados:', data);
      setArtists(data);
      setError(null);
    } catch (err) {
      console.error('Error al cargar artistas:', err);
      setError('Error al cargar los artistas');
    } finally {
      setLoading(false);
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
    try {
      const dataToSend = {
        ...formData,
        fecha_formacion: formData.fecha_formacion || null
      };
      console.log('Enviando datos:', dataToSend);

      if (isEditing) {
        console.log('Actualizando artista:', formData.id);
        await musicService.updateArtist(formData.id, dataToSend);
      } else {
        console.log('Creando nuevo artista');
        await musicService.createArtist(dataToSend);
      }
      setFormData({
        nombre_artista: '',
        fecha_formacion: '',
        pais_origen: ''
      });
      setIsEditing(false);
      loadArtists();
      setError(null);
    } catch (err) {
      console.error('Error al guardar artista:', err);
      if (err.response?.data?.detail) {
        setError(err.response.data.detail);
      } else {
        setError('Error al guardar el artista');
      }
    }
  };

  const handleEdit = (artist) => {
    console.log('Editando artista:', artist);
    setFormData({
      id: artist.id,
      nombre_artista: artist.nombre_artista,
      fecha_formacion: artist.fecha_formacion ? artist.fecha_formacion.split('T')[0] : '',
      pais_origen: artist.pais_origen || ''
    });
    setIsEditing(true);
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Estás seguro de que deseas eliminar este artista?')) {
      try {
        console.log('Eliminando artista:', id);
        await musicService.deleteArtist(id);
        console.log('Artista eliminado exitosamente');
        loadArtists();
        setError(null);
      } catch (err) {
        console.error('Error al eliminar artista:', err);
        setError('Error al eliminar el artista');
      }
    }
  };

  if (loading) {
    return <div className="text-center p-4">Cargando...</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Artistas</h1>
      
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="mb-8 bg-white p-6 rounded-lg shadow-md">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nombre del Artista
            </label>
            <input
              type="text"
              name="nombre_artista"
              value={formData.nombre_artista}
              onChange={handleChange}
              className="w-full p-2 border rounded"
              required
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Fecha de Formación
            </label>
            <input
              type="date"
              name="fecha_formacion"
              value={formData.fecha_formacion}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              País de Origen
            </label>
            <input
              type="text"
              name="pais_origen"
              value={formData.pais_origen}
              onChange={handleChange}
              className="w-full p-2 border rounded"
            />
          </div>
        </div>
        <div className="mt-4">
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            {isEditing ? 'Actualizar Artista' : 'Agregar Artista'}
          </button>
          {isEditing && (
            <button
              type="button"
              onClick={() => {
                setIsEditing(false);
                setFormData({
                  nombre_artista: '',
                  fecha_formacion: '',
                  pais_origen: ''
                });
              }}
              className="ml-2 bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
            >
              Cancelar
            </button>
          )}
        </div>
      </form>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Nombre
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                País de Origen
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Fecha de Formación
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Acciones
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {artists.map((artist) => (
              <tr key={artist.id}>
                <td className="px-6 py-4 whitespace-nowrap">
                  {artist.nombre_artista}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {artist.pais_origen}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {artist.fecha_formacion ? new Date(artist.fecha_formacion).toLocaleDateString() : ''}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <button
                    onClick={() => handleEdit(artist)}
                    className="text-indigo-600 hover:text-indigo-900 mr-4"
                  >
                    Editar
                  </button>
                  <button
                    onClick={() => handleDelete(artist.id)}
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
};

export default Artists; 