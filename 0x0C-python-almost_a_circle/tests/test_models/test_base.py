#!/usr/bin/python3
"""Unittest for Class Base"""


import unittest
import json
from models import base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Class Base"""

    def test_id(self):
        """Tests id"""
        a = Base()
        b = Base()
        c = Base(4)
        d = Base(-12)
        e = Base(-21.3)
        f = Base(0)
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 4)
        self.assertEqual(d.id, -12)
        self.assertEqual(e.id, -21.3)
        self.assertEqual(f.id, 0)
        self.assertEqual(type(f), Base)

    def test_json_string(self):
        """Test conversion"""
        a = Base.to_json_string([])
        b = Base.to_json_string([{'x': 2}])
        c1 = [{'x': 2}]
        c2 = Base.to_json_string(c1)
        self.assertEqual(a, "[]")
        self.assertEqual(b, '[{"x": 2}]')
        self.assertEqual(Base.from_json_string(c2), c1)


if __name__ == '__main__':
    unittest.main()
