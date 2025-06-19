from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal # TABLA INTERMEDIA: Crear dal?
from music.artista_genero import schemas


router = APIRouter(prefix="/artista_genero", tags=["ArtistaGenero"])


@router.post("/", response_model=schemas.Artista_GeneroCreateRequest)
async def crear_artista_genero(
    artista_genero: schemas.Artista_GeneroCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_artista_genero = await dal.create_artista_genero(db, artista_genero)
    return nuevo_artista_genero


@router.get("/{artista_genero_id}", response_model=schemas.Artista_GeneroResponse)
async def obtener_artista_genero(
    artista_genero_id: int,
    db: AsyncSession = Depends(get_db)
):
    artista_genero = await dal.select_artista_genero(db, artista_genero_id)
    if artista_genero is None:
        raise HTTPException(status_code=404, detail="ArtistaGenero no encontrado")
    return artista_genero