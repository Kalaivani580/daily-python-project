# test_initial_extractor.py

import unittest
import sys
import os

# ✅ Add the current folder to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from InitialExtractor import extract_initials

class TestInitialExtractor(unittest.TestCase):
    def test_regular_name(self):
        self.assertEqual(extract_initials("Kalai Udhaya"), "KU")

    def test_extra_spaces(self):
        self.assertEqual(extract_initials("  Elon   Musk  "), "EM")

    def test_empty_input(self):
        self.assertEqual(extract_initials(""), "")

    def test_single_name(self):
        self.assertEqual(extract_initials("Madonna"), "M")

    def test_lowercase_name(self):
        self.assertEqual(extract_initials("kalai udhaya"), "KU")

if __name__ == "__main__":
    unittest.main()
