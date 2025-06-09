import { Link } from 'react-router-dom';

function Footer() {
  return (
    <footer className="bg-gray-800">
      <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-white text-lg font-semibold mb-4">MusicHive</h3>
            <p className="text-gray-300 text-sm">
              Tu plataforma para descubrir, organizar y compartir tu música favorita.
            </p>
          </div>
          <div>
            <h3 className="text-white text-lg font-semibold mb-4">Enlaces</h3>
            <ul className="space-y-2">
              <li>
                <Link
                  to="/"
                  className="text-gray-300 hover:text-white text-sm"
                >
                  Inicio
                </Link>
              </li>
              <li>
                <Link
                  to="/about"
                  className="text-gray-300 hover:text-white text-sm"
                >
                  Acerca de
                </Link>
              </li>
              <li>
                <Link
                  to="/login"
                  className="text-gray-300 hover:text-white text-sm"
                >
                  Iniciar sesión
                </Link>
              </li>
              <li>
                <Link
                  to="/register"
                  className="text-gray-300 hover:text-white text-sm"
                >
                  Registrarse
                </Link>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-white text-lg font-semibold mb-4">Contacto</h3>
            <ul className="space-y-2">
              <li className="text-gray-300 text-sm">
                Email: info@musichive.com
              </li>
              <li className="text-gray-300 text-sm">
                Teléfono: +1 234 567 890
              </li>
            </ul>
          </div>
        </div>
        <div className="mt-8 border-t border-gray-700 pt-8">
          <p className="text-gray-300 text-sm text-center">
            &copy; {new Date().getFullYear()} MusicHive. Todos los derechos reservados.
          </p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
