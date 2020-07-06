#!/usr/bin/python
"""
Tests Base Model
"""
import unittest
from models.base_model import BaseModel
import pep8


class Test_Base(unittest.TestCase):
    """test 1"""

    def setUp(self):
        """sets up"""
        self.baseModel = BaseModel()

    def test_method(self):
        """Test methods"""
        self.assertTrue(hasattr(self.baseModel, "__init__"))
        self.assertTrue(hasattr(self.baseModel, "save"))
        self.assertTrue(hasattr(self.baseModel, "to_dict"))

    def test_doc(self):
        """Test docs"""
        self.assertIsNotNone(self.baseModel.__doc__)
        self.assertIsNotNone(self.baseModel.save.__doc__)
        self.assertIsNotNone(self.baseModel.to_dict.__doc__)

    def test_save(self):
        """Test save"""
        pass

    """def test_objects(self):
        Test to_dict
        self.assertTrue(type(self.baseModel.__objects),type([]))
    """

    def test_to_dict(self):
        """Test to_dict"""
        self.assertTrue(type(self.baseModel.to_dict()),type({}))

    def test_val(self):
        """attributes"""
        self.baseModel.name = "Holberton"
        self.baseModel.my_number = 89
        self.baseModel.save()

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
