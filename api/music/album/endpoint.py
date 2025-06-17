from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Annotated, List
from datetime import date

from database import get_db
from . import dal
from music.album import schemas


router = APIRouter(prefix="/album", tags=["Album"])


@router.post("/create", response_model=schemas.AlbumResponse)
async def crear_album(
    album: schemas.AlbumCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_album = await dal.create_album(db, album)
    return nuevo_album


@router.get("/", response_model=List[schemas.AlbumResponse])
async def obtener_albumes(
    db: AsyncSession = Depends(get_db)
):
    return await dal.select_all_albums(db)


@router.get("/{album_id}", response_model=schemas.AlbumResponse)
async def obtener_album(
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    album = await dal.select_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    return album


@router.delete("/{album_id}")
async def borrar_album(
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    album = await dal.select_album(db, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    
    await dal.delete_album(db, album_id)
    return {"message": "Álbum eliminado correctamente"}