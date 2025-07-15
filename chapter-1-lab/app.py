import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini model with API key from environment variable
if not os.getenv('GOOGLE_API_KEY'):
    st.error("Please set your Google API Key in the .env file!")
    st.stop()

# Create the chat model
chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.title("Gemini Chat App")

# Here we create our chat input
user_input = st.chat_input("Type your message here...")

# Generate and display response
if user_input:
    st.chat_message("user").write(user_input)
    try:
        response = chat_model.invoke(user_input)
        st.chat_message("assistant").write(response.content)
    except Exception as e:
        st.error(str(e))