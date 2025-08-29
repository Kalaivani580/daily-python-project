def shift_letter_by_one(text):
    shifted_text = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                shifted = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
            shifted_text += shifted
        else:
            shifted_text += char  # keep non-letters unchanged

    return shifted_text

# Example usage
input_text = input("Enter a word or sentence: ")
result = shift_letter_by_one(input_text)
print("Shifted text:", result)
