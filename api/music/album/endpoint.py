from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from datetime import date

from database import get_db
from . import dal
from music.album import schemas


router = APIRouter(prefix="/album", tags=["Album"])


@router.post("/create", response_model=schemas.AlbumCreateRequest)
async def crear_album(
    request: Request,
    nombre_album: str = Form(...),
    fecha_salida_album: Optional[date] = Form(None),  
    genero_id: Optional[int] = Form(None),
    artista_id: int = Form(...),
    db: AsyncSession = Depends(get_db)
):
    # Crea un diccionario con los datos del formulario
    album_data = {
        "nombre_album": nombre_album,
        "fecha_salida_album": fecha_salida_album,
        "genero_id": genero_id,
        "artista_id": artista_id,
    }

    # Crea un objeto AlbumCreateRequest con los datos del formulario
    album_create_request = schemas.AlbumCreateRequest(**album_data)
    nuevo_album = await dal.create_album(db, album_create_request)
    return {"request": nuevo_album}


@router.get("/{album_id}", response_model=schemas.AlbumResponse)
async def obtener_album(
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    album = await dal.select_album(db, album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    # return album
    return {"request": album}