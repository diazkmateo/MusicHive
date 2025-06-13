from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import models
from user.usuario import schemas
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def create_usuario(db: AsyncSession, usuario):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(
        nombre_usuario=usuario.nombre_usuario,
        contrasena_usuario=hashed_password,
        email=usuario.email,
        rol_id=usuario.rol_id
    )
    db.add(db_usuario)
    await db.commit()
    await db.refresh(db_usuario)
    return db_usuario


async def select_usuario(db: AsyncSession, usuario_id: int):
    result = await db.execute(
        select(models.Usuario).where(models.Usuario.id == usuario_id)
    )
    return result.scalar_one_or_none()


async def get_usuario_by_email(db: AsyncSession, email: str) -> Optional[models.Usuario]:
    result = await db.execute(
        select(models.Usuario).where(models.Usuario.email == email)
    )
    return result.scalar_one_or_none()


async def update_usuario(
    db: AsyncSession,
    usuario_id: int,
    usuario_update: schemas.UsuarioUpdateRequest
) -> Optional[models.Usuario]:
    try:
        # Obtener el usuario actual
        usuario = await select_usuario(db, usuario_id)
        if not usuario:
            return None

        # Actualizar campos básicos si se proporcionan
        if usuario_update.nombre_usuario is not None:
            usuario.nombre_usuario = usuario_update.nombre_usuario
        if usuario_update.email is not None:
            usuario.email = usuario_update.email

        # Actualizar contraseña si se proporciona
        if usuario_update.contrasena_actual and usuario_update.nueva_contrasena:
            # Verificar contraseña actual
            if not verify_password(usuario_update.contrasena_actual, usuario.contrasena_usuario):
                raise ValueError("La contraseña actual es incorrecta")
            
            # Actualizar con nueva contraseña
            usuario.contrasena_usuario = get_password_hash(usuario_update.nueva_contrasena)

        await db.commit()
        await db.refresh(usuario)
        return usuario
    except Exception as e:
        await db.rollback()
        raise e