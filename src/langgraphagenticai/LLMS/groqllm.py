import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls
        self.groq_api_key = user_controls.get("GROQ_API_KEY", "")
        self.selected_groq_model = user_controls.get("selected_groq_model", "groq/groq-llama-3.1-70b-chat")
        self.groq_client = None

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_controls.get("selected_groq_model", "")

            if not groq_api_key:
                st.error("Groq API Key is not set. Please enter your Groq API Key in the sidebar.")
                return None
            
            llm = ChatGroq(api_key=groq_api_key, model_name=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Failed to initialize Groq LLM: {str(e)}")
        return llm