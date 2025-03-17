from flask import Flask
from .routes import app_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(app_routes)  # Registra las rutas
    return app