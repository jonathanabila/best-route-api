from flask import jsonify

from exceptions.invalid_node import InvalidNode
from services.logger import new

LOG = new(__name__)


def setup_error_handler(app):
    @app.errorhandler(InvalidNode)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        LOG.error(f"Error: {messages}")
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code
