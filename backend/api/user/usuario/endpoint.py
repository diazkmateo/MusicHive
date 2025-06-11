from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from database import get_db
from . import dal
from user.usuario import schemas

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración de JWT
SECRET_KEY = "tu_clave_secreta_muy_segura"  # En producción, usar una clave segura y guardarla en variables de entorno
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(prefix="/usuario", tags=["Usuario"])


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login")
async def login(
    credentials: schemas.UsuarioLoginRequest,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Intento de login para email: {credentials.email}")
    try:
        usuario = await dal.get_usuario_by_email(db, credentials.email)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )
        
        if not verify_password(credentials.password, usuario.contrasena_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales inválidas"
            )

        access_token = create_access_token(
            data={"sub": usuario.email, "id": usuario.id}
        )
        
        return {
            "token": access_token,
            "user": {
                "id": usuario.id,
                "nombre_usuario": usuario.nombre_usuario,
                "email": usuario.email,
                "rol_id": usuario.rol_id
            }
        }
    except Exception as e:
        logger.error(f"Error en login: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.post("", response_model=schemas.UsuarioResponse)
@router.post("/", response_model=schemas.UsuarioResponse)
async def crear_usuario(
    usuario: schemas.UsuarioCreateRequest,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Recibida petición para crear usuario: {usuario}")
    try:
        nuevo_usuario = await dal.create_usuario(db, usuario)
        logger.info(f"Usuario creado exitosamente: {nuevo_usuario}")
        return nuevo_usuario
    except Exception as e:
        logger.error(f"Error al crear usuario: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{usuario_id}", response_model=schemas.UsuarioResponse)
async def obtener_usuario(
    usuario_id: int,
    db: AsyncSession = Depends(get_db)
):
    usuario = await dal.select_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario