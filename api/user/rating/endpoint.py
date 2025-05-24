from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/rating
async def rating():
    return {"rating": "rating loco"}