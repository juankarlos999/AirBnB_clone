#!/usr/bin/python
"""Tests Base Model"""
import unittest
from models.base_model import BaseModel
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_Base(unittest.TestCase):
    """test 1"""
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

if __name__ == '__main__':
    unittest.main()
