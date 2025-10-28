from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


# Se genera la clase que permite la interaccion con la base de datos
db = SQLAlchemy()


class Barbero(db.Model):
    __tablename__ = 'barberos'
    
    id_barbero = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(Integer)
    correo = Column(String(150), unique=True, nullable=False)
    telefono = Column(String(20))
    
    # Relación con horarios ocupados
    horarios_ocupados = relationship('HorarioOcupado', back_populates='barbero')
    
    def to_dict(self):
        return {
            'id_barbero': self.id_barbero,
            'nombre': self.nombre,
            'edad': self.edad,
            'correo': self.correo,
            'telefono': self.telefono
        }


class HorarioOcupado(db.Model):
    __tablename__ = 'horarios_ocupados'
    
    id_horario = Column(Integer, primary_key=True, autoincrement=True)
    id_barbero = Column(Integer, ForeignKey('barberos.id_barbero'), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    cita_id = Column(Integer, nullable=False)
    
    # Relación con barbero
    barbero = relationship('Barbero', back_populates='horarios_ocupados')
    
    def to_dict(self):
        return {
            'id_horario': self.id_horario,
            'id_barbero': self.id_barbero,
            'fecha': self.fecha.isoformat() if self.fecha else None,
            'hora': str(self.hora) if self.hora else None,
            'cita_id': self.cita_id,
            'barbero': self.barbero.nombre if self.barbero else None
        }
