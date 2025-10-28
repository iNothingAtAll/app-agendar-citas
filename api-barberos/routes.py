from flask import jsonify
from models import Barbero, HorarioOcupado


def register_routes(app):
    @app.route('/')
    def index():
        return {
            'message': 'API de Barberos - Barbería',
            'version': '1.0.0',
            'endpoints': {
                'barberos': '/barberos',
                'cronograma': '/cronograma'
            }
        }


    @app.route('/barberos', methods=['GET'])
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

    
    @app.route('/cronograma', methods=['GET'])
    def get_all_horarios():
        try:
            horarios = HorarioOcupado.query.all()

            return jsonify({
                'success': True,
                'data': [horario.to_dict() for horario in horarios],
            }), 200

        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500