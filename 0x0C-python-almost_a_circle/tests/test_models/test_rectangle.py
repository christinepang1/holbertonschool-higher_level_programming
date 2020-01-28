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
        r1 = Rectangle(12, 13, 14, 15)
        self.assertEqual(issubclass(Rectangle, Base), True)
        self.assertEqual(type(r), Rectangle)
        self.assertEqual((r.width, r.height, r.x, r.y), (12, 13, 0, 0))
        self.assertEqual(type(r1), Rectangle)
        self.assertEqual(type(r.width), int)
        self.assertEqual(type(r.height), int)

    def test_id(self):
        """Tests id"""
        r = Rectangle(12, 13)
        r1 = Rectangle(2, 3)
        self.assertEqual(r.id, 5)
        self.assertEqual(r1.id, 6)

if __name__ == '__main__':
    unittest.main()
