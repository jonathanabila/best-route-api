from unittest import TestCase

from src.exceptions.invalid_edges import InternalException, InvalidEdges


class TestInvalidEdges(TestCase):
    def test_invalid_edges(self):
        self.assertTrue(issubclass(InvalidEdges, InternalException))

        with self.assertRaises(InvalidEdges):
            raise InvalidEdges("message")

        self.assertEqual(repr(InvalidEdges("message")), "message")
