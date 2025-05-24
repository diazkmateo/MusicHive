from sqlalchemy import Column, SmallInteger, String
from sqlalchemy.orm import relationship
from ...database import Base

class Rol(Base):
    __tablename__ = "rol"

    id = Column(SmallInteger, primary_key=True, index=True, name="id_rol")
    nombre_rol = Column(String(50), unique=True, nullable=False)

    usuarios = relationship("Usuario", back_populates="rol")
    def __repr__(self):
        return f"<Rol(id={self.id}, nombre_rol='{self.nombre_rol}')>"