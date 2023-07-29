from flask import Flask
from .extensions import settings, cors, database


def create_app(**config):
    app = Flask(__name__)
    settings.init_app(app, **config)
    database.init_app(app)
    # TODO: Set api endpoints
    cors.init_app(app)

    return app
