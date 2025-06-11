import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

function Navbar() {
  const { isAuthenticated, logout } = useAuth();

  return (
    <nav className="bg-indigo-600">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
          <div className="flex-shrink-0">
              <Link to="/" className="text-white font-bold text-xl">
                MusicHive
              </Link>
            </div>
            <div className="hidden md:block">
              <div className="ml-10 flex items-baseline space-x-4">
            <Link 
              to="/" 
                  className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Inicio
                </Link>
                <Link
                  to="/about"
                  className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Acerca de
                </Link>
                {isAuthenticated && (
                  <>
                    <Link
                      to="/albums"
                      className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                    >
                      Álbumes
                    </Link>
                    <Link
                      to="/songs"
                      className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                    >
                      Canciones
                    </Link>
                    <Link
                      to="/artists"
                      className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                    >
                      Artistas
                    </Link>
                    <Link
                      to="/genres"
                      className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                    >
                      Géneros
                    </Link>
                    <Link
                      to="/collections"
                      className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                    >
                      Colecciones
            </Link>
                  </>
                )}
              </div>
            </div>
          </div>
          <div className="hidden md:block">
            <div className="ml-4 flex items-center md:ml-6">
              {isAuthenticated ? (
                <>
              <Link
                    to="/profile"
                    className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
              >
                    Perfil
              </Link>
                  <button
                    onClick={logout}
                    className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                  >
                    Cerrar sesión
                  </button>
                </>
              ) : (
                <>
            <Link
              to="/login"
                    className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
            >
              Iniciar sesión
            </Link>
                  <Link
                    to="/register"
                    className="text-white hover:bg-indigo-500 px-3 py-2 rounded-md text-sm font-medium"
                  >
                    Registrarse
                  </Link>
                </>
              )}
            </div>
          </div>
          <div className="-mr-2 flex md:hidden">
            <button
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-md text-white hover:bg-indigo-500 focus:outline-none"
              aria-controls="mobile-menu"
              aria-expanded="false"
            >
              <span className="sr-only">Abrir menú principal</span>
              <svg
                className="block h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                aria-hidden="true"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
                </svg>
            </button>
          </div>
        </div>
      </div>

      <div className="md:hidden" id="mobile-menu">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <Link
            to="/"
            className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
          >
            Inicio
          </Link>
          <Link
            to="/about"
            className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
          >
            Acerca de
          </Link>
          {isAuthenticated && (
            <>
              <Link
                to="/albums"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Álbumes
              </Link>
              <Link
                to="/songs"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Canciones
              </Link>
              <Link
                to="/artists"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Artistas
              </Link>
              <Link
                to="/genres"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Géneros
              </Link>
              <Link
                to="/collections"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Colecciones
              </Link>
              <Link
                to="/profile"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Perfil
              </Link>
              <button
                onClick={logout}
                className="text-white hover:bg-indigo-500 block w-full text-left px-3 py-2 rounded-md text-base font-medium"
              >
                Cerrar sesión
              </button>
            </>
          )}
          {!isAuthenticated && (
            <>
            <Link
              to="/login"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
            >
              Iniciar sesión
            </Link>
              <Link
                to="/register"
                className="text-white hover:bg-indigo-500 block px-3 py-2 rounded-md text-base font-medium"
              >
                Registrarse
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
