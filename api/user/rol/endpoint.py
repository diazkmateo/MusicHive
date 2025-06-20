from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from . import dal
from user.rol import schemas
from sqlalchemy.future import select
from models import Rol

router = APIRouter(prefix="/rol", tags=["Rol"])


@router.get("/crear_roles_default")
async def crear_roles_default(db: AsyncSession = Depends(get_db)):
    roles = ["admin", "usuario"]
    creados = []
    for nombre in roles:
        result = await db.execute(select(Rol).where(Rol.nombre_rol == nombre))
        if not result.scalar_one_or_none():
            nuevo_rol = Rol(nombre_rol=nombre)
            db.add(nuevo_rol)
            creados.append(nombre)
    await db.commit()
    return {"creados": creados or "Ya existen"}


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


@router.get("/", response_model=list[schemas.RolResponse])
async def obtener_todos_roles(db: AsyncSession = Depends(get_db)):
    return await dal.select_all_roles(db)