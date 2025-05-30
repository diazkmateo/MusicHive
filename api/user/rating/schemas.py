from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int
    puntuacion = int
    fecha_creacion = date
    usuario_id = int
    album_id = int

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int
    puntuacion = int
    fecha_creacion = date
    usuario_id = int
    album_id = int

    class Config:
        orm_mode = True  