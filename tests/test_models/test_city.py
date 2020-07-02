#!/usr/bin/python
"""Tests Base Model"""
import unittest
from models.city import City
import pep8


class Test_City(unittest.TestCase):
    """test 1"""

    def test_1(self):
        """Test objs"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_2(self):
        """Test type"""
        city = City()
        self.assertEqual(type(city.name), str)
        self.assertEqual(type(city.state_id), str)

    """def test_3(self):
        Test isinstance
        city = City
        self.assertIsInstance(city, City)
    """

    def test_4(self):
        """Test doc"""
        self.assertIsNotNone(City.__doc__)

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
