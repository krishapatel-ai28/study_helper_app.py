import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit.components.v1 as components

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- HEADER SECTION ---
st.markdown("<h6 style='text-align: center; color: gray;'>🚀 Powered by Krisha Patel</h6>", unsafe_allow_html=True)
st.image("logo.png", width=120)
st.markdown("<h2 style='text-align: center;'>👋 Welcome my friend!</h2>", unsafe_allow_html=True)
st.title("📚 AI Study Helper")

# --- INPUT SECTION ---

# Board, class, subject
board = st.selectbox("Select your board:", ["Gujarat Board (GSEB)", "CBSE", "Other"])
class_level = st.selectbox("Select your class:", ["8", "9", "10", "11", "12"])
subjects = [
    "Mathematics", "Science", "English", "Hindi", "Gujarati", "Social Science",
    "Physics", "Chemistry", "Biology", "Computer Science", "History", "Geography",
    "Civics", "Economics", "Business Studies", "Accountancy"
]
subject = st.selectbox("Select your subject:", subjects)

# Language selection
language = st.selectbox("Choose output language:", ["English", "Gujarati", "Hindi"])

# Voice input (Web Speech API)
st.markdown("### 🎤 Click below and speak your topic")
components.html("""
    <script>
        function startDictation() {
            if (window.hasOwnProperty('webkitSpeechRecognition')) {
                var recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.lang = "en-IN";
                recognition.start();

                recognition.onresult = function(e) {
                    document.getElementById('textInput').value = e.results[0][0].transcript;
                    recognition.stop();
                    document.getElementById('textInputForm').submit();
                };

                recognition.onerror = function(e) {
                    recognition.stop();
                }
            }
        }
    </script>
    <form id="textInputForm" action="">
        <input type="text" name="text" id="textInput" placeholder="Speak or type your topic" style="width: 300px; height: 30px; font-size: 16px;" />
        <button type="button" onclick="startDictation()" style="height: 34px;">🎤 Speak</button>
    </form>
""", height=150)

# Text input fallback
chapter = st.text_input("Or type your topic/chapter name:")

# Ask GPT
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Generate content
if st.button("Generate Study Material"):
    if chapter:
        with st.spinner("Generating your study material..."):
            prompt = f"""
You are an AI tutor for students of {board} in class {class_level}.
The topic is "{chapter}" from the subject "{subject}".

Your response must be in {language}.

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
        st.warning("Please speak or type the topic.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>✨ Created with love by <b>Krisha Patel</b></p>", unsafe_allow_html=True)


