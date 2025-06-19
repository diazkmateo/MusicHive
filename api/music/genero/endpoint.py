from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from database import get_db
from . import dal
from music.genero import schemas

router = APIRouter(prefix="/genero", tags=["Genero"])


@router.post("/create", response_model=schemas.GeneroCreateRequest)
async def crear_genero(
    request: Request,
    nombre_genero: Annotated[str, Form(...)],
    db: AsyncSession = Depends(get_db)
):
    nuevo_genero = await dal.create_genero(db, nombre_genero)
    return nuevo_genero


@router.get("/{genero_id}", response_model=schemas.GeneroResponse)
async def obtener_genero(
    genero_id: int,
    db: AsyncSession = Depends(get_db)
):
    genero = await dal.select_genero(db, genero_id)
    if genero is None:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return genero

# @router.put("/update/{genero_id}", response_model=schemas.GeneroResponse)
# async def actualizar_genero(
#     genero_id: int,
#     nuevo_nombre_genero: Annotated[str, Form(...)],
#     db: AsyncSession = Depends(get_db)
# ):
#     genero_actualizado = await dal.update_genero(db, genero_id, nuevo_nombre_genero)
#     return genero_actualizado

@router.post("/delete/{genero_id}", status_code=204)
async def borrar_genero(
    genero_id: int,
    db: AsyncSession = Depends(get_db)
):
    borrado = await dal.delete_genero(db, genero_id)
    if not borrado:
        raise HTTPException(status_code=404, detail="Genero no encontrado")
    return "Género borrado con éxito"

@router.get("/", response_model=list[schemas.GeneroResponse])
async def obtener_todos_generos(db: AsyncSession = Depends(get_db)):
    generos = await dal.select_all_generos(db)
    return generos