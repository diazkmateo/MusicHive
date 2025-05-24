from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/coleccion
async def coleccion():
    return {"coleccion": "coleccion loca"}