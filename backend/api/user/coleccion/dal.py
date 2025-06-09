from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
from user.coleccion import schemas


async def create_coleccion(
    db: AsyncSession,
    item: schemas.ColeccionCreateRequest
) -> models.Coleccion:
    nueva_coleccion = models.Coleccion(
        nombre_coleccion=item.nombre_coleccion,
        descripcion=item.descripcion,
        usuario_id=item.usuario_id
    )
    db.add(nueva_coleccion)
    await db.commit()
    await db.refresh(nueva_coleccion)
    return nueva_coleccion


async def select_coleccion(
    db: AsyncSession,
    coleccion_id: int
) -> models.Coleccion | None:
    result = await db.execute(
        select(models.Coleccion).where(models.Coleccion.id == coleccion_id)
    )
    return result.scalar_one_or_none()