from flask import Flask
from flask_cors import CORS

from config import Config
from models import db
from routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Habilitar CORS
    CORS(app)
    
    # Vincula la api con la clase SQLAlchemy
    db.init_app(app)
    
    # Registrar las rutas
    register_routes(app)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
