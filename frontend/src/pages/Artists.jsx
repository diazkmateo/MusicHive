import { useState } from 'react';
import { useApp } from '../context/AppContext';
import { musicService } from '../services/api';

function Artists() {
  const { artists, loading, addArtist, updateArtist, deleteArtist } = useApp();
  const [formData, setFormData] = useState({
    name: '',
    country: '',
    bio: '',
  });
  const [editingId, setEditingId] = useState(null);
  const [formError, setFormError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormError('');

    try {
      if (editingId) {
        const response = await musicService.updateArtist(editingId, formData);
        updateArtist(response.data);
        setEditingId(null);
      } else {
        const response = await musicService.createArtist(formData);
        addArtist(response.data);
      }

      setFormData({
        name: '',
        country: '',
        bio: '',
      });
    } catch (err) {
      setFormError(err.response?.data?.detail || 'Error al guardar el artista');
    }
  };

  const handleEdit = (artist) => {
    setEditingId(artist.id);
    setFormData({
      name: artist.name,
      country: artist.country,
      bio: artist.bio,
    });
  };

  const handleDelete = async (id) => {
    try {
      await musicService.deleteArtist(id);
      deleteArtist(id);
    } catch (err) {
      setFormError('Error al eliminar el artista');
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="md:grid md:grid-cols-3 md:gap-6">
          <div className="md:col-span-1">
            <div className="px-4 sm:px-0">
              <h3 className="text-lg font-medium leading-6 text-gray-900">
                Artistas
              </h3>
              <p className="mt-1 text-sm text-gray-600">
                Administra tu colección de artistas.
              </p>
            </div>
          </div>

          <div className="mt-5 md:mt-0 md:col-span-2">
            <form onSubmit={handleSubmit}>
              <div className="shadow sm:rounded-md sm:overflow-hidden">
                <div className="px-4 py-5 bg-white space-y-6 sm:p-6">
                  {formError && (
                    <div className="rounded-md bg-red-50 p-4">
                      <div className="text-sm text-red-700">{formError}</div>
                    </div>
                  )}

                  <div className="grid grid-cols-6 gap-6">
                    <div className="col-span-6 sm:col-span-3">
                      <label
                        htmlFor="name"
                        className="block text-sm font-medium text-gray-700"
                      >
                        Nombre
                      </label>
                      <input
                        type="text"
                        name="name"
                        id="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                        className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                      />
                    </div>

                    <div className="col-span-6 sm:col-span-3">
                      <label
                        htmlFor="country"
                        className="block text-sm font-medium text-gray-700"
                      >
                        País
                      </label>
                      <input
                        type="text"
                        name="country"
                        id="country"
                        value={formData.country}
                        onChange={handleChange}
                        required
                        className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                      />
                    </div>

                    <div className="col-span-6">
                      <label
                        htmlFor="bio"
                        className="block text-sm font-medium text-gray-700"
                      >
                        Biografía
                      </label>
                      <textarea
                        name="bio"
                        id="bio"
                        rows={3}
                        value={formData.bio}
                        onChange={handleChange}
                        required
                        className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                      />
                    </div>
                  </div>
                </div>

                <div className="px-4 py-3 bg-gray-50 text-right sm:px-6">
                  <button
                    type="submit"
                    className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    {editingId ? 'Actualizar' : 'Crear'} artista
                  </button>
                </div>
              </div>
            </form>

            <div className="mt-8">
              <div className="flex flex-col">
                <div className="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                  <div className="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                    <div className="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                      <table className="min-w-full divide-y divide-gray-200">
                        <thead className="bg-gray-50">
                          <tr>
                            <th
                              scope="col"
                              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                            >
                              Nombre
                            </th>
                            <th
                              scope="col"
                              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                            >
                              País
                            </th>
                            <th
                              scope="col"
                              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                            >
                              Biografía
                            </th>
                            <th scope="col" className="relative px-6 py-3">
                              <span className="sr-only">Acciones</span>
                            </th>
                          </tr>
                        </thead>
                        <tbody className="bg-white divide-y divide-gray-200">
                          {artists.map((artist) => (
                            <tr key={artist.id}>
                              <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                                {artist.name}
                              </td>
                              <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                {artist.country}
                              </td>
                              <td className="px-6 py-4 text-sm text-gray-500">
                                {artist.bio}
                              </td>
                              <td className="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
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
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Artists; 