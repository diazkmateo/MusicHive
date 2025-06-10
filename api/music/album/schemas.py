from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class AlbumCreateRequest(BaseModel):
    nombre_album: str
    fecha_salida_album: Optional[date] 
    genero_id: Optional[int]
    artista_id: int

# RESPONSE

class AlbumResponse(BaseModel):
    id: int
    nombre_album: str
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: int

    class Config:
        orm_mode = True  

class AlbumUpdateRequest(BaseModel):
    nombre_album: Optional[str] = None
    fecha_salida_album: Optional[date] = None
    genero_id: Optional[int] = None
    artista_id: Optional[int] = None

    class Config:
        orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy