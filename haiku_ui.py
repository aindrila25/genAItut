import haiku
import streamlit as st


st.title("Haiku Generator")

language = st.sidebar.selectbox("In which language do u want your haiku to be presented?",("English","Japanese","French","Spanish"))
topic = st.sidebar.text_input("Write down a topic for haiku")
if language and topic : 
    n= haiku.generate_haiku(language,topic)
    st.text(n)