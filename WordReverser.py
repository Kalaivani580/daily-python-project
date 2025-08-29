# WordReverser.py

import streamlit as st

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

# Streamlit UI
st.title("🔁 Word Reverser App")
st.write("This app reverses each word in the sentence while keeping their order.")

# Text input
user_input = st.text_input("Enter a sentence:")

# When user types something
if user_input:
    result = reverse_words(user_input)
    st.success(f"Reversed Sentence: {result}")
