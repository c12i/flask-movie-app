import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        """
         method that creates an instance of our User class
        """
        self.new_user = User(password = "banana")

    def test_password_setter(self):
        """
         ascertains that when password is being hashed and the pass_secure contains a value
        """
        self.assertTrue(self.new_user.password_hash is not None)
    
    def test_no_access_password(self):
        """
         confirms that our application raises an AttributeError when we try and access the password property
        """
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        """
        confirms that our password_hash can be verified when we pass in the correct password.
        """
        self.assertTrue(self.new_user.verify_password('banana'))