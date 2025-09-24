from marshmallow import Schema, fields


class DeploymentSchema(Schema):
    id = fields.UUID(required=True)
    github_url = fields.Url(required=True)
    name = fields.String(required=True)
    status = fields.String(required=True)
    url = fields.Url()
