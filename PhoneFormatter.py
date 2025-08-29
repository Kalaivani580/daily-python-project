import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI


# ✅ Step 1: Load the .env file
load_dotenv()

# ✅ Step 2: Read OpenAI API Key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("❌ API key not found! Please create a .env file with OPENAI_API_KEY.")
    st.stop()

# ✅ Step 3: Set API key for LangChain
os.environ["OPENAI_API_KEY"] = openai_api_key

# ✅ Step 4: Set up Streamlit page
st.set_page_config(page_title="📱 Phone Number Formatter", layout="centered")
st.title("📱 Phone Number Formatter")
st.markdown("Enter a 10-digit number to format it as **(xxx) xxx-xxxx**")

# ✅ Step 5: User input
phone_input = st.text_input("Enter 10-digit number", max_chars=10)

# ✅ Step 6: Button logic
if st.button("Format Number"):
    if phone_input.isdigit() and len(phone_input) == 10:
        # LangChain Prompt Template
        template = "Format this number {raw_number} as U.S. phone format (xxx) xxx-xxxx."
        prompt = PromptTemplate(
            input_variables=["raw_number"],
            template=template,
        )

        # LLM Setup
        llm = OpenAI(temperature=0)
        chain = LLMChain(llm=llm, prompt=prompt)

        # Run LLM to format
        formatted = chain.run(raw_number=phone_input)

        # Output
        st.success("🎉 Formatted Phone Number:")
        st.code(formatted.strip(), language='text')
    else:
        st.error("❌ Please enter exactly 10 digits. Example: 9876543210")
