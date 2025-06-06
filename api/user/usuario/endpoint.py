from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from . import dal
from user.usuario import schemas

router = APIRouter(prefix="/usuario", tags=["Usuario"])


@router.post("/", response_model=schemas.UsuarioResponse)
async def crear_usuario(
    usuario: schemas.UsuarioCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    nuevo_usuario = await dal.create_usuario(db, usuario)
    return nuevo_usuario


@router.get("/{usuario_id}", response_model=schemas.UsuarioResponse)
async def obtener_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_db)
):
    usuario = await dal.select_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario