import os

import click
from flask.cli import FlaskGroup

from . import create_app
from .config import DevConfig, ProdConfig
from .models import Deployment


def create_api_service():
    env = os.getenv("FLASK_ENV", "development")

    config_class = DevConfig if env == "development" else ProdConfig

    return create_app(config_class)


cli = FlaskGroup(create_app=create_api_service)


@cli.command("list_deployments")
def list_deployments():
    """List all deployments in the DB."""
    for d in Deployment.query.all():
        click.echo(f"{d.id} - {d.name} ({d.status})")


if __name__ == "__main__":
    cli()
