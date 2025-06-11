import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { musicService } from '../services/api';

interface Song {
    id: number;
    titulo: string;
    duracion: number;
    artista: string;
    album: string;
}

export default function AlbumSongs() {
    const { albumId } = useParams<{ albumId: string }>();
    const [songs, setSongs] = useState<Song[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchAlbumSongs = async () => {
            if (!albumId) return;
            
            try {
                const data = await musicService.getAlbumSongs(parseInt(albumId));
                setSongs(data);
                setLoading(false);
            } catch (err) {
                setError('Error al cargar las canciones del álbum');
                setLoading(false);
            }
        };

        fetchAlbumSongs();
    }, [albumId]);

    const formatDuration = (seconds: number) => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    };

    if (loading) return <div className="flex justify-center items-center h-64">Cargando canciones...</div>;
    if (error) return <div className="text-red-500 text-center">{error}</div>;

    return (
        <div className="container mx-auto px-4 py-8">
            <h2 className="text-3xl font-bold mb-8">Canciones</h2>
            <div className="bg-white rounded-lg shadow-lg overflow-hidden">
                <table className="min-w-full divide-y divide-gray-200">
                    <thead className="bg-gray-50">
                        <tr>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Título
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Artista
                            </th>
                            <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                Duración
                            </th>
                        </tr>
                    </thead>
                    <tbody className="bg-white divide-y divide-gray-200">
                        {songs.map((song) => (
                            <tr key={song.id} className="hover:bg-gray-50">
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm font-medium text-gray-900">{song.titulo}</div>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm text-gray-500">{song.artista}</div>
                                </td>
                                <td className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm text-gray-500">{formatDuration(song.duracion)}</div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
} 