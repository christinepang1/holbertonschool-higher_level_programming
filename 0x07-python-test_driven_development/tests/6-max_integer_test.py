#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_none(self):
        self.assertIs(max_integer([]), None)
        self.assertIs(max_integer(), None)
        self.assertIs(max_integer([]), None)
        self.assertIs(max_integer({}), None)

    def test_str(self):
        self.assertEqual(max_integer("Snorlax"), "x")
        self.assertEqual(max_integer(["Snorlax", "Metagross"]), "Snorlax")

    def test_none_0(self):
        self.assertIs(max_integer([0]), 0)

    def test_none_01(self):
        self.assertIs(max_integer([0, 0, 0, 0]), 0)

    def test_one(self):
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ordered_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_decreasing_positive(self):
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_unordered_positive(self):
        self.assertEqual(max_integer([89, 2, 93, 74]), 93)

    def test_unordered_negative(self):
        self.assertEqual(max_integer([-11, -22, -3423, -4]), -4)

    def test_unoredered_combo(self):
        self.assertEqual(max_integer([-91, -2, 3, 4]), 4)

    def test_ordered_flaot(self):
        self.assertEqual(max_integer([0.1, 2.2, 3.3, 4.4]), 4.4)

    def test_ordered_float_neg(self):
        self.assertEqual(max_integer([-1.9, -23.2, -83.3, -1.4]), -1.4)

    def test_equal_pos(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_equal_neg(self):
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

    def test_equal_float(self):
        self.assertEqual(max_integer([1.11, 1.11, 1.11, 1.11]), 1.11)

    def test_similar(self):
        self.assertEqual(max_integer([56.6, 55.6, 5.5, 6.5]), 56.6)

    def test_near(self):
        self.assertEqual(max_integer([89.1, 89.11, 89.111, 89.11111]), 89.11111)

    def test_array(self):
        self.assertEqual(max_integer([[1, 3, 4], [5, 7, 8]]), [5, 7, 8])

    def test_tuple(self):
        self.assertEqual(max_integer([(1, 2, 4), (5, 6, 8)]), (5, 6, 8))

    def test_bad(self):
        with self.assertRaises(TypeError):
            max_integer([54, 34, "Metagross", 27])
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
