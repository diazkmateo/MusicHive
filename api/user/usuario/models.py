from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True, name="id_usuario")
    nombre_usuario = Column(String(20), nullable=False, unique=True)
    contrasena_hash = Column(String, nullable=False, name="contrasena_usuario")
    email = Column(String(50), unique=True, index=True, nullable=False)
    rol_id = Column(SmallInteger, ForeignKey("rol.id_rol"), nullable=False)

    rol = relationship("Rol", back_populates="usuarios")
        
    reviews = relationship("Review", back_populates="usuario", cascade="all, delete-orphan")
    ratings = relationship("Rating", back_populates="usuario", cascade="all, delete-orphan")
    colecciones = relationship("Coleccion", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario(id={self.id}, nombre_usuario='{self.nombre_usuario}')>"