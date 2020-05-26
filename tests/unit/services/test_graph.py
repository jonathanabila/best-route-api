from unittest import TestCase
from collections import deque

from src.services.graph import Graph, make_edge
from exceptions.invalid_node import InvalidNode
from exceptions.invalid_edges import InvalidEdges


class TestGraph(TestCase):
    def setUp(self) -> None:
        self.raw_edges = [("A", "B", 1), ("A", "C", 1)]
        self.graph = Graph(self.raw_edges)

    def test_init_(self):
        with self.assertRaises(InvalidEdges) as cm:
            Graph([("A", "B")])
        self.assertEqual(cm.exception.code, 1)

    def test_vertices(self):
        self.assertEqual(self.graph.vertices, {"A", "B", "C"})

    def test_get_node_pairs(self):
        self.assertEqual(self.graph.get_node_pairs("A", "B"), [["A", "B"], ["B", "A"]])
        self.assertEqual(self.graph.get_node_pairs("A", "B", False), [["A", "B"]])

    def test_remove_edge(self):
        self.assertIsNone(self.graph.remove_edge("A", "B"))
        self.assertListEqual(self.graph.edges, [make_edge("A", "C", 1)])

    def test_add_edge(self):
        self.assertIsNone(self.graph.add_edge("A", "D", 1))

        self.assertListEqual(
            self.graph.edges,
            [make_edge(*i) for i in [*self.raw_edges, ("A", "D", 1), ("D", "A", 1)]],
        )

        with self.assertRaises(InvalidNode) as cm:
            self.graph.add_edge("A", "D", 1)
        self.assertEqual(cm.exception.code, 2)

    def test_add_edge_both_end_false(self):
        self.assertIsNone(self.graph.add_edge("A", "E", 1, both_ends=False))
        self.assertListEqual(
            self.graph.edges, [make_edge(*i) for i in [*self.raw_edges, ("A", "E", 1)]],
        )

    def test_neighbours(self):
        self.assertEqual(
            self.graph.neighbours, {"A": {"B": 1, "C": 1}, "B": {"A": 1}, "C": {"A": 1}}
        )

    def test_dijsktra(self):
        with self.assertRaises(InvalidNode) as cm:
            self.graph.dijkstra("F", "B")
        self.assertEqual(cm.exception.code, 3)

        with self.assertRaises(InvalidNode) as cm:
            self.graph.dijkstra("A", "F")
        self.assertEqual(cm.exception.code, 4)

        self.assertEqual(self.graph.dijkstra("A", "B"), (deque(["A", "B"]), 1))

        self.graph.add_edge("F", "G", 1)
        with self.assertRaises(InvalidNode) as cm:
            self.graph.dijkstra("A", "F")
        self.assertEqual(cm.exception.code, 5)
