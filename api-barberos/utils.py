from flask_jwt_extended import create_access_token
from flask import jsonify
from models import db, Cliente
import requests



def get_model_by_attributes(model, attributes: dict):
    try:
        element = model.query.filter_by(**attributes).first()

        return {
            'success': True,
            'data': element.to_dict(),
        }

    except Exception as e:
        return {
            'success': False,
            'error': f"Ocurrio un error al obtener el elemento de la tabla... {str(e)}"
        }


def create_model_instance(model, data: dict):
    try:
        instance = model(**data)
        db.session.add(instance)
        db.session.commit()

        return {
            'success': True,
            'data': instance.to_dict(),
        }

    except Exception as e:
        db.session.rollback()
        return {
            'success': False,
            'error': f"Ocurrio un error al crear el elemento de la tabla... {str(e)}"
        }


def create_client_token(data):
    try:
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

        return {
            'success': True,
            'token': access_token
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': f"Ocurrio un error al crear el token... {str(e)}"
        }