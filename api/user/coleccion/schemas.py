from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int
    nombre_coleccion = Optional[int] = None
    descripcion = Optional[str] = None
    usuario_id = int

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int
    nombre_coleccion = Optional[int] = None
    descripcion = Optional[str] = None
    usuario_id = int

    class Config:
        orm_mode = True  