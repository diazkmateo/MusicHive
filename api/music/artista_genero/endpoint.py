from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/artista_genero
async def artista_genero():
    return {"artista_genero": "artista_genero loco"}