import os
import google.generativeai as genai
import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="My QuickResolveBot", page_icon="🤖")
st.title("🤖 My QuickResolve Chatbot")

# Helper function to get the API key
def get_api_key():
    """Fetches the Google API key from environment variables."""
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        st.error("GOOGLE_API_KEY environment variable not set!")
        st.stop()
    return key

# Gemini Model Setup
try:
    genai.configure(api_key=get_api_key())
    # Use the model name that worked for you
    model = genai.GenerativeModel('models/gemini-flash-latest') 
except Exception as e:
    st.error(f"Error configuring Gemini: {e}")
    st.stop()

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input from the chat box at the bottom
if prompt := st.chat_input("What is the capital of India?"):
    
    # 1. Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get and display AI response
    with st.chat_message("assistant"):
        try:
            # Send the prompt to the AI
            response = model.generate_content(prompt)
            ai_response = response.text
            
            # Display the AI's response
            st.markdown(ai_response)
            
            # 3. Add AI response to history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            st.error(f"Error getting response from Gemini: {e}")