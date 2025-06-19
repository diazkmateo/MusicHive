from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from user.review.schemas import ReviewCreateRequest, ReviewResponse

router = APIRouter(prefix="/review", tags=["Review"])


@router.post("/", response_model=ReviewCreateRequest)
async def crear_rating(
    review: ReviewCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_review = await dal.create_review(db, review)
    return nueva_review


@router.get("/{review_id}", response_model=ReviewResponse)
async def obtener_rating(
    review_id: int,
    db: AsyncSession = Depends(get_db)
):
    review = await dal.select_review(db, review_id)
    if review is None:
        raise HTTPException(status_code=404, detail="Review no encontrada")
    return review


@router.get("/", response_model=list[ReviewResponse])
async def obtener_todas_reviews(db: AsyncSession = Depends(get_db)):
    reviews = await dal.select_all_reviews(db)
    return reviews


@router.delete("/{review_id}", status_code=204)
async def borrar_review(review_id: int, db: AsyncSession = Depends(get_db)):
    await dal.delete_review(db, review_id)
    return {"detail": "Review eliminada"}