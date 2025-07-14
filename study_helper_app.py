import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# Branding
st.markdown("<h4 style='text-align: center;'>Powered by Krisha Patel</h4>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📚 Welcome my friend!</h2>", unsafe_allow_html=True)

# Subject and class input
board = st.selectbox("📘 Choose your Board", ["Gujarat Board", "CBSE", "ICSE", "Other"])
subject = st.selectbox("📗 Choose Subject", ["Science", "Maths", "English", "Social Science", "Computer", "Other"])
student_class = st.selectbox("🏫 Select Class", ["6", "7", "8", "9", "10", "11", "12"])
topic = st.text_input("📝 Enter the chapter/topic name")

if topic:
    prompt = f"""
    You're a helpful Study Assistant. The user is in class {student_class}, studying under {board}.
    The subject is {subject}. Based on the topic "{topic}", do the following:

    1. Give a detailed but simple explanation of the topic in student-friendly language.
    2. Highlight important questions from this chapter (at least 5).
    3. Create a 20-mark test from the chapter.
    4. If the topic requires a diagram (e.g. science), describe or suggest it.
    5. Ask the student if they understood the topic, and if not, offer to explain again in another way.
    """

    try:
        with st.spinner("🧠 Thinking..."):
            response = model.generate_content(prompt)
            st.success("✅ Done!")
            st.write(response.text)
    except Exception as e:
        st.error("❌ Failed to get response. Please check your API key or try again.")
        st.text(str(e))


