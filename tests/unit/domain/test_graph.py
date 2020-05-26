from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.domain.graph import Graph


class TestGraph(TestCase):
    @patch("src.domain.graph.File")
    @patch("src.domain.graph.Dijsktra.__init__")
    def setUp(self, mock_dijsktra, mock_file) -> None:
        mock_dijsktra.return_value = MagicMock()
        mock_file.return_value = MagicMock()

        mock_file.return_value.get_file_content.return_value = "file_content"
        self.assertIsInstance(Graph(), Graph)
        mock_dijsktra.assert_called_with("file_content")

        self.graph = Graph()

    @patch("src.domain.graph.FILE_PATH", "file_path")
    @patch("src.domain.graph.File")
    def test_persist_edge(self, mock_file):
        mock_file.return_value = MagicMock()
        self.assertIsNone(self.graph._persist_edge("source", "destination", 1))
        mock_file.return_value.add_line.assert_called_with(
            "source,destination,1", "file_path"
        )

    @patch("src.domain.graph.Graph._persist_edge")
    @patch("src.domain.graph.Dijsktra.add_edge")
    def test_add_edge_path(self, mock_dijsktra, mock_persist_edge):
        mock_persist_edge.return_value = MagicMock()
        self.assertIsNone(self.graph.add_edge_path("source", "destination", 1))
        mock_dijsktra.assert_called_with("source", "destination", 1)
        mock_persist_edge.assert_called_with("source", "destination", 1)
