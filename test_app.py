import unittest
from app import App, User

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.register_user("testuser", "testpassword")

    def test_register_user(self):
        self.assertIn("testuser", self.app.users)

    def test_login(self):
        user = self.app.login("testuser", "testpassword")
        self.assertIsNotNone(user)

    def test_create_task(self):
        user = self.app.login("testuser", "testpassword")
        self.app.create_task(user, "Test Task", "This is a test task")
        tasks = self.app.get_user_tasks(user)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")

if __name__ == "__main__":
    unittest.main()
