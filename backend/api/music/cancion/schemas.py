from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class CancionCreateRequest(BaseModel):
    id: int
    nombre_cancion: str
    duracion_segundos: int
    numero_pista: Optional[int]
    
    album_id: int 


# RESPONSE

class CancionResponse(BaseModel):
    artista_id: int
    genero_id: int

    class Config:
        orm_mode = True  

class CancionUpdateRequest(BaseModel):
    nombre_cancion: Optional[str] = None
    duracion_segundos: Optional[int] = None
    numero_pista: Optional[int] = None
    album_id: Optional[int] = None

    class Config:
        orm_mode = True  # Permite que Pydantic lea los datos de los modelos ORM