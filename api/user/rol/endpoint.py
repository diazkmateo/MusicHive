from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from users.rol import dal
import schemas

router = APIRouter(prefix="/rol", tags=["Rol"])


@router.post("/", response_model=schemas.RolResponse)
async def crear_rol(
    rol: schemas.RolCreateRequest,
    db: AsyncSession = Depends(get_async_session)
):
    nuevo_rol = await dal.create_rol(db, rol)
    return nuevo_rol


@router.get("/{rol_id}", response_model=schemas.RolResponse)
async def obtener_rol(
    rol_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    rol = await dal.select_rol(db, rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol