import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { musicService } from '../services/api';

interface Album {
    id: number;
    titulo: string;
    fecha_lanzamiento: string;
    portada: string;
    canciones: number;
}

export default function ArtistAlbums() {
    const { artistId } = useParams<{ artistId: string }>();
    const [albums, setAlbums] = useState<Album[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchArtistAlbums = async () => {
            if (!artistId) return;
            
            try {
                const data = await musicService.getArtistAlbums(parseInt(artistId));
                setAlbums(data);
                setLoading(false);
            } catch (err) {
                setError('Error al cargar los álbumes del artista');
                setLoading(false);
            }
        };

        fetchArtistAlbums();
    }, [artistId]);

    if (loading) return <div className="flex justify-center items-center h-64">Cargando álbumes...</div>;
    if (error) return <div className="text-red-500 text-center">{error}</div>;

    return (
        <div className="container mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-8">Álbumes</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {albums.map((album) => (
                    <div key={album.id} className="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
                        <div className="relative h-48">
                            <img 
                                src={album.portada} 
                                alt={album.titulo}
                                className="w-full h-full object-cover"
                            />
                        </div>
                        <div className="p-6">
                            <h3 className="text-xl font-semibold mb-2">{album.titulo}</h3>
                            <p className="text-gray-600 text-sm">
                                {new Date(album.fecha_lanzamiento).toLocaleDateString()}
                            </p>
                            <p className="text-gray-500 text-sm mt-2">
                                {album.canciones} canciones
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
} 