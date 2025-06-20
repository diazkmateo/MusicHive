from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from fastapi import status

from database import get_db
from . import dal
from user.usuario import schemas
from user.auth.endpoint import is_admin

router = APIRouter(prefix="/usuario", tags=["Usuario"])

SECRET_KEY = "musichive-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuario/login")


@router.post("/", response_model=schemas.UsuarioResponse, dependencies=[Depends(is_admin)])
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


@router.get("/", response_model=list[schemas.UsuarioResponse], dependencies=[Depends(is_admin)])
async def obtener_todos_usuarios(db: AsyncSession = Depends(get_db)):
    return await dal.select_all_usuarios(db)


@router.put("/{usuario_id}", response_model=schemas.UsuarioResponse, dependencies=[Depends(is_admin)])
async def actualizar_usuario(
    usuario_id: int,
    usuario_data: schemas.UsuarioUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    usuario_actualizado = await dal.update_usuario(db, usuario_id, usuario_data)
    if usuario_actualizado is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_actualizado


@router.delete("/{usuario_id}", status_code=204, dependencies=[Depends(is_admin)])
async def borrar_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await dal.delete_usuario(db, usuario_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return None