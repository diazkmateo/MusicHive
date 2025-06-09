from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# REQUEST
class UsuarioCreateRequest(BaseModel):
    nombre_usuario: str
    contrasena_hash: str
    email: EmailStr
    rol_id: int  # SmallInteger en base de datos


# RESPONSE
class UsuarioResponse(BaseModel):
    id: int
    nombre_usuario: str
    contrasena_hash: str
    email: EmailStr
    rol_id: int

    class Config:
        orm_mode = True