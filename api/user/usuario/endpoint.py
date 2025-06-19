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


@router.get("/", response_model=list[schemas.UsuarioResponse])
async def obtener_todos_usuarios(db: AsyncSession = Depends(get_db)):
    return await dal.select_all_usuarios(db)


@router.delete("/{usuario_id}", status_code=204)
async def borrar_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await dal.delete_usuario(db, usuario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None