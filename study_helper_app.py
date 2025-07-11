import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Access the OpenAI API key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to ask GPT a question
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# ✅ Streamlit UI setup
st.set_page_config(page_title="AI Study Helper", layout="wide")
st.title("📚 AI Study Helper")

# Get board, class, subject, and topic from the user
board = st.selectbox("Select your board:", ["Gujarat Board (GSEB)", "CBSE", "Other"])
class_level = st.selectbox("Select your class:", ["8", "9", "10", "11", "12"])
subject = st.text_input("Enter the subject:")
chapter = st.text_input("Enter the topic or chapter name:")

# Button to generate content
if st.button("Generate Study Material"):
    if chapter and subject:
        with st.spinner("Generating your study material..."):
            prompt = f"""
You are an AI tutor for students of {board} in class {class_level}.
The topic is "{chapter}" from the subject "{subject}".

1. First, explain this topic in simple terms, suitable for class {class_level}.
2. Then give:
   - Key points and notes
   - 5 important questions
   - A 20-mark test (4-5 questions)
3. If any diagram is involved, describe it and explain how to draw it.
4. Ask if the student understood it; if not, explain in another way.
"""
            output = ask_gpt(prompt)
            st.markdown("### 🧠 Study Material:")
            st.markdown(output)
    else:
        st.warning("Please enter both subject and topic/chapter name.")

