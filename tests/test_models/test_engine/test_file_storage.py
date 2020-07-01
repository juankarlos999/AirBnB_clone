#!/usr/bin/python3
"""
Test FileStorage
"""


import unittest
from models.base_model import BaseModel
from models import storage


class test_FileStorage(unittest.TestCase):
    """Test file storage"""

    def test_all(self):
        """test all"""
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

if __name__ == '__main__':
    unittest.main()
