import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from app import app  # Remplacez 'your_flask_app' par le nom de votre fichier d'application Flask

class TestPurchasePlacesNoCompetition(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_no_competition(self):
        response = self.client.post('/purchasePlaces', data={'club': 'Iron Temple', 'places': '4'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '_main_':
    unittest.main()