from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# REQUEST

class AlbumCreateRequest(BaseModel):
    nombre_album: str
    fecha_salida_album: Optional[date] 
    genero_id: Optional[int]
    artista_id: int

# RESPONSE

class CancionBase(BaseModel):
    id: int
    nombre_cancion: str
    duracion_segundos: int
    numero_pista: Optional[int]
    album_id: int

    class Config:
        orm_mode = True

class AlbumResponse(BaseModel):
    id: int
    nombre_album: str
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: int
    genero: Optional["GeneroResponse"] = None
    artista: Optional["ArtistaResponse"] = None
    canciones: List[CancionBase] = []

    class Config:
        orm_mode = True

class AlbumUpdateRequest(BaseModel):
    nombre_album: Optional[str] = None
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: Optional[int] = None

    class Config:
        orm_mode = True

# Importaciones circulares
from music.genero.schemas import GeneroResponse
from music.artista.schemas import ArtistaResponse