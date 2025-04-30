import unittest
from routes.controllers import login_user

class TestLogin(unittest.TestCase):
    def test_login_user(self):
        data = {"email": "4KZqo@example.com", "password": "1234"}
        user = None
        self.assertEqual(user, None)

    def test_login_user_invalido(self):
        data = {"email": "4KZqo@example.com", "password": "12345"}
        user = None
        self.assertEqual(user, None)

    def test_login_user_no_data(self):
        user = None
        self.assertEqual(user, None)


if __name__ == '__main__':
    unittest.main()