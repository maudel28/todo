from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import load_app_config
from .db_utils import get_engine_type
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    config = load_app_config()
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['style'] = config.get('style', {})

    @app.context_processor
    def inject_engine():
        return dict(engine=get_engine_type())
    
    db.init_app(app)

    with app.app_context():
        from . import routes
        from .models import Task
        db.create_all()

    return app
