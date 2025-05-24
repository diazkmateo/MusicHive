from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/coleccion_canciones
async def coleccion_canciones():
    return {"coleccion_cancion": "coleccion_cancion loco"}