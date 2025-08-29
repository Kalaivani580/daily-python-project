import pytest
from NumberChecker import is_positive, is_even, is_prime

# --- Tests for is_positive ---
def test_is_positive_positive_number():
    assert is_positive(10) == True

def test_is_positive_negative_number():
    assert is_positive(-5) == False

def test_is_positive_zero():
    assert is_positive(0) == False

# --- Tests for is_even ---
def test_is_even_even_number():
    assert is_even(4) == True

def test_is_even_odd_number():
    assert is_even(7) == False

def test_is_even_zero():
    assert is_even(0) == True

def test_is_even_negative_even_number():
    assert is_even(-6) == True

def test_is_even_negative_odd_number():
    assert is_even(-3) == False

def test_is_even_float():
    assert is_even(2.0) == False # Floats are not considered even/odd integers
    assert is_even(3.5) == False

def test_is_even_string():
    assert is_even("abc") == False

# --- Tests for is_prime ---
def test_is_prime_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True

def test_is_prime_non_prime_numbers():
    assert is_prime(1) == False # Not prime by definition
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(15) == False

def test_is_prime_zero_and_negatives():
    assert is_prime(0) == False
    assert is_prime(-2) == False
    assert is_prime(-10) == False

def test_is_prime_float():
    assert is_prime(7.0) == False # Floats are not considered prime
    assert is_prime(11.5) == False

def test_is_prime_large_prime():
    assert is_prime(997) == True # A larger prime number

def test_is_prime_large_composite():
    assert is_prime(1000) == False
