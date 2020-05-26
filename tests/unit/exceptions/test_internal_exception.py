from unittest import TestCase

from src.exceptions.internal_exception import InternalException


class TestInternalException(TestCase):
    def test_internal_exception(self):
        self.assertTrue(issubclass(InternalException, Exception))

        with self.assertRaises(InternalException) as cm:
            raise InternalException("message", 500)
        self.assertEqual(cm.exception.code, 500)

        with self.assertRaises(InternalException) as cm:
            raise InternalException("418:message", 500)
        self.assertEqual(cm.exception.code, 418)
