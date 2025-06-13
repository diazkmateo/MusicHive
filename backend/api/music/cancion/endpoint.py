from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from music.cancion import schemas

router = APIRouter(prefix="/canciones", tags=["Cancion"])


@router.post("/", response_model=schemas.CancionCreateRequest)
async def crear_cancion(
    cancion: schemas.CancionCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_cancion = await dal.create_cancion(db, cancion)
    return nueva_cancion


@router.get("/{cancion_id}", response_model=schemas.CancionResponse)
async def obtener_cancion(
    cancion_id: int,
    db: AsyncSession = Depends(get_db)
):
    cancion = await dal.select_cancion(db, cancion_id)
    if cancion is None:
        raise HTTPException(status_code=404, detail="Cancion no encontrada")
    return cancion