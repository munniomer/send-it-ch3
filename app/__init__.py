import os
from flask import Flask, Blueprint
from config import app_config
from .database.db_connection import initialize_db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    initialize_db()
    return app
