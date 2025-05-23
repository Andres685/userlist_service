import os
from flask import Flask
from flask_cors import CORS
from models import db
from routes import routes
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configuración de extensiones
    CORS(app)
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(routes)
    
    # Crear tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)