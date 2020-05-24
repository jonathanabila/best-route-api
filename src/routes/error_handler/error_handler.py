from flask import jsonify

from exceptions.internal_exception import InternalException
from services.logger import new

LOG = new(__name__)


def setup_error_handler(app):
    def _make_error(_error):
        message = _error.message if hasattr(_error, "message") else "Invalid request"
        code = None

        if ":" in message:
            code = message.split(":")[0]
            message = message.split(":")[1]

        return {"errors": message, "code": code}

    @app.errorhandler(InternalException)
    def handle_error(err):
        return jsonify(_make_error(err)), err.code
