import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.title("🤖 RAG ChatBot")

user_input = st.chat_input("Ask your question...")

if user_input:
    try:
        response = requests.post(
            API_URL,
            json={"question": user_input},  # ✅ JSON BODY
            timeout=60
        )

        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error(f"Backend error: {response.text}")

    except Exception as e:
        st.error(str(e))
