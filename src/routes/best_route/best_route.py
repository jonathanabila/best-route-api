import flask_restful as restful
from flask import jsonify
from webargs.flaskparser import use_args

from schemas.best_route import BestRouteSchema, NewRouteSchema
from domain.graph import Graph

from services.logger import new

LOG = new(__name__)
graph = Graph()


class BestRoute(restful.Resource):
    @use_args(BestRouteSchema, location="querystring")
    def get(self, args):
        """

        :return:
        """
        response = graph.calculate(args["source"], args["destination"])
        return jsonify({"route": response[0], "cost": response[1]})

    @use_args(NewRouteSchema, location="json")
    def post(self, args):
        """

        :return:
        """
        graph.add_edge(args["source"], args["destination"], args["cost"])
        return jsonify({"status": "added", "route": {**args}})
