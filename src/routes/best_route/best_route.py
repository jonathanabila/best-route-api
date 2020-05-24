import flask_restful as restful
from webargs.flaskparser import use_args

from src.schemas.best_route import BestRouteSchema, NewRouteSchema
from services.logger import new

LOG = new(__name__)


class BestRoute(restful.Resource):
    @use_args(BestRouteSchema, location="querystring")
    def get(self, args):
        """

        :return:
        """

        print(args)
        pass

    @use_args(NewRouteSchema, location="json")
    def post(self, args):
        """

        :return:
        """
        print(args)
        pass
