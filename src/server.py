# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import os

from flask import Flask
from flask_cors import CORS

from services.logger import new
from routes.error_handler.error_handler import setup_error_handler
from routes.best_route.blueprint import setup_blueprint as setup_blueprint_best_route

LOG = new(__name__)

app = Flask(__name__)
CORS(app)

app.config["PROPAGATE_EXCEPTIONS"] = True


def register_blueprints(app_blueprint):
    LOG.info("Setup error handler")
    setup_error_handler(app_blueprint)
    LOG.info("Error handler registered")

    LOG.info("Registering blueprints")
    app_blueprint.register_blueprint(setup_blueprint_best_route())
    LOG.info("Blueprints registered")


def run_server():
    port = int(os.environ.get("PORT", 5000))

    register_blueprints(app)
    LOG.info("Starting app")
    app.run(host="0.0.0.0", port=port, debug=True)


if __name__ == "__main__":
    run_server()
