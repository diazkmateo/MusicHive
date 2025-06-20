from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import models
from database import get_db
from . import dal
from user.rating.schemas import RatingCreateRequest, RatingResponse
from user.auth.endpoint import get_current_user

router = APIRouter(prefix="/rating", tags=["Rating"])


@router.get("/", response_model=list[RatingResponse])
async def obtener_todos_ratings(
    db: AsyncSession = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    """
    Obtiene todos los ratings del usuario actual.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="No autorizado")
    
    ratings = await dal.get_ratings_by_user(db, current_user.id)
    return ratings


@router.get("/album/{album_id}", response_model=dict)
async def obtener_rating_promedio_album(
    album_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Obtiene el rating promedio y la cantidad de ratings para un álbum específico.
    """
    ratings = await dal.get_ratings_for_album(db, album_id)
    if not ratings:
        return {"promedio": 0, "total_ratings": 0}

    total_ratings = len(ratings)
    promedio = sum(r.puntuacion for r in ratings) / total_ratings

    return {"promedio": round(promedio, 2), "total_ratings": total_ratings}


@router.get("/{rating_id}", response_model=RatingResponse)
async def obtener_rating_por_id(
    rating_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    """
    Obtiene un rating específico por ID.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="No autorizado")
    
    rating = await dal.get_rating_by_id(db, rating_id, current_user.id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating no encontrado")
    
    return rating


@router.post("/", response_model=RatingResponse)
async def crear_o_actualizar_rating(
    rating_in: RatingCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    """
    Crea o actualiza un rating para un álbum.
    Un usuario solo puede tener un rating por álbum.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="No autorizado")

    rating = await dal.upsert_rating(db, rating_in, current_user.id)
    return rating


@router.delete("/{rating_id}")
async def borrar_rating(
    rating_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.Usuario = Depends(get_current_user)
):
    """
    Borra un rating específico.
    """
    if not current_user:
        raise HTTPException(status_code=403, detail="No autorizado")
    
    success = await dal.delete_rating_by_user(db, rating_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Rating no encontrado")
    
    return {"message": "Rating borrado exitosamente"} 