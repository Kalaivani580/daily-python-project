# ConversionFunctions.py

# Convert feet to meters
def feet_to_meters(feet):
    """Convert feet to meters"""
    return feet * 0.3048

# Convert meters to feet
def meters_to_feet(meters):
    """Convert meters to feet"""
    return meters / 0.3048

# Convert pounds to kilograms
def pounds_to_kg(pounds):
    """Convert pounds to kilograms"""
    return pounds * 0.45359237

# Convert kilograms to pounds
def kg_to_pounds(kg):
    """Convert kilograms to pounds"""
    return kg / 0.45359237


# Run this part only if the script is executed directly
if __name__ == "__main__":
    print("ConversionFunctions.py - Unit Conversion Examples")
    print("10 feet = ", feet_to_meters(10), "meters")
    print("3 meters = ", meters_to_feet(3), "feet")
    print("150 pounds = ", pounds_to_kg(150), "kg")
    print("70 kg = ", kg_to_pounds(70), "pounds")

# ConversionFunctions.py

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def pounds_to_kg(pounds):
    return pounds * 0.45359237

def kg_to_pounds(kg):
    return kg / 0.45359237


if __name__ == "__main__":
    print("ConversionFunctions.py - Unit Conversion Program")

    choice = input("Choose conversion (1=feet→meters, 2=meters→feet, 3=pounds→kg, 4=kg→pounds): ")

    if choice == "1":
        feet = float(input("Enter feet: "))
        print(f"{feet} feet = {feet_to_meters(feet)} meters")
    elif choice == "2":
        meters = float(input("Enter meters: "))
        print(f"{meters} meters = {meters_to_feet(meters)} feet")
    elif choice == "3":
        pounds = float(input("Enter pounds: "))
        print(f"{pounds} pounds = {pounds_to_kg(pounds)} kg")
    elif choice == "4":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg = {kg_to_pounds(kg)} pounds")
    else:
        print("Invalid choice")
