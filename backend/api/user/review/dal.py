from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
from user.review import schemas

async def create_review(db: AsyncSession, review: schemas.ReviewCreateRequest) -> models.Review:
    nueva_review = models.Review(
        contenido=review.contenido,
        album_id=review.album_id,
        usuario_id=review.usuario_id,
        fecha=review.fecha
    )
    db.add(nueva_review)
    await db.commit()
    await db.refresh(nueva_review)
    return nueva_review

async def select_review(db: AsyncSession, review_id: int) -> models.Review | None:
    result = await db.execute(
        select(models.Review).where(models.Review.id == review_id)
    )
    return result.scalar_one_or_none()