from flask import jsonify
from models import Cita, EstadoCita


def register_routes(app):
    @app.route('/')
    def index():
        return {
            'message': 'API de Citas - Barbería',
            'version': '1.0.0',
            'endpoints': {
                'citas': '/citas',
                'cita': '/cita/<:id>',
            }
        }
    

    @app.route('/citas', methods=['GET'])
    def get_all_citas():
        try:
            citas = Cita.query.all()

            return jsonify({
                'success': True,
                'data': [cita.to_dict() for cita in citas],
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500


    @app.route('/cita/<int:barbero_id>', methods=['GET'])
    def get_cita(barbero_id):
        try:
            cita = Cita.query.get_or_404(barbero_id)

            return jsonify({
                'success': True,
                'data': cita.to_dict(),
            }), 200
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
