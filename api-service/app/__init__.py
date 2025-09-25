from flask import Flask

from .config import Config
from .errors import register_error_handlers
from .extensions import db, register_extensions
from .routes import register_routes


def create_app(config_class: Config = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_error_handlers(app)
    register_routes(app)

    with app.app_context():
        db.create_all()

    return app
