from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/genero
async def genero():
    return {"genero": "genero loco"}