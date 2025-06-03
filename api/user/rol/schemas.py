from pydantic import BaseModel


# REQUEST
class RolCreateRequest(BaseModel):
    nombre_rol: str


# RESPONSE
class RolResponse(BaseModel):
    id: int
    nombre_rol: str

    class Config:
        orm_mode = True