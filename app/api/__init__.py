from .resource import bp as company_bp


def init_app(app):
    app.register_blueprint(company_bp)

    @app.route('/')
    def index():
        return app.config["APP_NAME"]
