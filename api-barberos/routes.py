from flask_jwt_extended import create_access_token, jwt_required
from flask import jsonify, request
from models import Barbero, Cronograma
import requests

def register_routes(app):
    @app.route('/')
    def index():
        return {
            'message': 'API de Barberos - Barbería',
            'version': '1.0.0',
            'endpoints': {
                'barberos': '/barberos',
                'cronograma': '/barberos/cronograma',
                'citas_barbero': '/barbero/<int:barbero_id>/citas',
                'registrar_usuario': '/registrar/usuario'
            }
        }


    @app.route('/registrar/usuario', methods=['POST'])
    def registrar_usuario():
        data = request.get_json()

        nombre = data.get("nombre")
        correo = data.get("correo")
        telefono = data.get("telefono")
        
        access_token = create_access_token(
            identity=nombre,
            additional_claims={"role": "usuario"}
        )

        return jsonify({
            "success": True,
            "access_token": access_token
        }), 200


    @app.route('/barberos', methods=['GET'])
    @jwt_required()
    def get_all_barberos():
        try:
            barberos = Barbero.query.all()

            return jsonify({
                'success': True,
                'data': [barbero.to_dict() for barbero in barberos],
            }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500


    @app.route('/barbero/<int:barbero_id>/citas', methods=['GET'])
    @jwt_required()
    def get_citas_barbero(barbero_id):
        try:
            response = requests.get(f'http://api-citas:5001/cita/{barbero_id}')

            if response.status_code != 200:
                return jsonify({
                    'success': False,
                    'error': f'Error al obtener citas.'
                }), response.status_code

            data = response.json()

            return jsonify({
                'success': True,
                'data': data
            }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500


    @app.route('/barberos/cronograma', methods=['GET'])
    @jwt_required()
    def get_all_horarios():
        try:
            cronograma = Cronograma.query.all()

            return jsonify({
                'success': True,
                'data': [horario.to_dict() for horario in cronograma],
            }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500