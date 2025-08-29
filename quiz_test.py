import streamlit as st

# Title
st.title("🧠 Simple Quiz App")

# Questions & Answers
quiz = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is 5 + 7?": "12",
    "Who wrote 'Hamlet'?": "Shakespeare"
}

# Initialize score
score = 0

# Loop through questions
for question, correct_answer in quiz.items():
    user_answer = st.text_input(question, key=question)
    if user_answer:
        if user_answer.strip().lower() == correct_answer.lower():
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Wrong! The correct answer is: {correct_answer}")

# Show score
if st.button("Show Score"):
    st.info(f"🎯 Your score: {score} out of {len(quiz)}")
