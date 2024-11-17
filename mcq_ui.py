from mcq import generate_mcq
import streamlit as st


st.title("MCQ Generator")
topic = st.sidebar.text_input("enter the topic:")
number = st.sidebar.text_input("Enter the number of ques needed:")
if topic and number:
    mmm = generate_mcq(topic,number)
    st.text(mmm)