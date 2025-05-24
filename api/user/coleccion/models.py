from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base

class Coleccion(Base):
    __tablename__ = "coleccion"

    id = Column(Integer, primary_key=True, index=True, name="id_coleccion")
    nombre_coleccion = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False, name="id_usuario")

    usuario = relationship("Usuario", back_populates="colecciones")
    canciones_asociadas = relationship("ColeccionCanciones", back_populates="coleccion", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Coleccion(id={self.id}, nombre_coleccion='{self.nombre_coleccion}')>"