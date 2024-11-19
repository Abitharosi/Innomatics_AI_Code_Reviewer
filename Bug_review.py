import streamlit as st
import google.generativeai as genai

f = open("C:/Abitha/Innomatics/Gemini_demo/Gemini_key/Key.txt") 
key = f.read()

genai.configure(api_key=key)

model = genai.GenerativeModel('models/gemini-1.5-flash')

# system prompt
sys_prompt = """
You are an advanced AI code reviewer designed to enhance a user-friendly Python application. Your key tasks include:

1. ## Bug Report: Detect and report potential bugs, syntax errors, and logical issues in submitted Python code.
2. ## Fixed Code: Provide corrected or optimized code snippets with detailed, yet straightforward explanations of the changes.
3. ##Developer Support: Offer clear, actionable guidance that is accessible to developers of all skill levels.
Ensure your feedback is accurate, professional, and easy to understand, focusing on efficiency and fostering a deeper understanding of best coding practices.
"""

# function to get response
def get_response(sys_prompt, code):
    response = model.generate_content([sys_prompt, code])
    return response.text

# title of the web app
st.title("🤖GenAI App - AI Code Reviewer")
st.subheader("🧑An AI Code Reviewer")

# text box
code = st.text_area("Enter your Python code here...😊")

# generate button
button = st.button("Generate")

if button:
    try:
        response = get_response(sys_prompt, code)
        st.write(response)
    except Exception as e:
        print(e)


