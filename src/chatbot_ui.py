from dotenv import load_dotenv
import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=API_KEY)


# --- Streamlit Page Config ---
st.set_page_config(page_title="Gemini Chat", page_icon="💬", layout="centered")

st.title("💬 Gemini Chat Assistant")
st.write("Type your message below and chat in real-time with your AI assistant.")

# --- Maintain chat state ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# --- Chat history display ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
# --- Input box for new user message ---
user_input = st.chat_input("Type your message...")

if user_input:
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # 2. Append user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # 3. Get model response
    with st.chat_message("assistant"):
        response = model.invoke(st.session_state.messages)
        st.markdown(response.content)
    
    # 4. Append assistant response to session
    st.session_state.messages.append(
        {"role": "assistant", "content": response.content}
    )
    user_query = input("👤: ")

    
