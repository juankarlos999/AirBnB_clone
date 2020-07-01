#!/usr/bin/python
"""Tests Base Model"""
import unittest
from models.amenity import Amenity
import pep8


class Test_Amenity(unittest.TestCase):
    """test 1"""
    amenity = Amenity()

    def test_1(self):
        """test"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_2(self):
        """test type"""
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

    def test_3(self):
        """test isinstance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_4(self):
        """Test documentation"""
        amenity = Amenity()
        self.assertIsNotNone(Amenity.__doc__)


if __name__ == '__main__':
    unittest.main()
