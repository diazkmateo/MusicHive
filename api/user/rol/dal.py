from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api import models
import schemas


async def create_rol(db: AsyncSession, rol: schemas.RolCreateRequest) -> models.Rol:
    nuevo_rol = models.Rol(nombre_rol=rol.nombre_rol)
    db.add(nuevo_rol)
    await db.commit()
    await db.refresh(nuevo_rol)
    return nuevo_rol


async def select_rol(db: AsyncSession, rol_id: int) -> models.Rol | None:
    result = await db.execute(
        select(models.Rol).where(models.Rol.id == rol_id)
    )
    return result.scalar_one_or_none()