from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from music.album import schemas

router = APIRouter(prefix="/albums", tags=["Album"])


@router.post("/", response_model=schemas.AlbumCreateRequest)
async def crear_album(
    album: schemas.AlbumCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_album = await dal.create_album(db, album)
    return nuevo_album


@router.get("/{album_id}", response_model=schemas.AlbumResponse)
async def obtener_album(
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    album = await dal.select_album(db, album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return album