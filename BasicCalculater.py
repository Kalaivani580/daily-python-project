# BasicCalculater.py

# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask the user to choose an operation
print("Choose operation: +  -  *  /")
operation = input("Enter operation: ")

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operation selected."

# Show the result
print("Result:", result)
