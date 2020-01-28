#!/usr/bin/python3
"""Unittesting for Class Square"""

import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test Class Square"""

    def setUp(self):
        """Resets objects"""
        Base._Base__nb_objects = 0

    def test_base(self):
        """Test if inherits"""
        r = Square(30)
        r1 = Square(31)
        self.assertEqual(r.id, 1)
        self.assertEqual(r1.id, 2)
        self.assertEqual(issubclass(Square, Base), True)

    def test_dimensions(self):
        """Tests if int"""
        r = Square(3)
        self.assertEqual(r.width, 3)
        self.assertEqual(type(r.width), int)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.size, 3)
        r1 = Square(20, 5, 7, 7)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 7)
        self.assertEqual(r1.id, 7)

    def test_area(self):
        """Tests area"""
        r = Square(3)
        r1 = Square(9, 7, 8, 2)
        self.assertEqual(r.area(), 9)
        self.assertEqual(r1.area(), 81)

    def test_syntax(self):
        """Tests representation"""
        r = Square(9, 7, 8, 2)
        re = "[Square] ({}) {}/{} - {}".format(
                r.id, r.x, r.y, r.size)
        self.assertEqual(str(r), re)

if __name__ == '__main__':
    unittest.main()
