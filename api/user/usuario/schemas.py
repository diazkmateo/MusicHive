from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# REQUEST
class UsuarioCreateRequest(BaseModel):
    nombre_usuario: str
    contrasena_hash: str
    email: EmailStr
    rol_id: int  # SmallInteger en base de datos


class UsuarioUpdateRequest(BaseModel):
    rol_id: Optional[int] = None
    # Aquí se podrían añadir otros campos que se quieran poder actualizar


# RESPONSE
class UsuarioResponse(BaseModel):
    id: int
    nombre_usuario: str
    contrasena_hash: str
    email: EmailStr
    rol_id: int

    class Config:
        orm_mode = True