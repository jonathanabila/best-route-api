from unittest import TestCase
from . import app


class TestBestRoute(TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()

    def test_get(self):
        pass

    def test_post(self):
        pass
