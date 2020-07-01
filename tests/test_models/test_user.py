#!/usr/bin/python
"""Tests User"""
import unittest
from models.user import User
# import pep8


class Test_User(unittest.TestCase):
    """test 1"""

    def test_1(self):
        """Test attributes"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "__init__"))

    def test_doc(self):
        """Test docs"""
        user = User()
        self.assertIsNotNone(User.__doc__)

    def test_2(self):
        """Test type"""
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        # self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    """def test_pep8(self):
        pep8
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    """

if __name__ == '__main__':
    unittest.main()
