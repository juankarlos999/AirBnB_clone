#!/usr/bin/python3
"""
Test Console
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models import storage
from models.user import User
import unittest
import pep8
from console import HBNBCommand


class Test_Console(unittest.TestCase):
    """
    Tests console
    """

    def test_pep8(self):
        """
        Pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """
        documentation
        """
        self.assertIsNotNone(HBNBCommand.__doc__)

    """def test_type(self):
        type method
        Console = HBNBCommand()
        self.assertEqual(type(Console), str)
    """

if __name__ == '__main__':
    unittest.main()
