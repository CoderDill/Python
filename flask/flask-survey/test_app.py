from werkzeug.wrappers import response
from app import app, CURRENT_SURVEY_KEY
from flask import session
from unittest import TestCase


class ColorViewsTestCase(TestCase):
    def test_color_form(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<h3>Welcome</h3>", html)

    def test_pick_survey(self):
        with app.test_client() as client:
            res = client.post("/", data={"survey_code": "satisfaction"})
            html = res.get_data(as_text=True)

            self.assertIn("<h1>Customer Satisfaction Survey</h1>", html)

    def test_start(self):
        with app.test_client() as client:
            res = client.post("/start")

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, "http://localhost/questions/0")

    def test_start_followed(self):
        with app.test_client() as client:
            res = client.post(
                "/start", data={"current_survey": "satisfaction"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertIn("<h1>Redirecting...</h1>", html)

    def test_session(self):
        with app.test_client() as client:
            # with client.session_transaction() as change_seesion: IF YOU WANT TO CHANGE SESSION, THEN TEST
            # change_seesion[CURRENT_SURVEY_KEY, 'satisfaction']
            res = client.post("/", data={"survey_code": "satisfaction"})

            self.assertEqual(session[CURRENT_SURVEY_KEY], "satisfaction")
