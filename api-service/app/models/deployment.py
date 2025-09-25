import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from ..extensions import db


class Deployment(db.Model):
    __tablename__ = "deployments"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    github_url = db.Column(db.String(255), nullable=False, unique=True, index=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    status = db.Column(db.String(50), nullable=False, index=True)
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    def __repr__(self):
        return f"<Deployment {self.deployment_id} - {self.status}>"
