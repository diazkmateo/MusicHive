from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
import models
from user.usuario import schemas


async def create_usuario(db: AsyncSession, usuario: schemas.UsuarioCreateRequest) -> models.Usuario:
    nuevo_usuario = models.Usuario(
        nombre_usuario=usuario.nombre_usuario,
        contrasena_hash=usuario.contrasena_hash,
        email=usuario.email,
        rol_id=usuario.rol_id
    )
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario

async def select_usuario(db: AsyncSession, usuario_id: int) -> models.Usuario | None:
    result = await db.execute(
        select(models.Usuario)
        .where(models.Usuario.id == usuario_id)
        .options(
            selectinload(models.Usuario.rol),
            selectinload(models.Usuario.reviews),
            selectinload(models.Usuario.ratings),
            selectinload(models.Usuario.colecciones)
        )
    )
    return result.scalar_one_or_none()

async def select_all_usuarios(db: AsyncSession):
    result = await db.execute(select(models.Usuario))
    return result.scalars().all()

async def delete_usuario(db: AsyncSession, usuario_id: int) -> bool:
    obj = await select_usuario(db, usuario_id)
    if obj is None:
        return False
    await db.delete(obj)
    await db.commit()
    return True