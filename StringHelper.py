def capitalize_string(text):
    """
    Capitalizes the first letter of each word in a given string.
    Uses the string's .title() method.
    Raises TypeError if input is not a string.
    Returns the capitalized string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text.title()

def reverse_string(text):
    """
    Reverses a given string.
    Uses slicing [::-1] for efficient reversal.
    Raises TypeError if input is not a string.
    Returns the reversed string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text[::-1]

def count_characters(text):
    """
    Counts the total number of characters in a given string.
    Uses the built-in len() function.
    Raises TypeError if input is not a string.
    Returns the character count as an integer.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return len(text)

if __name__ == "__main__":
    # Example Usage:
    print("--- Capitalize String ---")
    print(f"'hello world' capitalized: {capitalize_string('hello world')}")
    print(f"'python programming' capitalized: {capitalize_string('python programming')}")
    print(f"'  leading spaces' capitalized: {capitalize_string('  leading spaces')}")
    print(f"'NUMBERS 123' capitalized: {capitalize_string('NUMBERS 123')}")

    print("\n--- Reverse String ---")
    print(f"'hello' reversed: {reverse_string('hello')}")
    print(f"'Python' reversed: {reverse_string('Python')}")
    print(f"'12345' reversed: {reverse_string('12345')}")
    print(f"'' reversed: {reverse_string('')}")

    print("\n--- Count Characters ---")
    print(f"Character count of 'hello': {count_characters('hello')}")
    print(f"Character count of 'Python is fun': {count_characters('Python is fun')}")
    print(f"Character count of '': {count_characters('')}")
    print(f"Character count of ' spaces ': {count_characters(' spaces ')}")
