import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls['selected_llm'] = st.selectbox(
                "Select LLM",
                options=llm_options,
                index=0,
                help="Select the LLM to use for the agent.",
            )

            if self.user_controls["selected_llm"] == "Groq":

                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_groq_model'] = st.selectbox("Select Groq Model",
                                                                         options=model_options,
                                                                         index=0,
                                                                         help="Select the Groq model to use.")

                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Groq API Key",
                                                                                                      type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to use Groq models.")

            self.user_controls['selected_usecase'] = st.selectbox(
                "Select Use Case",
                options=usecase_options,
                index=0,
                help="Select the use case",
            )

            if self.user_controls['selected_usecase'] == "Chatbot With Web" or self.user_controls[
                'selected_usecase'] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls['TAVILY_API_KEY'] = st.session_state[
                    "TAVILY_API_KEY"] = st.text_input(
                    "Tavily API Key",
                    type="password",
                    help="Enter your Tavily API Key to use web search capabilities."
                )

                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("Please enter your Tavily API Key to use web search capabilities.")

            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox("🗓️ Select Time Frame",
                                              ["Daily", "Weekly", "Monthly"],
                                              index=0
                                              )

                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.timeframe = time_frame
        return self.user_controls
