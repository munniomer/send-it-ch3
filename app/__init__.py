import os
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from config import app_config
from .database.db_connection import create_tables


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    jwt = JWTManager(app)
    from app.api.v2 import v2
    app.register_blueprint(v2)
    create_tables()
    return app
