from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, Conflict, NotFound

from ..common.enums import DeploymentStatus, Routes
from ..extensions import db
from ..models import Deployment
from ..schemas import DeploymentSchema

deployments_bp = Blueprint("deployments", __name__)

create_deployment_schema = DeploymentSchema(only=("name", "github_url"))
deployment_schema = DeploymentSchema()


@deployments_bp.route(Routes.GET_DEPLOYMENT.value, methods=["GET"])
def get_deployment(deployment_id: str):
    deployment = Deployment.query.get(deployment_id)

    if not deployment:
        raise NotFound(description=f"Deployment {deployment_id} not found")

    return jsonify(deployment_schema.dump(deployment))


@deployments_bp.route(Routes.CREATE_DEPLOYMENT.value, methods=["POST"])
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
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    try:
        db.session.add(deployment)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        if "UNIQUE constraint failed" in str(e) or "duplicate key" in str(e):
            raise Conflict(
                description="A deployment with this name or URL already exists"
            )
        else:
            raise BadRequest(description="Database constraint violation")

    return jsonify(deployment_schema.dump(deployment)), 201
