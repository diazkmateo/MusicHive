from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from music.album import schemas

async def create_album(db: AsyncSession, album: schemas.AlbumCreateRequest) -> models.Album:
    nuevo_album = models.Album(
        nombre_album=album.nombre_album,
        fecha_salida_album=album.fecha_salida_album,
        genero_id=album.genero_id,
        artista_id=album.artista_id
    )
    db.add(nuevo_album)
    await db.commit()
    await db.refresh(nuevo_album)
    return nuevo_album


async def select_album(db: AsyncSession, album_id: int) -> models.Album | None:
    result = await db.execute(
        select(models.Album).where(models.Album.id == album_id).options(
            selectinload(models.Album.genero),
            selectinload(models.Album.artista),
            selectinload(models.Album.canciones)
        )
    )
    return result.scalar_one_or_none() ### Preguntar


async def delete_album(db: AsyncSession, album_id: int) -> None:
    result = await db.execute(
        select(models.Album).where(models.Album.id == album_id)
    )
    album = result.scalar_one_or_none()
    if album:
        await db.delete(album)
        await db.commit()


async def update_album(db: AsyncSession, album_id: int, album_data: schemas.AlbumUpdateRequest) -> models.Album | None:
    result = await db.execute(
        select(models.Album).where(models.Album.id == album_id)
    )
    album = result.scalar_one_or_none()
    
    if not album:
        return None
    
    for key, value in album_data.dict(exclude_unset=True).items(): # Preguntar
        setattr(album, key, value)
    
    await db.commit()
    await db.refresh(album)
    return album