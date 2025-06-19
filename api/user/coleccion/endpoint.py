from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from user.coleccion.schemas import ColeccionCreateRequest, ColeccionResponse

router = APIRouter(prefix="/coleccion", tags=["Coleccion"]) # El atributo tag aparece en /docs


@router.post("/", response_model=ColeccionResponse)
async def create_coleccion(
    item: ColeccionCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_coleccion = await dal.create_coleccion(db, item)
    return nueva_coleccion


@router.get("/{coleccion_id}", response_model=ColeccionResponse)
async def setect_coleccion(
    coleccion_id: int,
    db: AsyncSession = Depends(get_db)
):
    coleccion = await dal.select_coleccion(db, coleccion_id)
    if coleccion is None:
        raise HTTPException(status_code=404, detail="Colección no encontrada")
    return coleccion