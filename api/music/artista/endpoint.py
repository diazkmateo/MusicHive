from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from music.artista import schemas

router = APIRouter(prefix="/artista", tags=["Artista"])


@router.post("/", response_model=schemas.ArtistaCreateRequest)
async def crear_artista(
    artista: schemas.ArtistaCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_artista = await dal.create_artista(db, artista)
    return nuevo_artista


@router.get("/{artista_id}", response_model=schemas.ArtistaResponse)
async def obtener_artista(
    artista_id: int,
    db: AsyncSession = Depends(get_db)
):
    artista = await dal.select_artista(db, artista_id)
    if artista is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artista


@router.get("/", response_model=list[schemas.ArtistaResponse])
async def obtener_todos_artistas(db: AsyncSession = Depends(get_db)):
    artistas = await dal.select_all_artistas(db)
    return artistas


@router.delete("/{artista_id}", status_code=204)
async def borrar_artista(artista_id: int, db: AsyncSession = Depends(get_db)):
    await dal.delete_artista(db, artista_id)
    return {"detail": "Artista eliminado"}