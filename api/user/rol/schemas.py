from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int #smallint
    nombre_rol = str

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int #smallint
    nombre_rol = str

    class Config:
        orm_mode = True  