from flask import Flask
from app.config import Config
from extensions import register_extensions


def create_app(config_class: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    return app