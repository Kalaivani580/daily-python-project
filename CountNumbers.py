import streamlit as st

# Title
st.title("🔢 Count Positive, Negative, and Zero Numbers")

# Instructions
st.write("Enter a list of numbers separated by commas (e.g., `1, -2, 0, 5, -3`).")

# User input
input_string = st.text_input("Enter numbers:")

def count_numbers(numbers):
    positives = sum(1 for n in numbers if n > 0)
    negatives = sum(1 for n in numbers if n < 0)
    zeros = sum(1 for n in numbers if n == 0)
    return positives, negatives, zeros

if input_string:
    try:
        # Convert input string to list of numbers
        number_list = [float(n.strip()) for n in input_string.split(',')]
        pos_count, neg_count, zero_count = count_numbers(number_list)

        # Display results
        st.success("✅ Counts:")
        st.write(f"**Positive numbers:** {pos_count}")
        st.write(f"**Negative numbers:** {neg_count}")
        st.write(f"**Zeros:** {zero_count}")
    except ValueError:
        st.error("❌ Please enter a valid list of numbers.")
