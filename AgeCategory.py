# AgeCategory.py

def categorize_age(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Main program
if __name__ == "__main__":
    try:
        age_input = int(input("Enter your age: "))
        category = categorize_age(age_input)
        print(f"You are a: {category}")
    except ValueError:
        print("Please enter a valid number for age.")
