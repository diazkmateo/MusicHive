from pydantic import BaseModel
from typing import Optional


# REQUEST
class ReviewCreateRequest(BaseModel):
    titulo_review: str  # máx. 100 si querés limitarlo
    nota_review: int    # puede ser SmallInteger (0-255)
    texto_review: Optional[str] = None
    album_id: int
    usuario_id: int


# RESPONSE
class ReviewResponse(BaseModel):
    id: int
    titulo_review: str
    nota_review: int
    texto_review: Optional[str] = None
    album_id: int
    usuario_id: int

    class Config:
        orm_mode = True