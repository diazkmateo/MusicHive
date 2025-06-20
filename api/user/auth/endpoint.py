from fastapi import APIRouter, Depends, HTTPException, status, Security
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from fastapi.security import OAuth2PasswordBearer, HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from database import get_db
from user.usuario import dal as usuario_dal
from . import schemas
import models

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "musichive-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
http_bearer = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(http_bearer), db: AsyncSession = Depends(get_db)) -> models.Usuario:
    """Decodifica el token, obtiene el usuario de la BD y lo devuelve."""
    from sqlalchemy.future import select
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        nombre_usuario: str = payload.get("sub")
        if nombre_usuario is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
        
        result = await db.execute(
            select(models.Usuario)
            .where(models.Usuario.nombre_usuario == nombre_usuario)
            .options(selectinload(models.Usuario.rol))
        )
        usuario = result.scalar_one_or_none()

        if usuario is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
        return usuario
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")

async def is_admin(current_user: models.Usuario = Depends(get_current_user)):
    """Verifica si el usuario actual es administrador."""
    if not current_user.rol or current_user.rol.nombre_rol.lower() != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acceso denegado: se requiere rol de administrador.")
    return current_user

async def verificar_usuario(nombre_usuario: str, contrasena: str, db: AsyncSession):
    from sqlalchemy.future import select
    result = await db.execute(
        select(models.Usuario)
        .where(models.Usuario.nombre_usuario == nombre_usuario)
        .options(selectinload(models.Usuario.rol))
    )
    usuario = result.scalar_one_or_none()
    if usuario and pwd_context.verify(contrasena, usuario.contrasena_hash):
        return usuario
    return None

def crear_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register", status_code=201)
async def register_usuario(request: schemas.UsuarioRegisterRequest, db: AsyncSession = Depends(get_db)):
    # Verificar si el usuario ya existe
    from sqlalchemy.future import select
    result = await db.execute(select(models.Usuario).where(models.Usuario.nombre_usuario == request.nombre_usuario))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    # Crear usuario usando DAL
    await usuario_dal.create_usuario(db, request)
    return {"msg": "Usuario registrado exitosamente"}

@router.post("/login", response_model=schemas.TokenResponse)
async def login_usuario(form_data: schemas.UsuarioLoginRequest, db: AsyncSession = Depends(get_db)):
    usuario = await verificar_usuario(form_data.nombre_usuario, form_data.contrasena, db)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    access_token = crear_token({"sub": usuario.nombre_usuario, "id": usuario.id, "rol": usuario.rol.nombre_rol})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def get_current_user_info(current_user: models.Usuario = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "nombre_usuario": current_user.nombre_usuario,
        "email": current_user.email,
        "rol": current_user.rol.nombre_rol if current_user.rol else "Sin rol"
    } 