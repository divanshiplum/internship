import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("What's your name?")

clicked = st.button("Greet me")

if clicked and name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")
  
    st.balloons()
