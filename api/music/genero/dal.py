from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from music.genero import schemas

async def create_genero(db: AsyncSession, genero: str):
    nuevo_genero = models.Genero(
        nombre_genero = genero
    )
    db.add(nuevo_genero)
    await db.commit()
    await db.refresh(nuevo_genero)
    return nuevo_genero

async def select_genero(db: AsyncSession, genero_id: int) -> models.Genero | None: 
    result = await db.execute(
        select(models.Genero).where(models.Genero.id == genero_id).options(
            selectinload(models.Genero.artistas_asociados),
            selectinload(models.Genero.albums)
        )
    )
    return result.scalar_one_or_none()

async def delete_genero(db: AsyncSession, genero_id: int) -> None:
    result = await db.execute(
        select(models.Genero).where(models.Genero.id == genero_id)
    )
    genero = result.scalar_one_or_none()
    if genero:
        await db.delete(genero)
        await db.commit()

async def update_genero(db: AsyncSession, genero_id: int, genero_data: schemas.GeneroUpdateRequest) -> models.Genero | None:
    result = await db.execute(
        select(models.Genero).where(models.Genero.id == genero_id)
    )
    genero = result.scalar_one_or_none()
    
    if not genero:
        return None
    
    for key, value in genero_data.dict(exclude_unset=True).items():
        setattr(genero, key, value)
    
    await db.commit()
    await db.refresh(genero)
    return genero