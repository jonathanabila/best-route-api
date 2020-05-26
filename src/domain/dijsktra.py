from services.graph import Graph


class Dijsktra:
    def __init__(self, edges):
        self._graph = Graph(self.parse_edger(edges))

    @staticmethod
    def parse_edger(edges):
        return [tuple(i) for i in edges]

    def calculate(self, source, destination):
        path, cost = self._graph.dijkstra(source, destination)
        return " - ".join(path), cost

    def add_edge(self, source, destination, cost):
        self._graph.add_edge(source, destination, cost)
