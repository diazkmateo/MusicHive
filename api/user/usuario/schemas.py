from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int
    nombre_usuario = str
    contrasena_hash = str
    email = str
    rol_id = int #smallint

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int
    nombre_usuario = str
    contrasena_hash = str
    email = str
    rol_id = int #smallint

    class Config:
        orm_mode = True  