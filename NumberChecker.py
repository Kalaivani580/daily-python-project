import math

def is_positive(number):
    """
    Checks if a number is positive.
    Returns True if the number is greater than 0, False otherwise.
    """
    return number > 0

def is_even(number):
    """
    Checks if a number is even.
    Returns True if the number is an even integer, False otherwise.
    """
    if not isinstance(number, int):
        return False
    return number % 2 == 0

def is_prime(number):
    """
    Checks if a number is a prime number.
    Returns True if the number is prime, False otherwise.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if not isinstance(number, int):
        return False
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:  # Optimization: exclude even numbers greater than 2
        return False
    # Check for divisors from 3 up to the square root of the number, skipping even numbers
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Example Usage:
    print(f"Is 5 positive? {is_positive(5)}")       # Expected: True
    print(f"Is -3 positive? {is_positive(-3)}")     # Expected: False
    print(f"Is 0 positive? {is_positive(0)}")       # Expected: False

    print(f"Is 4 even? {is_even(4)}")             # Expected: True
    print(f"Is 7 even? {is_even(7)}")             # Expected: False
    print(f"Is 0 even? {is_even(0)}")             # Expected: True
    print(f"Is 3.5 even? {is_even(3.5)}")         # Expected: False

    print(f"Is 2 prime? {is_prime(2)}")           # Expected: True
    print(f"Is 7 prime? {is_prime(7)}")           # Expected: True
    print(f"Is 10 prime? {is_prime(10)}")         # Expected: False
    print(f"Is 1 prime? {is_prime(1)}")           # Expected: False
    print(f"Is 0 prime? {is_prime(0)}")           # Expected: False
    print(f"Is -5 prime? {is_prime(-5)}")         # Expected: False
    print(f"Is 11.5 prime? {is_prime(11.5)}")     # Expected: False
