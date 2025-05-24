from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/review
async def album():
    return {"album1": "Album loco"}