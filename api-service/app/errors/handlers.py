from flask import jsonify
from werkzeug.exceptions import HTTPException


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_HTTP_error(e: HTTPException):
        return (
            jsonify(
                {
                    "error": e.name,
                    "message": e.description,
                }
            ),
            e.code,
        )

    @app.errorhandler(Exception)
    def handle_exception(e: Exception):
        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error has occurred.",
                }
            ),
            500,
        )
