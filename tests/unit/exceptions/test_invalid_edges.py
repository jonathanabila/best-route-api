from unittest import TestCase

from src.exceptions.invalid_edges import InternalException, InvalidEdges


class TestInvalidEdges(TestCase):
    def test_invalid_edges(self):
        self.assertTrue(issubclass(InvalidEdges, InternalException))

        with self.assertRaises(InvalidEdges) as cm:
            raise InvalidEdges("99999:message")
        self.assertEqual(cm.exception.code, 99999)

        with self.assertRaises(InvalidEdges) as cm:
            raise InvalidEdges("message")
        self.assertEqual(cm.exception.code, 500)

        self.assertEqual(repr(InvalidEdges("message")), "message")
