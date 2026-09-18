import streamlit as st
st.title("My first streamlit App")
st.write("Welcome to streamlit!")
name = st.text_input("Enter Your Name")

if st.button("submit"):
    st.success(f"Hello {name}")