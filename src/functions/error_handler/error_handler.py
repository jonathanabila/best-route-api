from flask import jsonify

from services.logger import new

LOG = new(__name__)


def setup_error_handler(app):
    @app.errorhandler(422)
    @app.errorhandler(400)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        LOG.error(f"Error: {messages}")
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    return
