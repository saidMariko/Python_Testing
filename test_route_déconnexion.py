import unittest
from app import app  

class TestLogoutRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_logout_route(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '_main_':
    unittest.main()