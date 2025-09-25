from flask import Flask

from .deployments import deployments_bp
from .healthcheck import hc_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(deployments_bp)
    app.register_blueprint(hc_bp)
