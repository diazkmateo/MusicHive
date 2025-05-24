from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/artista
async def artista():
    return {"artista": "artista loco"}