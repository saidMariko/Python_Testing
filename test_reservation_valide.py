import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app 

class TestPurchasePlacesValidReservation(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_valid_reservation(self):
        response = self.client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('welcome.html')

if __name__ == '_main_':
    unittest.main()