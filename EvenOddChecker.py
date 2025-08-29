# EvenOddChecker.py

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Check a single number
num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}")

# Check a list of numbers
number_list = [10, 15, 23, 42, 8, 9, 100]
print("\nChecking list of numbers:")
for n in number_list:
    result = check_even_odd(n)
    print(f"{n} is {result}")
