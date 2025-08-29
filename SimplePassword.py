# SimplePassword.py

def is_valid_password(password, min_length=8):
    """
    Check if the password meets the minimum length requirement.
    
    Args:
        password (str): The password to validate.
        min_length (int): The minimum required length for the password.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    return len(password) >= min_length


def main():
    password = input("Enter your password: ")
    
    if is_valid_password(password):
        print("✅ Password is valid.")
    else:
        print("❌ Password is too short. It must be at least 8 characters long.")


if __name__ == "__main__":
    main()
