from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/review
async def review():
    return {"review1": "Reseña loca"}