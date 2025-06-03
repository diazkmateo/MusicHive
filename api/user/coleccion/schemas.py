from pydantic import BaseModel
from typing import Optional


# REQUEST
class ColeccionCreateRequest(BaseModel):
    nombre_coleccion: str
    descripcion: Optional[str] = None
    usuario_id: int


# RESPONSE
class ColeccionResponse(BaseModel):
    id: int
    nombre_coleccion: str
    descripcion: Optional[str] = None
    usuario_id: int

    class Config:
        orm_mode = True