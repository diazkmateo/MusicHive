from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from music.artista import schemas

async def create_artista(db: AsyncSession, artista: schemas.ArtistaCreateRequest) -> models.Artista:
    nuevo_artista = models.Artista(
        nombre_artista=artista.nombre_artista,
        fecha_formacion=artista.fecha_formacion,
        pais_origen=artista.pais_origen
    )
    db.add(nuevo_artista)
    await db.commit()
    await db.refresh(nuevo_artista)
    return nuevo_artista

async def select_artista(db: AsyncSession, artista_id: int) -> models.Artista | None:
    result = await db.execute(
        select(models.Artista).where(models.Artista.id == artista_id).options(
            selectinload(models.Artista.generos_asociados),
            selectinload(models.Artista.albums)
        )
    )
    return result.scalar_one_or_none() 

async def delete_artista(db: AsyncSession, artista_id: int) -> None:    
    result = await db.execute(
        select(models.Artista).where(models.Artista.id == artista_id)
    )
    artista = result.scalar_one_or_none()
    if artista:
        await db.delete(artista)
        await db.commit()

async def update_artista(db: AsyncSession, artista_id: int, artista_data: schemas.ArtistaUpdateRequest) -> models.Artista | None:
    result = await db.execute(
        select(models.Artista).where(models.Artista.id == artista_id)
    )
    artista = result.scalar_one_or_none()
    
    if not artista:
        return None
    
    for key, value in artista_data.dict(exclude_unset=True).items():
        setattr(artista, key, value)
    
    await db.commit()
    await db.refresh(artista)
    return artista

async def select_all_artistas(db: AsyncSession):
    result = await db.execute(
        select(models.Artista).options(
            selectinload(models.Artista.generos_asociados),
            selectinload(models.Artista.albums)
        )
    )
    return result.scalars().all()