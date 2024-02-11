import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app 

class TestShowSummaryInvalidEmail(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_showSummary_invalid_email(self):
        response = self.client.post('/showSummary', data={'email': 'invalid@email.com'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')

if __name__ == '_main_':
    unittest.main()