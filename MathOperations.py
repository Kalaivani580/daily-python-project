import math

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    n! = n * (n-1) * ... * 1
    0! = 1
    Raises TypeError if n is not an integer.
    Raises ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def power(base, exponent):
    """
    Calculates the base raised to the power of the exponent.
    Uses the built-in pow() function for robust handling of various types.
    """
    return pow(base, exponent)

def square_root(n):
    """
    Calculates the square root of a non-negative number.
    Returns a float.
    Raises TypeError if n is not a number.
    Raises ValueError if n is negative.
    """
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number (integer or float).")
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    return math.sqrt(n)

if __name__ == "__main__":
    # Example Usage when running this file directly
    print("--- Factorial ---")
    print(f"Factorial of 5: {factorial(5)}")   # Expected: 120
    print(f"Factorial of 0: {factorial(0)}")   # Expected: 1
    # You can uncomment these to see the errors when running directly
    # try:
    #     print(f"Factorial of -3: {factorial(-3)}")
    # except (ValueError, TypeError) as e:
    #     print(f"Error: {e}")

    print("\n--- Power ---")
    print(f"2 to the power of 3: {power(2, 3)}")     # Expected: 8
    print(f"10 to the power of -2: {power(10, -2)}") # Expected: 0.01

    print("\n--- Square Root ---")
    print(f"Square root of 9: {square_root(9)}")       # Expected: 3.0
    print(f"Square root of 2: {square_root(2)}")       # Expected: 1.414...
