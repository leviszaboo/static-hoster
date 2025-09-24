from uuid import uuid4

from app.common.enums import DeploymentStatus, Routes
from app.extensions import db
from app.models import Deployment
from app.schemas import DeploymentSchema
from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, NotFound

deployments = Blueprint("deployments", __name__)

create_deployment_schema = DeploymentSchema(only=("name", "github_url"))
deployment_schema = DeploymentSchema()


@deployments.route(Routes.GET_DEPLOYMENT.value, methods=["GET"])
def get_deployment(deployment_id: str):
    deployment = Deployment.query.get(deployment_id)

    if not deployment:
        raise NotFound(description=f"Deployment {deployment_id} not found")

    return jsonify(deployment_schema.dump(deployment))


@deployments.route(Routes.CREATE_DEPLOYMENT.value, methods=["POST"])
def create_deployment():
    data = request.get_json()

    errors = create_deployment_schema.validate(data)
    if errors:
        raise BadRequest(description=str(errors))

    deployment_id = str(uuid4())
    deployment_status = DeploymentStatus.PENDING.value
    deployment_url = None

    deployment = Deployment(
        id=deployment_id,
        github_url=data["github_url"],
        name=data["name"],
        status=deployment_status,
        url=deployment_url,
    )

    db.session.add(deployment)
    db.session.commit()

    return jsonify(deployment_schema.dump(deployment)), 201
