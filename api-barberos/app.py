from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS

from config import Config
from models import db
from routes import register_routes

def create_app():
    # Crear la instancia de la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Habilitar CORS
    CORS(app)

    # Vincula la api con la clase SQLAlchemy
    db.init_app(app)
    
    
    # Configura JWT
    JWTManager(app)


    # Registro cada uno de las rutas
    register_routes(app)
    
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
