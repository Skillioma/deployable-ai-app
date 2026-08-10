import streamlit as st
from config.settings import load_settings
from services.ai_service import generate_response
from prompts.templates import build_user_prompt

st.title("Professional AI App")

settings = load_settings()

prompt = st.text_area("Enter your prompt")

if st.button("Generate"):

    if prompt.strip():
        
        prepared_prompt = build_user_prompt(prompt)

        response = generate_response(
            prompt=prepared_prompt,
            api_key=settings.api_key,
            model_name=settings.model_name
        )

        st.write(response)