#!/usr/bin/python
"""Tests Review"""
import unittest
from models.review import Review
import pep8


class Test_Review(unittest.TestCase):
    """test 1"""

    def Test_1(self):
        """Test attribute"""
        review = Review
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_doc(self):
        """Test docs"""
        self.assertIsNotNone(Review.__doc__)

    def test_2(self):
        """ Test Type"""
        review = Review
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(type(review.text), str)

    def test_pep8(self):
        """pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
