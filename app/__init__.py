from flask import Flask
from .extensions import settings, cors
from . import api


def create_app(**config):
    app = Flask(__name__)
    settings.init_app(app, **config)
    # TODO: init database and set models
    api.init_app(app)
    cors.init_app(app)

    return app
