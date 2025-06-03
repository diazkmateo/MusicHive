from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST
class RatingCreateRequest(BaseModel):
    puntuacion: int        # SmallInteger en la base de datos
    album_id: int
    usuario_id: int


# RESPONSE
class RatingResponse(BaseModel):
    id: int
    puntuacion: int
    fecha_creacion: date
    album_id: int
    usuario_id: int

    class Config:
        orm_mode = True