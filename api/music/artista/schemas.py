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
    fecha_formacion: Optional[date] = None # Optional[date]???
    pais_origen: Optional[str] = None

    class Config:
        orm_mode: True  

class ArtistaUpdateRequest(BaseModel):
    nombre_artista: Optional[str] = None
    fecha_formacion: Optional[date] = None # Optional[date]???
    pais_origen: Optional[str] = None

    class Config:
        orm_mode: True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy