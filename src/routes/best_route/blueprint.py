from flask import Blueprint
from flask_restful import Api

from .best_route import BestRoute


def setup_blueprint():
    blueprint = Blueprint("best_path", __name__)

    api = Api(blueprint)
    api.add_resource(BestRoute, "/best_route")
    return blueprint
