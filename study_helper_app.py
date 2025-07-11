import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# App Title and Branding
st.markdown("""
    <h1 style='text-align: center;'>📘 Powered by Krisha Patel</h1>
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/3135/3135768.png' width='100'>
    </div>
    <h2 style='text-align: center;'>👋 Welcome my friend!</h2>
""", unsafe_allow_html=True)

# Subject and Board Selection
board = st.selectbox("📚 Select Your Board", ["Gujarat Board (GSEB)", "CBSE", "ICSE", "Other"])
subject = st.selectbox("📘 Choose Subject", ["Science", "Maths", "Social Science", "English", "Hindi", "Gujarati"])

# Topic Input
topic = st.text_input("Enter the topic or chapter name:")

# Ask GPT function
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Generate Study Material
if st.button("📖 Generate Study Material"):
    if topic:
        prompt = f"""
        You are a helpful study assistant for students of the {board} in the subject of {subject}.
        The user is studying the topic: "{topic}".

        1. First explain the full topic in detail suitable for a school student.
        2. If the topic includes a diagram, explain the diagram in words.
        3. Then ask the user if they understand. If not, explain the topic again in a simpler way.
        4. Highlight key points or notes.
        5. Create 5 important questions (1-2 marks level).
        6. Create a 20-mark test paper (mix of short and long questions).
        7. Support Gujarati or Hindi if topic suggests (auto-detect).
        """
        with st.spinner("⏳ Generating content, please wait..."):
            output = ask_gpt(prompt)
            st.markdown("""---""")
            st.markdown("### 📋 Study Material:")
            st.markdown(output)
    else:
        st.warning("Please enter a topic first.")
