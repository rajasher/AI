import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
if not os.getenv('GOOGLE_API_KEY'):
    st.error("Please set your Google API Key in the .env file!")
    st.stop()

st.title("Chat App")
model_type = st.sidebar.selectbox("Model", ["Gemini", "Ollama"])

# Initialize the appropriate model based on selection
def get_model():
    if model_type == "Gemini":
        return ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    else:
        return Ollama(model="llama3.2:1b", base_url="http://localhost:11434")

# Here we create our chat input
user_input = st.chat_input("Type your message here...")

# Generate and display response
if user_input:
    st.chat_message("user").write(user_input)
    try:
        model = get_model()
        response = model.invoke(user_input)
        
        # Handle different response formats from different model types
        content = response.content if hasattr(response, 'content') else response
        st.chat_message("assistant").write(content)
    except Exception as e:
        st.error(str(e))

