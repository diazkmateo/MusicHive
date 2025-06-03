from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from users.coleccion import dal
from schemas import ColeccionCreateRequest, ColeccionResponse

router = APIRouter(prefix="/coleccion", tags=["Colección"])


@router.post("/", response_model=ColeccionResponse)
async def crear_coleccion(
    item: ColeccionCreateRequest,
    db: AsyncSession = Depends(get_async_session)
):
    nueva_coleccion = await dal.create_coleccion(db, item)
    return nueva_coleccion


@router.get("/{coleccion_id}", response_model=ColeccionResponse)
async def obtener_coleccion(
    coleccion_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    coleccion = await dal.select_coleccion(db, coleccion_id)
    if coleccion is None:
        raise HTTPException(status_code=404, detail="Colección no encontrada")
    return coleccion