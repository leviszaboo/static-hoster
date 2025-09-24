import uuid
from datetime import datetime

from app.common.enums import DeploymentStatus
from app.extensions import db
from sqlalchemy import Enum
from sqlalchemy.dialects.postgresql import UUID


class Deployment(db.Model):
    __tablename__ = "deployments"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    github_url = db.Column(db.String(255), nullable=False, unique=True, index=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    status = db.Column(Enum(DeploymentStatus), nullable=False, index=True)
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<Deployment {self.deployment_id} - {self.status}>"
