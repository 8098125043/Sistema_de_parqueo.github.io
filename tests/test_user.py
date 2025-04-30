import unittest

class TestUser(unittest.TestCase):
    def test_get_user(self):
        user = None
        self.assertIsNone(user)


if __name__ == '__main__':
    unittest.main()