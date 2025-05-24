from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/cancion
async def cancion():
    return {"cancion": "cancion loca"}