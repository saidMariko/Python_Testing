import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app 

class TestShowSummaryNoEmail(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_showSummary_no_email(self):
        response = self.client.post('/showSummary', data={}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('index.html')


if __name__ == '_main_':
    unittest.main()