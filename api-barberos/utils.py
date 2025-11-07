from flask_jwt_extended import create_access_token
from flask import jsonify
from models import db, Cliente
import requests



def get_cliente_by_email(email):
    try:
        cliente = Cliente.query.filter_by(correo=email).first()

        return {
            'success': True,
            'data': cliente.to_dict(),
        }

    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def insertar_cliente(data):
    nombre = data.get("nombre")
    correo = data.get("correo")
    telefono = data.get("telefono")

    cliente_nuevo = Cliente(
        nombre=nombre, 
        correo=correo, 
        telefono=telefono
    )

    db.session.add(cliente_nuevo)
    db.session.commit()
    db.session.close()



def create_token(data):
    nombre = data.get("nombre")
    correo = data.get("correo")
    telefono = data.get("telefono")

    access_token = create_access_token(
        identity={
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono
        }
    )

    return access_token