import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(isinstance(user.id, str))
        self.assertTrue(isinstance(user.created_at, datetime))
        self.assertTrue(isinstance(user.updated_at, datetime))

if __name__ == "__main__":
    unittest.main()