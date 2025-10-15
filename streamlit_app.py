# streamlit_app.py
import streamlit as st
import requests
import os

st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini Chatbot")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question:")

if st.button("Send"):
    if user_input:
        try:
            response = requests.post(
                "http://backend:8000/chat",  # backend container name
                json={"question": user_input},
                timeout=30
            )
            answer = response.json().get("answer")
        except Exception as e:
            answer = f"⚠️ Error: {e}"

        st.session_state.chat_history.append({"user": user_input, "bot": answer})

# Display chat
for msg in st.session_state.chat_history:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Bot:** {msg['bot']}")