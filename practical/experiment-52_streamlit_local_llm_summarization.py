"""Streamlit Local LLM Summarization\nSummarize notices through a Streamlit application.\n"""

import streamlit as st
from transformers import pipeline

st.title("Engineering AI Application")
task = st.text_area("Enter your text")

if st.button("Generate"):
    generator = pipeline("text-generation", model="gpt2")
    result = generator(task, max_new_tokens=120, return_full_text=False)
    st.write(result[0]["generated_text"])
