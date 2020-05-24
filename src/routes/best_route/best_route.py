import flask_restful as restful
from webargs.flaskparser import use_args

from src.schemas.best_route import BestRouteSchema, NewRouteSchema
from services.logger import new

LOG = new(__name__)


class BestRoute(restful.Resource):
    @use_args(BestRouteSchema)
    def get(self, args):
        """

        :return:
        """
        pass

    @use_args(NewRouteSchema)
    def post(self, args):
        """

        :return:
        """
        pass
