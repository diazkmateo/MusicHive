import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { userService } from '../services/api';

function Profile() {
  const { user } = useAuth();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [formData, setFormData] = useState({
    nombre_usuario: '',
    email: '',
    contrasena_actual: '',
    nueva_contrasena: '',
    confirmar_contrasena: '',
  });

  useEffect(() => {
    if (user) {
      setFormData(prev => ({
        ...prev,
        nombre_usuario: user.nombre_usuario || '',
        email: user.email || '',
      }));
      setLoading(false);
    }
  }, [user]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value,
    }));
    setError('');
    setSuccess('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    // Validaciones
    if (!formData.nombre_usuario || !formData.email) {
      setError('El nombre de usuario y el correo electrónico son obligatorios');
      return;
    }

    if (formData.nueva_contrasena) {
      if (!formData.contrasena_actual) {
        setError('Debes ingresar tu contraseña actual para cambiarla');
        return;
      }
      if (formData.nueva_contrasena !== formData.confirmar_contrasena) {
        setError('Las contraseñas no coinciden');
        return;
      }
      if (formData.nueva_contrasena.length < 6) {
        setError('La nueva contraseña debe tener al menos 6 caracteres');
        return;
      }
    }

    try {
      const updateData = {
        nombre_usuario: formData.nombre_usuario,
        email: formData.email,
      };

      if (formData.nueva_contrasena) {
        updateData.contrasena_actual = formData.contrasena_actual;
        updateData.nueva_contrasena = formData.nueva_contrasena;
      }

      await userService.updateProfile(updateData);
      setSuccess('Perfil actualizado correctamente');
      
      // Limpiar campos de contraseña
      setFormData(prev => ({
        ...prev,
        contrasena_actual: '',
        nueva_contrasena: '',
        confirmar_contrasena: '',
      }));
    } catch (err) {
      console.error('Error al actualizar el perfil:', err);
      setError(err.response?.data?.detail || 'Error al actualizar el perfil');
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
      <div className="max-w-3xl mx-auto">
        <div className="bg-white shadow sm:rounded-lg">
          <div className="px-4 py-5 sm:p-6">
            <h3 className="text-lg leading-6 font-medium text-gray-900">
              Perfil de usuario
            </h3>
            <div className="mt-2 max-w-xl text-sm text-gray-500">
              <p>Actualiza tu información personal y contraseña.</p>
            </div>
            <form onSubmit={handleSubmit} className="mt-5 space-y-6">
              {error && (
                <div className="rounded-md bg-red-50 p-4">
                  <div className="text-sm text-red-700">{error}</div>
                </div>
              )}
              {success && (
                <div className="rounded-md bg-green-50 p-4">
                  <div className="text-sm text-green-700">{success}</div>
                </div>
              )}
              <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                <div className="sm:col-span-3">
                  <label
                    htmlFor="nombre_usuario"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Nombre de usuario
                  </label>
                  <div className="mt-1">
                    <input
                      type="text"
                      name="nombre_usuario"
                      id="nombre_usuario"
                      value={formData.nombre_usuario}
                      onChange={handleChange}
                      required
                      className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                    />
                  </div>
                </div>

                <div className="sm:col-span-3">
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium text-gray-700"
                  >
                    Correo electrónico
                  </label>
                  <div className="mt-1">
                    <input
                      type="email"
                      name="email"
                      id="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                      className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                    />
                  </div>
                </div>

                <div className="sm:col-span-6">
                  <h4 className="text-sm font-medium text-gray-900">
                    Cambiar contraseña
                  </h4>
                  <div className="mt-2 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                    <div className="sm:col-span-2">
                      <label
                        htmlFor="contrasena_actual"
                        className="block text-sm font-medium text-gray-700"
                      >
                        Contraseña actual
                      </label>
                      <div className="mt-1">
                        <input
                          type="password"
                          name="contrasena_actual"
                          id="contrasena_actual"
                          value={formData.contrasena_actual}
                          onChange={handleChange}
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        />
                      </div>
                    </div>

                    <div className="sm:col-span-2">
                      <label
                        htmlFor="nueva_contrasena"
                        className="block text-sm font-medium text-gray-700"
                      >
                        Nueva contraseña
                      </label>
                      <div className="mt-1">
                        <input
                          type="password"
                          name="nueva_contrasena"
                          id="nueva_contrasena"
                          value={formData.nueva_contrasena}
                          onChange={handleChange}
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        />
                      </div>
                    </div>

                    <div className="sm:col-span-2">
                      <label
                        htmlFor="confirmar_contrasena"
                        className="block text-sm font-medium text-gray-700"
                      >
                        Confirmar contraseña
                      </label>
                      <div className="mt-1">
                        <input
                          type="password"
                          name="confirmar_contrasena"
                          id="confirmar_contrasena"
                          value={formData.confirmar_contrasena}
                          onChange={handleChange}
                          className="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div className="flex justify-end">
                <button
                  type="submit"
                  className="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Guardar cambios
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Profile; 