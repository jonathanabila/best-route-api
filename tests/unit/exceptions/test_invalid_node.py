from unittest import TestCase

from src.exceptions.invalid_node import InternalException, InvalidNode


class TestInvalidNode(TestCase):
    def test_invalid_node(self):
        self.assertTrue(issubclass(InvalidNode, InternalException))

        with self.assertRaises(InvalidNode):
            raise InvalidNode("message")

        self.assertEqual(repr(InvalidNode("message")), "message")
