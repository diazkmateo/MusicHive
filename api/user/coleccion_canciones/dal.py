from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
from user.coleccion_canciones import schemas


async def create_coleccion_cancion(
    db: AsyncSession,
    item: schemas.ColeccionCancionesCreateRequest
) -> models.ColeccionCanciones:
    nueva_asociacion = models.ColeccionCanciones(
        coleccion_id=item.coleccion_id,
        cancion_id=item.cancion_id,
        # Si item.fecha_anadido es None, SQLAlchemy usará el default en el modelo
        fecha_anadido=item.fecha_anadido
    )
    db.add(nueva_asociacion)
    await db.commit()
    await db.refresh(nueva_asociacion)
    return nueva_asociacion


async def select_coleccion_cancion(
    db: AsyncSession,
    asociacion_id: int
) -> models.ColeccionCanciones | None:
    result = await db.execute(
        select(models.ColeccionCanciones).where(
            models.ColeccionCanciones.id == asociacion_id
        )
    )
    return result.scalar_one_or_none()


async def select_all_coleccion_cancion(db: AsyncSession):
    result = await db.execute(select(models.ColeccionCanciones))
    return result.scalars().all()


async def delete_coleccion_cancion(db: AsyncSession, asociacion_id: int) -> bool:
    obj = await select_coleccion_cancion(db, asociacion_id)
    if obj is None:
        return False
    await db.delete(obj)
    await db.commit()
    return True