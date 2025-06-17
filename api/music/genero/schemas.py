from pydantic import BaseModel
from typing import Optional
from datetime import date


class GeneroCreateRequest(BaseModel):
    nombre_genero: str
    

class GeneroResponse(BaseModel):
    id: int
    nombre_genero: str

    class Config:
        orm_mode = True

class GeneroUpdateRequest(BaseModel):
    nombre_genero: Optional[str] = None

    class Config:
        orm_mode = True 