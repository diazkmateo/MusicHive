from pydantic import BaseModel, EmailStr

class UsuarioRegisterRequest(BaseModel):
    nombre_usuario: str
    contrasena: str
    email: EmailStr
    rol_id: int

class UsuarioLoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer" 