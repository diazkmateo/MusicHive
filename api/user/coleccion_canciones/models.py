from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ...database import Base

class ColeccionCanciones(Base):
    __tablename__ = "coleccion_canciones"

    id = Column(Integer, primary_key=True, index=True, name="id_coleccion_canciones")
    coleccion_id = Column(Integer, ForeignKey("coleccion.id_coleccion"), nullable=False)
    cancion_id = Column(Integer, ForeignKey("cancion.id_cancion"), nullable=False)
    fecha_anadido = Column(Date, nullable=False, default=func.current_date(), name="fecha_añadido")

    coleccion = relationship("Coleccion", back_populates="canciones_asociadas")
    cancion = relationship("Cancion", back_populates="colecciones_asociadas")

    def __repr__(self):
        return f"<ColeccionCanciones(id={self.id}, coleccion_id={self.coleccion_id}, cancion_id={self.cancion_id})>"