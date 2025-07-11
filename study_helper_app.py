import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- App Heading ---
st.markdown("<h1 style='text-align: center;'>📘 Study Helper</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>👋 Welcome my friend!</h3>", unsafe_allow_html=True)

# --- Powered By ---
st.markdown("<p style='text-align: center; color: gray;'>🚀 Powered by <b>Krisha Patel</b></p>", unsafe_allow_html=True)

# --- Class Selection ---
class_level = st.selectbox("Select Your Class:", [
    "Class 6", "Class 7", "Class 8", "Class 9", "Class 10", 
    "Class 11 (Science)", "Class 11 (Commerce)", 
    "Class 12 (Science)", "Class 12 (Commerce)"
])

# --- Board Selection ---
board = st.selectbox("Select Your Board:", ["GSEB", "CBSE", "ICSE", "Other"])
subject = st.text_input("Enter Subject:")
topic = st.text_input("Enter Chapter/Topic:")

def ask_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if st.button("Generate Study Material"):
    with st.spinner("Generating content..."):
        prompt = f"""
You are an AI Study Helper. The user is from {board}, studying in {class_level}.
Explain the topic: "{topic}" from subject: "{subject}" in detail appropriate for their class.
Then:
1. Give 5 important key points.
2. Suggest 5 important exam questions.
3. Create a 20-mark test based on this topic.
4. If the topic includes diagrams, describe or mention them too.
"""
        output = ask_gpt(prompt)
        st.markdown("### 📚 Study Material:")
        st.write(output)
