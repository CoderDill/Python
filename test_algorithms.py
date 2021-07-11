from unittest import TestCase
from fun import reverse_str, is_palindrome, factorial


class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str("hello"), "olleh")

    def test_is_palindrom(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertRaises(ValueError, factorial, -5)