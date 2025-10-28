from sqlalchemy import create_engine, Column, Integer, String, Date, Time, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Se genera la clase que permite la interaccion con la base de datos
db = SQLAlchemy()


class EstadoCita(db.Model):
    __tablename__ = 'estados_cita'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_estado = Column(String(50), nullable=False, unique=True)
    
    # Relación con citas
    citas = relationship('Cita', back_populates='estado')
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre_estado': self.nombre_estado
        }


class Cita(db.Model):
    __tablename__ = 'citas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    notas = Column(Text)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    barbero_id = Column(Integer, nullable=False)
    estado_id = Column(Integer, ForeignKey('estados_cita.id'), nullable=False, default=1)
    
    # Relación con estado
    estado = relationship('EstadoCita', back_populates='citas')
    
    def to_dict(self):
        return {
            'id': self.id,
            'fecha': self.fecha.isoformat() if self.fecha else None,
            'hora': str(self.hora) if self.hora else None,
            'notas': self.notas,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'barbero_id': self.barbero_id,
            'estado_id': self.estado_id,
            'estado': self.estado.nombre_estado if self.estado else None
        }
