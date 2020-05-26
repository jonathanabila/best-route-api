from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.services.file import File


class TestFile(TestCase):
    def test__path_to_file(self):
        File._path_to_file("../dist/file_path").endswith("/dist/file_path")

    def test_convert_to_integer(self):
        self.assertListEqual(File._convert_to_integer(["a", "b", "c"]), ["a", "b", "c"])
        self.assertListEqual(File._convert_to_integer(["a", "b", 1]), ["a", "b", 1])

    def test_parse_file(self):
        self.assertListEqual(File._parse_file(["A,B,C\n"], ","), [["A", "B", "C"]])

    @patch("src.services.file.File._path_to_file")
    @patch("builtins.open")
    def test_read_file(self, mock_open, mock_path):
        mock_open.return_value.__enter__.return_value.readlines.return_value = "mock"
        mock_path.return_value = "path_file"

        self.assertEqual(File().read_file("file_path"), "mock")

        mock_path.assert_called_with("file_path")

    @patch("src.services.file.File.read_file")
    def test_get_file_content(self, mock_read_file):
        mock_read_file.return_value = ["A,B,C\n", "A,B,1\n"]

        self.assertEqual(
            File().get_file_content("file_name"), [["A", "B", "C"], ["A", "B", 1]]
        )
        mock_read_file.assert_called_with("file_name")

    @patch("src.services.file.File._path_to_file", MagicMock())
    @patch("builtins.open")
    def test_add_line(self, mock_open):
        self.assertIsNone(File().add_line("line", "file_name"))
        mock_open.return_value.__enter__.return_value.write.assert_called_with("line\n")
