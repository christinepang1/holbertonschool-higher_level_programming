#!/usr/bin/python3
"""Unittesting for Class Rectangle"""

import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test Class Rectangle"""

    def test_base(self):
        """Test if inherits"""
        r = Rectangle(12, 13)
        self.assertEqual(issubclass(Rectangle, Base), True)

if __name__ == '__main__':
    unittest.main()
