import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ArtistList from './components/ArtistList';
import ArtistAlbums from './components/ArtistAlbums';
import AlbumSongs from './components/AlbumSongs';
import Register from './components/Register';

function App() {
    return (
        <Router>
            <div className="min-h-screen bg-gray-100">
                <nav className="bg-white shadow-lg">
                    <div className="max-w-7xl mx-auto px-4">
                        <div className="flex justify-between h-16">
                            <div className="flex">
                                <div className="flex-shrink-0 flex items-center">
                                    <h1 className="text-2xl font-bold text-indigo-600">MusicHive</h1>
                                </div>
                                <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
                                    <a href="/" className="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">
                                        Artistas
                                    </a>
                                    <a href="/register" className="text-gray-500 hover:text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 border-transparent text-sm font-medium">
                                        Registrarse
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </nav>

                <main>
                    <Routes>
                        <Route path="/" element={<ArtistList />} />
                        <Route path="/artista/:artistId/albumes" element={<ArtistAlbums />} />
                        <Route path="/album/:albumId/canciones" element={<AlbumSongs />} />
                        <Route path="/register" element={<Register />} />
                    </Routes>
                </main>
            </div>
        </Router>
    );
}

export default App; 