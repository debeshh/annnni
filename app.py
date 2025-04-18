import streamlit as st
import requests
import uuid
import json
from datetime import datetime

st.set_page_config(page_title="ANNNI", layout="wide")
st.title("Hey Debesh")
st.write("how can i help you today.")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

WEBHOOK_URL = "https://zorooo.app.n8n.cloud/webhook/7df913c7-d1ba-42a3-bf95-6f6a769e866d/chat"
API_TOKEN = "your-bearer-token-here" 

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_input = st.chat_input("Type your message here...")


def send_message_to_webhook(message, session_id):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "sessionId": session_id,
        "chatInput": message
    }
    
    try:
        response = requests.post(WEBHOOK_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for 4XX/5XX responses
        
        data = response.json()
        return data.get("output", "Sorry, I couldn't process your request.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with the AI service: {str(e)}")
        return "Sorry, there was an error processing your request. Please try again later."


if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message_to_webhook(user_input, st.session_state.session_id)
            st.write(response)
    
    st.session_state.chat_history.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("Session Information")
    st.write(f"**Session ID:** {st.session_state.session_id}")
    st.write(f"**Session Start:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if st.button("Start New Session"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.chat_history = []
        st.rerun()