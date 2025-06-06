from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class AlbumCreateRequest(BaseModel):
    id = int
    nombre_album = str
    fecha_salida_album = Optional[date] # Column(Date, nullable=True)
    genero_id = Optional[int]
    artista_id = int

# RESPONSE

class AlbumResponse(BaseModel):
    id: int
    nombre_album: str
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: int

    class Config:
        orm_mode = True  