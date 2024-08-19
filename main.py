import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Subtitle
st.header("Welcome to my first Streamlit app!")

# Input from the user
name = st.text_input("What's your name?")

# Button to display the greeting
if st.button("Greet me"):
    st.write(f"Hello, {name}! Welcome to the Streamlit app.")
else:
    st.write("Enter your name and click the button to be greeted.")

# Display a slider
age = st.slider("How old are you?", 0, 100, 25)

# Display the age
st.write(f"You're {age} years old.")
