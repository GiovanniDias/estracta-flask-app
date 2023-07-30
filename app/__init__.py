from flask import Flask
from .extensions import settings, cors, database
from . import api


def create_app(**config):
    app = Flask(__name__)
    settings.init_app(app, **config)
    database.init_app(app)
    api.init_app(app)
    cors.init_app(app)

    return app
