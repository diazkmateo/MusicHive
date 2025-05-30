from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ArtistaCreateRequest(BaseModel):
    id = int
    nombre_artista = str
    fecha_formacion = date # Optional[date]???
    pais_origen = str

# RESPONSE

class ArtistaResponse(BaseModel):
    id = int
    nombre_artista = str
    fecha_formacion = Optional[date] = None # Optional[date]???
    pais_origen = Optional[str] = None

    class Config:
        orm_mode = True  