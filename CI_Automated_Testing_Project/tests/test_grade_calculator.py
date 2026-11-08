"""Automated unit tests for grade_calculator.py."""

import unittest
from grade_calculator import calculate_average, has_passed, letter_grade


class TestGradeCalculator(unittest.TestCase):
    def test_average_normal(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_average_single_grade(self):
        self.assertEqual(calculate_average([75]), 75)

    def test_average_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_average_invalid_grade(self):
        with self.assertRaises(ValueError):
            calculate_average([50, 120])

    def test_pass_boundary(self):
        self.assertTrue(has_passed(50))

    def test_fail_boundary(self):
        self.assertFalse(has_passed(49.9))

    def test_letter_grade_a(self):
        self.assertEqual(letter_grade(95), "A")

    def test_letter_grade_b(self):
        self.assertEqual(letter_grade(85), "B")

    def test_letter_grade_f(self):
        self.assertEqual(letter_grade(40), "F")

    def test_letter_grade_invalid(self):
        with self.assertRaises(ValueError):
            letter_grade(101)


if __name__ == "__main__":
    unittest.main()
