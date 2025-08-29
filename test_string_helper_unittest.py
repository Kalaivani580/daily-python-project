import unittest
# Import the functions you want to test from your StringHelper.py file
from StringHelper import capitalize_string, reverse_string, count_characters

class TestStringHelper(unittest.TestCase):
    """
    Test suite for StringHelper functions using unittest framework.
    """

    # --- Tests for capitalize_string ---
    def test_capitalize_string_basic(self):
        """Test with a standard multi-word string."""
        self.assertEqual(capitalize_string("hello world"), "Hello World")

    def test_capitalize_string_single_word(self):
        """Test with a single word."""
        self.assertEqual(capitalize_string("python"), "Python")

    def test_capitalize_string_empty(self):
        """Test with an empty string."""
        self.assertEqual(capitalize_string(""), "")

    def test_capitalize_string_with_numbers(self):
        """Test with numbers and letters."""
        self.assertEqual(capitalize_string("123 test python"), "123 Test Python")

    def test_capitalize_string_mixed_case(self):
        """Test with a string that already has mixed casing."""
        self.assertEqual(capitalize_string("PyThOn PrOgRaMmInG"), "Python Programming")

    def test_capitalize_string_leading_trailing_spaces(self):
        """Test with leading/trailing spaces."""
        self.assertEqual(capitalize_string("  leading and trailing  "), "  Leading And Trailing  ")

    def test_capitalize_string_punctuation(self):
        """Test with punctuation."""
        self.assertEqual(capitalize_string("hello, world!"), "Hello, World!")

    def test_capitalize_string_non_string_input_raises_typeerror(self):
        """Test that non-string inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            capitalize_string(123)
        with self.assertRaises(TypeError):
            capitalize_string(None)
        with self.assertRaises(TypeError):
            capitalize_string(['a', 'b'])
        with self.assertRaises(TypeError):
            capitalize_string(5.5)

    # --- Tests for reverse_string ---
    def test_reverse_string_basic(self):
        """Test basic string reversal."""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_palindrome(self):
        """Test a string that is a palindrome."""
        self.assertEqual(reverse_string("madam"), "madam")

    def test_reverse_string_empty(self):
        """Test with an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_with_numbers_and_symbols(self):
        """Test with a string containing numbers and special characters."""
        self.assertEqual(reverse_string("123!@#"), "#@!321")

    def test_reverse_string_long_string(self):
        """Test with a longer string."""
        self.assertEqual(reverse_string("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")

    def test_reverse_string_non_string_input_raises_typeerror(self):
        """Test that non-string inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(None)
        with self.assertRaises(TypeError):
            reverse_string(True)

    # --- Tests for count_characters ---
    def test_count_characters_basic(self):
        """Test basic character counting."""
        self.assertEqual(count_characters("hello"), 5)

    def test_count_characters_empty(self):
        """Test with an empty string."""
        self.assertEqual(count_characters(""), 0)

    def test_count_characters_with_spaces(self):
        """Test counting characters including spaces."""
        self.assertEqual(count_characters("hello world"), 11)

    def test_count_characters_with_numbers_and_symbols(self):
        """Test counting characters including numbers and symbols."""
        self.assertEqual(count_characters("abc123!@#"), 9)

    def test_count_characters_long_string(self):
        """Test counting characters in a longer string."""
        self.assertEqual(count_characters("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_count_characters_non_string_input_raises_typeerror(self):
        """Test that non-string inputs raise a TypeError."""
        with self.assertRaises(TypeError):
            count_characters(123)
        with self.assertRaises(TypeError):
            count_characters(None)
        with self.assertRaises(TypeError):
            count_characters({'key': 'value'})

if __name__ == '__main__':
    unittest.main()
