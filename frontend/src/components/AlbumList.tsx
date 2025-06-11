import { useState, useEffect } from 'react';
import { musicService } from '../services/api';

interface Album {
    id: number;
    titulo: string;
    artista: string;
    fecha_lanzamiento: string;
    portada: string;
}

export default function AlbumList() {
    const [albums, setAlbums] = useState<Album[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchAlbums = async () => {
            try {
                const data = await musicService.getAlbums();
                setAlbums(data);
                setLoading(false);
            } catch (err) {
                setError('Error al cargar los álbumes');
                setLoading(false);
            }
        };

        fetchAlbums();
    }, []);

    if (loading) return <div>Cargando álbumes...</div>;
    if (error) return <div className="text-red-500">{error}</div>;

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
            {albums.map((album) => (
                <div key={album.id} className="bg-white rounded-lg shadow-md overflow-hidden">
                    <img 
                        src={album.portada} 
                        alt={album.titulo}
                        className="w-full h-48 object-cover"
                    />
                    <div className="p-4">
                        <h3 className="text-xl font-semibold">{album.titulo}</h3>
                        <p className="text-gray-600">{album.artista}</p>
                        <p className="text-sm text-gray-500">
                            {new Date(album.fecha_lanzamiento).toLocaleDateString()}
                        </p>
                    </div>
                </div>
            ))}
        </div>
    );
} 