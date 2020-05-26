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
        self.assertIsNone(Graph())
        mock_dijsktra.assert_called_with("file_content")
