from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configuration import Param

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Param)

    db.init_app(app)

    # Importer et enregistrer les routes
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
