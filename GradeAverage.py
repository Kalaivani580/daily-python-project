import streamlit as st

st.title("Test Score Average Calculator")

st.write("Enter your 5 test scores below:")

# Input fields for test scores
score1 = st.number_input("Test Score 1", min_value=0.0, max_value=100.0, step=1.0)
score2 = st.number_input("Test Score 2", min_value=0.0, max_value=100.0, step=1.0)
score3 = st.number_input("Test Score 3", min_value=0.0, max_value=100.0, step=1.0)
score4 = st.number_input("Test Score 4", min_value=0.0, max_value=100.0, step=1.0)
score5 = st.number_input("Test Score 5", min_value=0.0, max_value=100.0, step=1.0)

# Button to calculate average
if st.button("Calculate Average"):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    st.write(f"Average Score: {average:.2f}")
    
    # Determine Pass or Fail
    if average >= 40:
        st.success("Result: Pass 🎉")
    else:
        st.error("Result: Fail ❌")
