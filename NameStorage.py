# NameStorage.py
# Program to save names to a file and read them back

def save_names(filename):
    print("✨ Let's save some names! (Type 'done' to finish)")
    with open(filename, 'w') as file:
        while True:
            name = input("Enter a name: ")
            if name.lower() == 'done':
                break
            file.write(name + '\n')
    print("✅ All names saved to file!")

def read_names(filename):
    print("\n📂 Reading names from file...")
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            print("🧾 Here are the names you saved:")
            for name in names:
                print("- " + name.strip())
    except FileNotFoundError:
        print("🚫 File not found!")

# Main logic
file_name = "names.txt"
save_names(file_name)
read_names(file_name)
