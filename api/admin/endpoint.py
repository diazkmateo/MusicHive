from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
from models import Rol

# Importa todos los modelos para que Base los conozca
import models

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/init-db", summary="Inicializa la base de datos")
async def init_db(db: AsyncSession = Depends(get_db)):
    """
    Borra todas las tablas y las vuelve a crear.
    Luego, inserta los roles 'admin' y 'usuario' si no existen.
    ¡USAR CON PRECAUCIÓN!
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    roles = ["admin", "usuario"]
    for nombre_rol in roles:
        nuevo_rol = Rol(nombre_rol=nombre_rol)
        db.add(nuevo_rol)
    
    await db.commit()
    
    return {"mensaje": "Base de datos inicializada y roles creados exitosamente."} 