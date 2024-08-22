import streamlit as st
import os
from quote_page import show_quote_page
from bmi_calculator import show_bmi_calculator



def get_full_url():
    # Pobieramy pełny URL z nagłówków HTTP
    return st.get_option("server.baseUrlPath")

def main():
    full_url = get_full_url()
    
    if 'quotes.diduknow.org' in full_url:
        show_quote_page()
    elif 'bmi.diduknow.org' in full_url:
        show_bmi_calculator()
    else:
        st.write("Welcome to the main page of diduknow.org. Please use a specific subdomain.")

    # Dla debugowania
    st.write(f"Current URL: {full_url}")

if __name__ == "__main__":
    main()