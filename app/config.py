import streamlit as st


class Config:

    @staticmethod
    def get_provider():
        return st.session_state.get("provider", "")

    @staticmethod
    def get_api_key():
        return st.session_state.get("api_key", "")

    @staticmethod
    def get_model():
        return st.session_state.get("model", "")