from app import create_app


def app():
    app = create_app()
    with app.app_context():
        yield app


def client(app):
    return app.test_client()
