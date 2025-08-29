import streamlit as st

# Streamlit app title
st.title("Find the Largest Number in a List (Without Using max())")

# Text input from user
user_input = st.text_input("Enter numbers separated by commas (e.g., 5, 12, 8, 23, 1):")

# Check if input is given
if user_input:
    try:
        # Convert the input string to a list of integers
        num_list = [int(num.strip()) for num in user_input.split(",")]

        # Initialize 'largest' with the first value in the list
        largest = num_list[0]

        # Loop through the list to find the largest number
        for number in num_list:
            if number > largest:
                largest = number

        # Display the result
        st.success(f"The largest number in the list is: {largest}")

    except ValueError:
        st.error("❌ Please enter valid numbers only, separated by commas.")
