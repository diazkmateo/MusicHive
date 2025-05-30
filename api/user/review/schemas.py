from pydantic import BaseModel
from typing import Optional
from datetime import date

# REQUEST

class ColeccionCreateRequest(BaseModel):
    id = int
    titulo_review = str # Aclarar tamaño de str?
    nota_review = int # smallint
    texto_review = Optional[str] = None
    album_id = int
    usuario_id = int

# RESPONSE

class ColeccionResponse(BaseModel):
    id = int
    titulo_review = str # Aclarar tamaño de str?
    nota_review = int # smallint
    texto_review = Optional[str] = None
    album_id = int
    usuario_id = int

    class Config:
        orm_mode = True  