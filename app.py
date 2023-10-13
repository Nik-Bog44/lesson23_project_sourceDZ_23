import os

from flask import Flask
from views import main_bp
from db import db


DB_NAME = os.getenv('DB-NAME')
DB_USER = os.getenv('DB-USER')
DB_PASSWORD = os.getenv('DB-PASSWORD')
DB_HOST = os.getenv('DB-HOST')


def create_app() -> Flask:
    """Initialize Flasc app"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app
