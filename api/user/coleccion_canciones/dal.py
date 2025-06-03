from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from api import models
import schemas


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