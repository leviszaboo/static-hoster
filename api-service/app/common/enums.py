from enum import Enum


class DeploymentStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"


class Routes(Enum):
    GET_DEPLOYMENT = "/api/deployments/<uuid:deployment_id>"
    CREATE_DEPLOYMENT = "/api/deployments"
