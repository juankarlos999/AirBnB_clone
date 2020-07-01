#!/usr/bin/python
"""Tests State"""
import unittest
from models.state import State
# import pep8


class Test_State(unittest.TestCase):
    """test 1"""

    def test_1(self):
        """Test attr"""
        state = State
        self.assertTrue(hasattr(State, "name"))

    def test_doc(self):
        """Test docs"""
        self.assertIsNotNone(State.__doc__)

    """def test_2(self):
        Test isinstance
        state = State
        self.assertIsInstance(state, State)
    """

    """def test_pep8(self):
        pep8
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    """

if __name__ == '__main__':
    unittest.main()
