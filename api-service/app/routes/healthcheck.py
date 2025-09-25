import datetime

from flask import Blueprint, jsonify
from sqlalchemy import text

from ..extensions import db

hc_bp = Blueprint("healthcheck", __name__)


def check_database_status():
    try:
        db.session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(f"Database check failed: {e}")
        return False


@hc_bp.route("/", methods=["GET"])
def health_check_with_deps():
    db_healthy = check_database_status()
    current_time = datetime.datetime.now().isoformat()

    status = "healthy"
    issues = []

    if not db_healthy:
        status = "unhealthy"
        issues.append("database_down")

    http_status_code = 200 if status == "healthy" else 503

    return (
        jsonify(
            {
                "status": status,
                "timestamp": current_time,
                "dependencies": {"database": "healthy" if db_healthy else "unhealthy"},
                "issues": issues,
            }
        ),
        http_status_code,
    )
