import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("What's your name?")

clicked = st.button("Greet me")

if clicked and name:
    # State 3 - the happy path.
    st.write(f"Hello, {name}! Welcome to Streamlit.")
    st.balloons()
else:
    # NEW - what shows when the button was NOT clicked (or the box is empty).
    if name:
        # State 2 - we know who they are, they just haven't clicked yet.
        st.write(f"Hi {name}. Click the button above for a surprise.")
    else:
        # State 1 - the first thing anyone sees when the app opens.
        st.write("Type your name above, then click the button.")
