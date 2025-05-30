from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class GeneroCreateRequest(BaseModel):
    id = int
    nombre_genero = str
    
# RESPONSE

class GeneroResponse(BaseModel):
    id = int
    nombre_genero = str

    class Config:
        orm_mode = True  