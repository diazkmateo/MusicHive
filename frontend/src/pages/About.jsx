function About() {
  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
            Acerca de MusicHive
          </h1>
          <p className="mt-5 max-w-xl mx-auto text-xl text-gray-500">
            Tu plataforma para descubrir, organizar y compartir tu música favorita.
          </p>
        </div>

        <div className="mt-20">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="px-4 py-5 sm:p-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">
                  Nuestra Misión
                </h3>
                <div className="mt-2 max-w-xl text-sm text-gray-500">
                  <p>
                    En MusicHive, nos apasiona conectar a los amantes de la música
                    con sus canciones favoritas. Nuestra misión es crear una
                    plataforma donde los usuarios puedan descubrir nueva música,
                    organizar sus colecciones y compartir sus gustos musicales con
                    otros.
                  </p>
                </div>
              </div>
            </div>

            <div className="bg-white overflow-hidden shadow rounded-lg">
              <div className="px-4 py-5 sm:p-6">
                <h3 className="text-lg leading-6 font-medium text-gray-900">
                  Características Principales
                </h3>
                <div className="mt-2 max-w-xl text-sm text-gray-500">
                  <ul className="list-disc pl-5 space-y-2">
                    <li>Gestión de álbumes y canciones</li>
                    <li>Organización de artistas y géneros</li>
                    <li>Creación de colecciones personalizadas</li>
                    <li>Reseñas y calificaciones</li>
                    <li>Perfiles de usuario personalizables</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="mt-20">
          <div className="bg-white shadow overflow-hidden sm:rounded-lg">
            <div className="px-4 py-5 sm:px-6">
              <h3 className="text-lg leading-6 font-medium text-gray-900">
                Tecnologías Utilizadas
              </h3>
              <p className="mt-1 max-w-2xl text-sm text-gray-500">
                Nuestra plataforma está construida con las últimas tecnologías web.
              </p>
            </div>
            <div className="border-t border-gray-200">
              <dl>
                <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                  <dt className="text-sm font-medium text-gray-500">Frontend</dt>
                  <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                    React, TailwindCSS, React Router
                  </dd>
                </div>
                <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                  <dt className="text-sm font-medium text-gray-500">Backend</dt>
                  <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                    FastAPI, SQLAlchemy, PostgreSQL
                  </dd>
                </div>
                <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
                  <dt className="text-sm font-medium text-gray-500">Autenticación</dt>
                  <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                    JWT (JSON Web Tokens)
                  </dd>
                </div>
              </dl>
            </div>
          </div>
        </div>

        <div className="mt-20 text-center">
          <h2 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            ¿Listo para comenzar?
          </h2>
          <p className="mt-4 text-lg leading-6 text-gray-500">
            Únete a nuestra comunidad y comienza a explorar el mundo de la música.
          </p>
          <div className="mt-8 flex justify-center">
            <div className="inline-flex rounded-md shadow">
              <a
                href="/register"
                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Registrarse
              </a>
            </div>
            <div className="ml-3 inline-flex">
              <a
                href="/login"
                className="inline-flex items-center justify-center px-5 py-3 border border-transparent text-base font-medium rounded-md text-indigo-600 bg-white hover:bg-gray-50"
              >
                Iniciar sesión
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About; 