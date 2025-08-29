# InitialExtractor.py

def extract_initials(full_name):
    """
    Extracts and returns the uppercase initials from a full name.
    Example: "kalai udhaya" → "KU"
    """
    if not full_name.strip():
        return ""

    parts = full_name.strip().split()
    initials = ''.join(part[0].upper() for part in parts if part)
    return initials

# Run directly
if __name__ == "__main__":
    name = input("Enter full name: ")
    print("Initials:", extract_initials(name))
