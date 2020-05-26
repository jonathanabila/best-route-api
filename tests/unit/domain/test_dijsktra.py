from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.domain.dijsktra import Dijsktra


class TestDijsktra(TestCase):
    @patch("src.domain.dijsktra.Dijsktra.parse_edger", MagicMock())
    @patch("src.domain.dijsktra.Graph", MagicMock())
    def setUp(self) -> None:
        self.dijsktra = Dijsktra("edges")

    def test_parse_edger(self):
        self.assertEqual(
            self.dijsktra.parse_edger(["C", "C", "M"]), [("C",), ("C",), ("M",)]
        )

    def test_calculate(self):
        self.dijsktra._graph.dijkstra.return_value = ["source", "destination"], 1
        self.assertEqual(
            self.dijsktra.calculate("source", "destination"),
            ("source - destination", 1),
        )
        self.dijsktra._graph.dijkstra.assert_called_with("source", "destination")

    def test_add_edge(self):
        self.assertIsNone(self.dijsktra.add_edge("source", "destination", 1))
        self.dijsktra._graph.add_edge.assert_called_with("source", "destination", 1)
