import unittest
from app import app  # Remplacez 'your_flask_app' par le nom de votre application Flask

class TestBookContent(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_book_content(self):
        response = self.app.get('/book/CAN/Iron Temple')  # Remplacez 'competition_name' et 'club_name' par des valeurs valides
if __name__ == '_main_':
    unittest.main()