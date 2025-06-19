from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from . import dal
from user.rol import schemas

router = APIRouter(prefix="/rol", tags=["Rol"])


@router.post("/", response_model=schemas.RolCreateRequest)
async def crear_rol(
    rol: schemas.RolCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_rol = await dal.create_rol(db, rol)
    return nuevo_rol


@router.get("/{rol_id}", response_model=schemas.RolResponse)
async def obtener_rol(
    rol_id: int,
    db: AsyncSession = Depends(get_db)
):
    rol = await dal.select_rol(db, rol_id)
    if rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol