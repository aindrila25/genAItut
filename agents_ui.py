from agents import generate_papersummary
import streamlit as st


st.title("Research Paper Summarizer")
code = st.sidebar.text_input("Enter the arxiv code of the paper")
if code:
    c = generate_papersummary(code)
    st.text_area("Paper Summary", value=c, height=200)