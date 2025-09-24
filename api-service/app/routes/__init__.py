from app.routes.deployments import deployments
from flask import Flask


def register_routes(app: Flask) -> None:
    app.register_blueprint(deployments)
