from unittest import TestCase

from src.exceptions.invalid_node import InternalException, InvalidNode


class TestInvalidNode(TestCase):
    def test_invalid_node(self):
        self.assertTrue(issubclass(InvalidNode, InternalException))

        with self.assertRaises(InvalidNode) as cm:
            raise InvalidNode("99999:message")
        self.assertEqual(cm.exception.code, 99999)

        with self.assertRaises(InvalidNode) as cm:
            raise InvalidNode("message")
        self.assertEqual(cm.exception.code, 400)

        self.assertEqual(repr(InvalidNode("message")), "message")
