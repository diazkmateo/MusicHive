from pydantic import BaseModel
from datetime import date
from typing import Optional


# REQUEST
class ColeccionCancionesCreateRequest(BaseModel):
    coleccion_id: int
    cancion_id: int
    fecha_anadido: Optional[date] = None  # Si no se envía, la BD puede usar su valor por defecto.


# RESPONSE
class ColeccionCancionesResponse(BaseModel):
    id: int
    coleccion_id: int
    cancion_id: int
    fecha_anadido: date

    class Config:
        orm_mode = True