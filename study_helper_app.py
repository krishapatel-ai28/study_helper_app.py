import streamlit as st
from openai import OpenAI

# ✅ Replace with your actual OpenAI API key here or use environment variable
client = OpenAI(api_key="your-openai-api-key")  # You can also use os.getenv("OPENAI_API_KEY")

# Function to get AI response from OpenAI
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.set_page_config(page_title="AI Study Helper", layout="wide")
st.title("📚 AI Study Helper")

# Input Section
board = st.selectbox("Select your board:", ["Gujarat Board (GSEB)", "CBSE", "Other"])
class_level = st.selectbox("Select your class:", ["8", "9", "10", "11", "12"])
subject = st.text_input("Enter the subject:")
chapter = st.text_input("Enter the topic or chapter name:")

if st.button("Generate Study Material"):
    if chapter and subject:
        with st.spinner("Generating study material..."):
            prompt = f"""
You are an AI tutor for board: {board}, class: {class_level}.
Explain the chapter "{chapter}" from subject "{subject}" in detail suitable for class {class_level}.

Then provide:
- Key points and notes
- 5 important questions
- A 20-mark test (with 4-5 questions)
- If the topic includes any diagrams, describe them clearly
"""
            output = ask_gpt(prompt)
            st.markdown("### 🧠 Study Material Output:")
            st.markdown(output)
    else:
        st.warning("Please fill all the required fields.")
