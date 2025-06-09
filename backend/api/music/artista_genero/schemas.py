from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class Artista_GeneroCreateRequest(BaseModel):
    artista_id: int
    genero_id: int

# RESPONSE

class Artista_GeneroResponse(BaseModel):
    artista_id: int
    genero_id: int

    class Config:
        orm_mode = True  