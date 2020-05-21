# Thanks to Maria Boldyreva
# https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc

from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float("inf")
Edge = namedtuple("Edge", "start, end, cost")


def make_edge(start, end, cost):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) != 3]
        if wrong_edges:
            raise ValueError("Wrong edges data: {}".format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    @staticmethod
    def get_node_pairs(n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError("Edge {} {} already exists".format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        vertices = self.vertices.copy()
        neighbours = self.neighbours.copy()

        assert source in vertices, "Such source node doesn't exist"

        distances = {vertex: inf for vertex in vertices}
        previous_vertices = {vertex: None for vertex in vertices}
        distances[source] = 0

        while vertices:
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        final_distance = 0
        while current_vertex:
            path.appendleft(current_vertex)

            for neighbour in neighbours[current_vertex]:
                if neighbour[0] == path[1]:
                    final_distance += neighbour[1]
                    break

            current_vertex = previous_vertices[current_vertex]

        return path, final_distance
