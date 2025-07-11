import streamlit as st
import openai

openai.api_key = "your-openai-api-key-here"  # Replace with your actual OpenAI API key

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

st.title("📘 AI Study Helper")

# User Inputs
topic = st.text_input("Enter your topic or chapter:")
student_class = st.selectbox("Select your class:", [6, 7, 8, 9, 10, 11, 12])
board = st.selectbox("Select your education board:", ["Gujarat Board (GSEB)", "CBSE", "ICSE", "Other"])
book_name = st.text_input("Textbook Name (e.g., GSEB, NCERT, etc.):")
language = st.radio("Select language:", ["English", "Gujarati"])

if st.button("Generate Study Material"):
    prompt = f"""
    You are an AI tutor for a class {student_class} student from the {board}.
    They are studying from '{book_name}' and want help with the topic '{topic}'.

    Explain this topic in {'Gujarati' if language == 'Gujarati' else 'English'}, using the style and syllabus of {board}.
    Include diagrams (as text or link) and give a clear explanation.

    Then list 5-7 important questions, and finally create a 20-mark test with a mix of 1, 2, and 5-mark questions.
    """
    response = ask_gpt(prompt)
    st.subheader("📚 Study Material")
    st.write(response)
