from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from user.rating.schemas import RatingCreateRequest, RatingResponse

router = APIRouter(prefix="/rating", tags=["Rating"])


@router.post("/", response_model=RatingCreateRequest)
async def crear_rating(
    rating: RatingCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_rating = await dal.create_rating(db, rating)
    return nueva_rating


@router.get("/{rating_id}", response_model=RatingResponse)
async def obtener_rating(
    rating_id: int,
    db: AsyncSession = Depends(get_db)
):
    rating = await dal.select_rating(db, rating_id)
    if rating is None:
        raise HTTPException(status_code=404, detail="Rating no encontrado")
    return rating