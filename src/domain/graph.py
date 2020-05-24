from domain.dijsktra import Dijsktra
from services.file import File

FILE_PATH = "../dist/input-routes.csv"


class Graph(Dijsktra):
    def __init__(self):
        routes = File().get_file_content(FILE_PATH)
        super().__init__(routes)

    @staticmethod
    def _persist_edge(source, destination, cost):
        line = ",".join([source, destination, str(cost)])
        File().add_line(line, FILE_PATH)

    def add_edge_path(self, source, destination, cost):
        self.add_edge(source, destination, cost)
        self._persist_edge(source, destination, cost)
