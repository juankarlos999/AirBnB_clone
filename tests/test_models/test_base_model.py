#!/usr/bin/python
"""Tests Base Model"""
import unittest
from models.base_model import BaseModel
# import pep8


class Test_Base(unittest.TestCase):
    """test 1"""
    model = BaseModel()

    def setUp(self):
        """sets up"""
        pass

    def test_method(self):
        """Test methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_doc(self):
        """Test docs"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        """Test save"""
        pass

    def test_val(self):
        """attributes"""
        self.model.name = "Holberton"
        self.model.my_number = 89
        self.model.save()

    """def test_pep8(self):
        pep8
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    """

if __name__ == '__main__':
    unittest.main()
