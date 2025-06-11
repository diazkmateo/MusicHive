from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
import models
from user.usuario import schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def create_usuario(db: AsyncSession, usuario):
    hashed_password = get_password_hash(usuario.password)
    db_usuario = models.Usuario(
        nombre_usuario=usuario.nombre_usuario,
        contrasena_hash=hashed_password,
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


async def get_usuario_by_email(db: AsyncSession, email: str):
    result = await db.execute(
        select(models.Usuario).where(models.Usuario.email == email)
    )
    return result.scalar_one_or_none()