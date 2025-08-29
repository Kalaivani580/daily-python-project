from # DateFunctions.py

from datetime import date

def is_leap_year(year: int) -> bool:
    """
    Check if a given year is a leap year.
    Returns True if leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birth_year: int, birth_month: int, birth_day: int) -> int:
    """
    Calculate age based on birthdate.
    Returns age as an integer.
    """
    today = date.today()
    age = today.year - birth_year

    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1
    
    return age

# Test the functions if file is run directly
if __name__ == "__main__":
    print("Leap year check for 2024:", is_leap_year(2024))
    print("Leap year check for 2023:", is_leap_year(2023))
    print("Age for DOB 2000-08-15:", calculate_age(2000, 8, 15))
