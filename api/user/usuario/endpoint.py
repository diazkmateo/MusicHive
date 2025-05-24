from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/usuario
async def usuario():
    return {"usuario": "usuario loco"}