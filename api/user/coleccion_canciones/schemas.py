from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int
    coleccion_id = int
    cancion_id = int
    fecha_anadido = date

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int
    coleccion_id = int
    cancion_id = int
    fecha_anadido = date

    class Config:
        orm_mode = True  