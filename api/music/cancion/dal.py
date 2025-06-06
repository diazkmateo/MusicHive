from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from music.cancion import schemas

async def create_cancion(db: AsyncSession, Cancion: schemas.CancionCreateRequest) -> models.Cancion:
    nuevo_Cancion = models.Cancion(
        nombre_cancion=Cancion.nombre_cancion,
        duracion_segundos=Cancion.duracion_segundos,
        numero_pista=Cancion.numero_pista,
        album_id=Cancion.album_id
    )
    db.add(nuevo_Cancion)
    await db.commit()
    await db.refresh(nuevo_Cancion)
    return nuevo_Cancion

async def select_cancion(db: AsyncSession, cancion_id: int) -> models.Cancion | None:
    result = await db.execute(
        select(models.Cancion).where(models.Cancion.id == cancion_id).options(
            selectinload(models.Cancion.album_id)
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