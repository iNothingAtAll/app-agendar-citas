from flask import jsonify
from models import Barbero, Cronograma


def register_routes(app):
    @app.route('/')
    def index():
        return {
            'message': 'API de Barberos - Barbería',
            'version': '1.0.0',
            'endpoints': {
                'barberos': '/barberos',
                'cronograma': '/barberos/cronograma'
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


    @app.route('/barberos/cronograma', methods=['GET'])
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