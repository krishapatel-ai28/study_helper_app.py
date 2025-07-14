import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel('gemini-pro')

# UI Layout
st.markdown("<h1 style='text-align:center;'>📘 Study Helper AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color: gray;'>Powered by Krisha Patel</h4>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>👋 Welcome my friend!</h2>", unsafe_allow_html=True)

# Subject and Class Selection
subject = st.selectbox("Select Subject", ["Science", "Maths", "Social Science", "English", "Gujarati", "Hindi"])
board = st.selectbox("Select Board", ["Gujarat Board", "CBSE", "ICSE", "Other"])
student_class = st.selectbox("Select Class", ["6", "7", "8", "9", "10", "11", "12"])
topic = st.text_input("Enter your topic or chapter")

# Generate Content Button
if st.button("Generate Study Material"):
    if topic:
        with st.spinner("Thinking and generating your study materials..."):
            prompt = f"""
You are a helpful study assistant for a student in class {student_class} from {board}. The subject is {subject}.
Help the student understand the topic "{topic}" in their level of understanding.

1. Explain the topic clearly and in detail.
2. If it involves any process, reaction, or diagram, describe it properly.
3. Then ask: "Did you understand?" — if not, explain again in simpler terms.
4. After explanation, give:
   - Key summary points
   - 5 important questions
   - A 20-mark test from this topic

Provide content in simple language.
"""
            response = model.generate_content(prompt)
            st.success("✅ Done! Here's your study material:")
            st.markdown(response.text)
    else:
        st.warning("⚠️ Please enter a topic first.")

