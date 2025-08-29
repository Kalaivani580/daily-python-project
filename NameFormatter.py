# NameFormatter.py

import streamlit as st

st.title("📝 Name Formatter Tool")

# User input
full_name = st.text_input("Enter your full name (e.g., John Michael Smith):")

# When user types a name
if full_name:
    name_parts = full_name.strip().split()

    if len(name_parts) == 2:
        first, last = name_parts
        middle = None
    elif len(name_parts) == 3:
        first, middle, last = name_parts
    else:
        st.warning("Please enter 2 or 3 parts (e.g., John Smith or John Michael Smith).")
        st.stop()

    # Display formats
    st.subheader("Formatted Outputs:")
    st.write(f"**First Last**: {first} {last}")
    st.write(f"**Last, First**: {last}, {first}")

    if middle:
        st.write(f"**Initial. Last**: {first[0]}. {last}")
        st.write(f"**F. M. Last**: {first[0]}. {middle[0]}. {last}")
    else:
        st.write(f"**Initial. Last**: {first[0]}. {last}")
