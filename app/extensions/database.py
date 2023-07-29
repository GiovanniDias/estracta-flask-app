from flask_sqlalchemy import SQLAlchemy


# Check changes before commit
db = SQLAlchemy(
    engine_options={
        "pool_recycle": 3600,
        "pool_pre_ping": True,
    })


def init_app(app):
    db.init_app(app)
