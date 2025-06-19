from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
from user.rating import schemas


async def create_rating(db: AsyncSession, rating: schemas.RatingCreateRequest) -> models.Rating:
    nueva_rating = models.Rating(
        puntuacion=rating.puntuacion,
        album_id=rating.album_id,
        usuario_id=rating.usuario_id
    )
    db.add(nueva_rating)
    await db.commit()
    await db.refresh(nueva_rating)
    return nueva_rating


async def select_rating(db: AsyncSession, rating_id: int) -> models.Rating | None:
    result = await db.execute(
        select(models.Rating).where(models.Rating.id == rating_id)
    )
    return result.scalar_one_or_none()


async def select_all_ratings(db: AsyncSession):
    result = await db.execute(select(models.Rating))
    return result.scalars().all()


async def delete_rating(db: AsyncSession, rating_id: int) -> None:
    result = await db.execute(select(models.Rating).where(models.Rating.id == rating_id))
    rating = result.scalar_one_or_none()
    if rating:
        await db.delete(rating)
        await db.commit()