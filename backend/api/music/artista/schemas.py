from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ArtistaCreateRequest(BaseModel):
    nombre_artista: str
    fecha_formacion: Optional[date] = None
    pais_origen: Optional[str] = None

# RESPONSE

class ArtistaResponse(BaseModel):
    id: int
    nombre_artista: str
    fecha_formacion: Optional[date] = None
    pais_origen: Optional[str] = None

    class Config:
        from_attributes = True

class ArtistaUpdateRequest(BaseModel):
    nombre_artista: Optional[str] = None
    fecha_formacion: Optional[date] = None
    pais_origen: Optional[str] = None

    class Config:
        from_attributes = True