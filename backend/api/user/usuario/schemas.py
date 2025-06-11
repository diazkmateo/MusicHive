from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# REQUEST
class UsuarioCreateRequest(BaseModel):
    nombre_usuario: str
    password: str  # Contraseña en texto plano
    email: EmailStr
    rol_id: int  # SmallInteger en base de datos


class UsuarioLoginRequest(BaseModel):
    email: EmailStr
    password: str  # Contraseña en texto plano


# RESPONSE
class UsuarioResponse(BaseModel):
    id: int
    nombre_usuario: str
    email: EmailStr
    rol_id: int

    class Config:
        orm_mode = True