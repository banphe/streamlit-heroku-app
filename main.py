import os
import streamlit as st
st.write("hellllooooo")
# Ensure the app is using the port Heroku assigns
port = int(os.environ.get("PORT", 8501))