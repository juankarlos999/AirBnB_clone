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

    def test_objects(self):
        """tests __objects"""
        obj = storage.all()
        self.assertNotEqual(type(obj), type([]))

    def test_reload(self):
        """Tests reload"""
        new_object = storage.all()
        self.assertEqual(type(new_object), type({}))

    def test_new(self):
        """Test new"""
        new_ = FileStorage()
        var_ = BaseModel()
        new_.new(var_)
        key_ = var_.to_dict()['__class__'] + '.' + var_.id
        self.assertTrue(new_.all()[key_].id, var_.id)

    def reload(self):
        """Tests reload"""
        pass

    def save(self):
        """Tests save"""
        pass

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
