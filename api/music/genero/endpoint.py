from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
import schemas

router = APIRouter(prefix="/genero", tags=["Genero"])


@router.post("/", response_model=schemas.GeneroCreateRequest)
async def crear_genero(
    genero: schemas.GeneroCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_genero = await dal.create_genero(db, genero)
    return nuevo_genero


@router.get("/{genero_id}", response_model=schemas.GeneroResponse)
async def obtener_genero(
    genero_id: int,
    db: AsyncSession = Depends(get_db)
):
    genero = await dal.select_genero(db, genero_id)
    if genero is None:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return genero