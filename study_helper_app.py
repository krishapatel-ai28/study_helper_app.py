import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set model name
model = genai.GenerativeModel("models/gemini-pro")  # ✅ FULL model name

# Logo & branding
st.image("logo.png", width=120)
st.markdown("<h4 style='text-align: center;'>Powered by Krisha Patel</h4>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📚 Welcome my friend!</h2>", unsafe_allow_html=True)

# User input
board = st.selectbox("📘 Choose your Board", ["Gujarat Board", "CBSE", "ICSE", "Other"])
subject = st.selectbox("📗 Choose Subject", ["Science", "Maths", "English", "Social Science", "Computer", "Other"])
student_class = st.selectbox("🏫 Select Class", ["6", "7", "8", "9", "10", "11", "12"])
topic = st.text_input("📝 Enter the chapter/topic name")

if topic:
    prompt = f"""
    You are a helpful Study Assistant. The user is in class {student_class}, studying under {board}.
    The subject is {subject}. Based on the topic "{topic}", do the following:

    1. Explain the topic simply and clearly.
    2. Give at least 5 important questions.
    3. Create a 20-mark test.
    4. Mention if a diagram is required.
    5. Ask if the student understood, and re-explain if needed.
    """

    try:
        with st.spinner("💡 Thinking..."):
            response = model.generate_content(prompt)
            st.success("✅ Done!")
            st.write(response.text)
    except Exception as e:
        st.error("❌ Something went wrong.")
        st.exception(e)


