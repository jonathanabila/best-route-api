from unittest import TestCase

from src.exceptions.internal_exception import InternalException


class TestInternalException(TestCase):
    def test_internal_exception(self):
        self.assertTrue(issubclass(InternalException, Exception))

        with self.assertRaises(InternalException):
            raise InternalException()
