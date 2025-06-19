from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from user.coleccion_canciones import dal
from user.coleccion_canciones.schemas import ColeccionCancionesCreateRequest, ColeccionCancionesResponse

router = APIRouter(prefix="/coleccion_canciones", tags=["ColeccionCanciones"])


@router.post("/", response_model=ColeccionCancionesResponse)
async def crear_coleccion_cancion(
    item: ColeccionCancionesCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nueva_asociacion = await dal.create_coleccion_cancion(db, item)
    return nueva_asociacion


@router.get("/{asociacion_id}", response_model=ColeccionCancionesResponse)
async def obtener_coleccion_cancion(
    asociacion_id: int,
    db: AsyncSession = Depends(get_db)
):
    asociacion = await dal.select_coleccion_cancion(db, asociacion_id)
    if asociacion is None:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return asociacion


@router.get("/", response_model=list[ColeccionCancionesResponse])
async def obtener_todas_coleccion_cancion(db: AsyncSession = Depends(get_db)):
    return await dal.select_all_coleccion_cancion(db)


@router.delete("/{asociacion_id}", status_code=204)
async def borrar_coleccion_cancion(asociacion_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await dal.delete_coleccion_cancion(db, asociacion_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Asociación no encontrada")
    return None