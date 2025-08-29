# EmailUsername.py

def extract_username(email):
    if '@' in email:
        return email.split('@')[0]
    else:
        return "Invalid email address"

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your email address: ")
    username = extract_username(user_input)
    print("Username:", username)

