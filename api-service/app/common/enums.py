from enum import Enum


class DeploymentStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    FAILED = "FAILED"


class Routes(Enum):
    GET_DEPLOYMENT = "/deployments/<uuid:deployment_id>"
    CREATE_DEPLOYMENT = "/deployments"
