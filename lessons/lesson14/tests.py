import unittest
from user import User

class UserTests(unittest.TestCase):

    def test_create_user(self):
        user = User("99", "L", "test@gmail.com","25", "Ukr")
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.user_id, int)
        self.assertIsInstance(user.age, int)

    def test_set_int_age(self):
        user = User("99", "L", "test@gmail.com","25", "Ukr")
        user.age = 152
        self.assertIsInstance(user.age, int)
        self.assertEqual(user.age, 152)
    def test_set_str_age(self):
        user = User("99", "L", "test@gmail.com","25", "Ukr")
        user.age = "152"
        self.assertIsInstance(user.age, int)
        self.assertEqual(user.age, 152)


if __name__ == "__main__":
    unittest.main()