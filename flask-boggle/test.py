from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_boggle(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertIn(
                "<h1>Boggle!</h1>", html)
