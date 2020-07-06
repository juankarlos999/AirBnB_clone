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

    def setUp(self):
        """ setup"""
        self.hbnbCommand = HBNBCommand()
        self.hbnbCommand2 = BaseModel()

    def test_create(self):
        """test create"""
        self.hbnbCommand.do_create(self.hbnbCommand2.to_dict()['__class__'])

    def test_show(self):
        """test show"""
        cls = self.hbnbCommand2.to_dict()['__class__']
        _id = self.hbnbCommand2.id
        self.hbnbCommand.do_show(cls+' '+_id)

    def test_destroy(self):
        """test destrooy"""
        cls = self.hbnbCommand2.to_dict()['__class__']
        _id = self.hbnbCommand2.id
        self.hbnbCommand.do_destroy(cls+' '+_id)

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
