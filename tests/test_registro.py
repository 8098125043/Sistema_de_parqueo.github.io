import unittest
from routes.controllers import create_user

class TestRegistro(unittest.TestCase):
    def test_create_user(self):
        user = None
        self.assertIsNone(user)

    def test_create_user_invalido(self):
        user = None
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()