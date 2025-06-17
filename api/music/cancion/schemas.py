from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# REQUEST

class CancionCreateRequest(BaseModel):
    nombre_cancion: str
    duracion_segundos: int
    numero_pista: Optional[int]
    album_id: int

# RESPONSE

class AlbumBase(BaseModel):
    id: int
    nombre_album: str
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: int

    class Config:
        orm_mode = True

class CancionResponse(BaseModel):
    id: int
    nombre_cancion: str
    duracion_segundos: int
    numero_pista: Optional[int]
    album_id: int
    album: Optional[AlbumBase] = None

    class Config:
        orm_mode = True

class CancionUpdateRequest(BaseModel):
    nombre_cancion: Optional[str] = None
    duracion_segundos: Optional[int] = None
    numero_pista: Optional[int] = None
    album_id: Optional[int] = None

    class Config:
        orm_mode = True