from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from music.cancion import schemas

async def create_cancion(db: AsyncSession, cancion: schemas.CancionCreateRequest) -> models.Cancion:
    nueva_cancion = models.Cancion(
        nombre_cancion=cancion.nombre_cancion,
        duracion_segundos=cancion.duracion_segundos,
        numero_pista=cancion.numero_pista,
        album_id=cancion.album_id
    )
    db.add(nueva_cancion)
    await db.commit()
    await db.refresh(nueva_cancion)
    
    # Cargar el álbum después de crear la canción
    result = await db.execute(
        select(models.Cancion).where(models.Cancion.id == nueva_cancion.id).options(
            selectinload(models.Cancion.album)
        )
    )
    return result.scalar_one()

async def select_cancion(db: AsyncSession, cancion_id: int) -> models.Cancion | None:
    result = await db.execute(
        select(models.Cancion).where(models.Cancion.id == cancion_id).options(
            selectinload(models.Cancion.album)
        )
    )
    return result.scalar_one_or_none()

async def delete_cancion(db: AsyncSession, cancion_id: int) -> None:
    result = await db.execute(
        select(models.Cancion).where(models.Cancion.id == cancion_id)
    )
    cancion = result.scalar_one_or_none()
    if cancion:
        await db.delete(cancion)
        await db.commit()

async def update_cancion(db: AsyncSession, cancion_id: int, cancion_data: schemas.CancionUpdateRequest) -> models.Cancion | None:
    result = await db.execute(
        select(models.Cancion).where(models.Cancion.id == cancion_id)
    )
    cancion = result.scalar_one_or_none()
    
    if not cancion:
        return None
    
    for key, value in cancion_data.dict(exclude_unset=True).items():
        setattr(cancion, key, value)
    
    await db.commit()
    await db.refresh(cancion)
    return cancion

async def select_all_canciones(db: AsyncSession) -> list[models.Cancion]:
    result = await db.execute(
        select(models.Cancion).options(
            selectinload(models.Cancion.album)
        )
    )
    return result.scalars().all()