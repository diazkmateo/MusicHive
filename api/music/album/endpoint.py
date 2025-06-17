from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional, Annotated
from datetime import date

from database import get_db
from . import dal
from music.album import schemas


router = APIRouter(prefix="/album", tags=["Album"])


@router.post("/create", response_model=schemas.AlbumCreateRequest)
async def crear_album(
    request: Request,

    nombre_album: Annotated[str, Form(...)],
    fecha_salida_album: Annotated[int, Form(...)],  
    genero_id: Annotated[int, Form(...)],
    artista_id: Annotated[int, Form(...)],

    db: AsyncSession = Depends(get_db)
):
    try:
        fecha_salida = date.fromisoformat(fecha_salida_album)
    except ValueError:
        raise HTTPException(status_code=400, detail="Fecha de salida inválida. Use formato YYYY-MM-DD.")

    album_data = {
        "nombre_album": nombre_album,
        "fecha_salida_album": fecha_salida_album,
        "genero_id": genero_id,
        "artista_id": artista_id,
    }

    album_create_request = schemas.AlbumCreateRequest(**album_data)
    nuevo_album = await dal.create_album(db, album_create_request)
    return {"request": nuevo_album}


@router.get("/{album_id}", response_model=schemas.AlbumResponse)
async def obtener_album(
    request: Request,
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    album = await dal.select_album(db, album_id)
    if album is None:
        raise HTTPException(status_code=404, detail="Álbum no encontrado")
    # return album
    return {"request": album}