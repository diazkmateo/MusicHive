from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
from music.artista_genero import schemas


async def create_artista_genero(
    db: AsyncSession,
    item: schemas.Artista_GeneroCreateRequest
) -> models.ArtistaGenero:
    nueva_asociacion = models.ArtistaGenero(
        artista_id=item.artista_id,
        genero_id=item.genero_id,
        fecha_anadido=item.fecha_anadido  # Si es None, SQLAlchemy usará el default
    )
    db.add(nueva_asociacion)
    await db.commit()
    await db.refresh(nueva_asociacion)
    return nueva_asociacion


async def select_artista_genero(
    db: AsyncSession,
    asociacion_id: int
) -> models.ArtistaGenero | None:
    result = await db.execute(
        select(models.ArtistaGenero).where(
            models.ArtistaGenero.id == asociacion_id
        )
    )
    return result.scalar_one_or_none()
