from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import get_db
from . import dal
from music.cancion import schemas

router = APIRouter(prefix="/cancion", tags=["Cancion"])


@router.post("/create", response_model=schemas.CancionResponse)
async def crear_cancion(
    cancion: schemas.CancionCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_cancion = await dal.create_cancion(db, cancion)
    return nueva_cancion


@router.get("/", response_model=List[schemas.CancionResponse])
async def obtener_canciones(
    db: AsyncSession = Depends(get_db)
):
    return await dal.select_all_canciones(db)


@router.get("/{cancion_id}", response_model=schemas.CancionResponse)
async def obtener_cancion(
    cancion_id: int,
    db: AsyncSession = Depends(get_db)
):
    cancion = await dal.select_cancion(db, cancion_id)
    if not cancion:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return cancion


@router.delete("/{cancion_id}")
async def borrar_cancion(
    cancion_id: int,
    db: AsyncSession = Depends(get_db)
):
    cancion = await dal.select_cancion(db, cancion_id)
    if not cancion:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    
    await dal.delete_cancion(db, cancion_id)
    return {"message": "Canción borrada exitosamente"}