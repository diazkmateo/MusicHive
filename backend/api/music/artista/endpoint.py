from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import logging
from sqlalchemy.exc import IntegrityError

from database import get_db
from . import dal
from music.artista import schemas

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/artistas", tags=["Artista"])


@router.get("/", response_model=List[schemas.ArtistaResponse])
async def listar_artistas(
    db: AsyncSession = Depends(get_db)
):
    artistas = await dal.get_artistas(db)
    return artistas


@router.post("/", response_model=schemas.ArtistaResponse)
async def crear_artista(
    artista: schemas.ArtistaCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Recibida petición para crear artista: {artista}")
    try:
        nuevo_artista = await dal.create_artista(db, artista)
        logger.info(f"Artista creado exitosamente: {nuevo_artista}")
        return nuevo_artista
    except IntegrityError as e:
        logger.error(f"Error de integridad al crear artista: {str(e)}")
        if "UNIQUE constraint failed: artista.nombre_artista" in str(e):
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe un artista con el nombre '{artista.nombre_artista}'"
            )
        raise HTTPException(status_code=500, detail="Error al crear el artista")
    except Exception as e:
        logger.error(f"Error al crear artista: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al crear el artista")


@router.get("/{artista_id}", response_model=schemas.ArtistaResponse)
async def obtener_artista(
    artista_id: int,
    db: AsyncSession = Depends(get_db)
):
    artista = await dal.select_artista(db, artista_id)
    if artista is None:
        raise HTTPException(status_code=404, detail="Artista no encontrado")
    return artista


@router.put("/{artista_id}", response_model=schemas.ArtistaResponse)
async def actualizar_artista(
    artista_id: int,
    artista: schemas.ArtistaUpdateRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        artista_actualizado = await dal.update_artista(db, artista_id, artista)
        if artista_actualizado is None:
            raise HTTPException(status_code=404, detail="Artista no encontrado")
        return artista_actualizado
    except IntegrityError as e:
        logger.error(f"Error de integridad al actualizar artista: {str(e)}")
        if "UNIQUE constraint failed: artista.nombre_artista" in str(e):
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe un artista con el nombre '{artista.nombre_artista}'"
            )
        raise HTTPException(status_code=500, detail="Error al actualizar el artista")
    except Exception as e:
        logger.error(f"Error al actualizar artista: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al actualizar el artista")


@router.delete("/{artista_id}")
async def eliminar_artista(
    artista_id: int,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Recibida petición para eliminar artista con ID: {artista_id}")
    try:
        artista = await dal.select_artista(db, artista_id)
        if artista is None:
            raise HTTPException(status_code=404, detail="Artista no encontrado")
        await dal.delete_artista(db, artista_id)
        logger.info(f"Artista {artista_id} eliminado exitosamente")
        return {"message": "Artista eliminado correctamente"}
    except Exception as e:
        logger.error(f"Error al eliminar artista: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al eliminar el artista")