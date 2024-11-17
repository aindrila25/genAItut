import petname 
import streamlit as st


st.title("Name generator")

type = st.sidebar.selectbox("What do u want to name?",("cat","dog","daughter","son"))
num = st.sidebar.text_input("How many names do u want?", "5")
if type and num : 
    n=petname.generate_name(num,type)
    st.text(n)