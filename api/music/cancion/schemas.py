from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class CancionCreateRequest(BaseModel):
    id = int
    nombre_cancion = str
    duracion_segundos = int
    numero_pista: Optional[int]
    
    album_id: int # ESTO ES FK, PREGUNTAR AL PROFE


# RESPONSE

class CancionResponse(BaseModel):
    artista_id: int
    genero_id: int

    class Config:
        orm_mode = True  