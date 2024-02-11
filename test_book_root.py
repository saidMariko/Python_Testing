import unittest
from app import app  # Remplacez 'your_flask_app' par le nom de votre application Flask

class TestBookRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_book_route(self):
        response = self.app.get('/book/competition_name/club_name')  # Remplacez 'competition_name' et 'club_name' par des valeurs valides
        self.assertEqual(response.status_code, 200)

if __name__ == '_main_':
    unittest.main()