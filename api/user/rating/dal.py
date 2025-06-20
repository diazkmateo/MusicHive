from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
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


async def get_ratings_by_user(db: AsyncSession, user_id: int) -> list[models.Rating]:
    """
    Obtiene todos los ratings de un usuario específico.
    """
    result = await db.execute(
        select(models.Rating).where(models.Rating.usuario_id == user_id)
    )
    return result.scalars().all()


async def get_rating_by_id(db: AsyncSession, rating_id: int, user_id: int) -> models.Rating | None:
    """
    Obtiene un rating específico por ID, verificando que pertenezca al usuario.
    """
    result = await db.execute(
        select(models.Rating).where(
            and_(
                models.Rating.id == rating_id,
                models.Rating.usuario_id == user_id
            )
        )
    )
    return result.scalar_one_or_none()


async def delete_rating_by_user(db: AsyncSession, rating_id: int, user_id: int) -> bool:
    """
    Borra un rating específico, verificando que pertenezca al usuario.
    Retorna True si se borró exitosamente, False si no se encontró.
    """
    result = await db.execute(
        select(models.Rating).where(
            and_(
                models.Rating.id == rating_id,
                models.Rating.usuario_id == user_id
            )
        )
    )
    rating = result.scalar_one_or_none()
    
    if rating:
        await db.delete(rating)
        await db.commit()
        return True
    return False


async def upsert_rating(db: AsyncSession, rating_in: schemas.RatingCreateRequest, user_id: int) -> models.Rating:
    """
    Crea un nuevo rating o actualiza uno existente para un usuario y álbum específicos.
    """
    # Buscar si ya existe un rating para este usuario y este álbum
    result = await db.execute(
        select(models.Rating).where(
            and_(
                models.Rating.usuario_id == user_id,
                models.Rating.album_id == rating_in.album_id
            )
        )
    )
    existing_rating = result.scalar_one_or_none()

    if existing_rating:
        # Si existe, actualiza la puntuación
        existing_rating.puntuacion = rating_in.puntuacion
        db.add(existing_rating)
        await db.commit()
        await db.refresh(existing_rating)
        return existing_rating
    else:
        # Si no existe, crea uno nuevo
        new_rating = models.Rating(
            puntuacion=rating_in.puntuacion,
            album_id=rating_in.album_id,
            usuario_id=user_id
        )
        db.add(new_rating)
        await db.commit()
        await db.refresh(new_rating)
        return new_rating


async def get_ratings_for_album(db: AsyncSession, album_id: int) -> list[models.Rating]:
    result = await db.execute(
        select(models.Rating).where(models.Rating.album_id == album_id)
    )
    return result.scalars().all()