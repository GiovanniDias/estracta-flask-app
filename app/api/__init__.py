from .companies import bp as companies_bp


def init_app(app):
    app.register_blueprint(companies_bp)

    @app.route('/')
    def index():
        return app.config["APP_NAME"]
