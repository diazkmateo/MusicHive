from fastapi import APIRouter, Depends


router = APIRouter()

@router.get("/") # localhost:8000/rol
async def rol():
    return {"rol": "rol loco"}