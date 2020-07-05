#!/usr/bin/python3
"""
Test FileStorage
"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import pep8


class test_FileStorage(unittest.TestCase):
    """Test file storage"""

    def test_all(self):
        """test all"""
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    """def test_objects(self):
        tests __objects
        FileStore.__FileStorage__objects = {}
    """

    def test_reload(self):
        """Tests reload"""
        self.assertEqual(list, type(FileStorage.__objects))

    def test_reload(self):
        """Tests reload"""
        pass

    def test_save(self, obj=None):
        """Tests reload"""
        pass

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
