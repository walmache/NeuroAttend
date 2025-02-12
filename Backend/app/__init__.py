from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

# Inicializar extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    # Crear la aplicación Flask
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    # Inicializar extensiones con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints (rutas)
    from app.routes.clientes import clientes_bp
    from app.routes.reuniones import reuniones_bp
    from app.routes.asistencia import asistencia_bp

    app.register_blueprint(clientes_bp, url_prefix='/api/clientes')
    app.register_blueprint(reuniones_bp, url_prefix='/api/reuniones')
    app.register_blueprint(asistencia_bp, url_prefix='/api/asistencia')

    return app