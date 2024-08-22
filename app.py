import streamlit as st
import os
from quote_page import show_quote_page
from bmi_calculator import show_bmi_calculator

def get_host():
    # Próbujemy pobrać hosta z nagłówka HTTP
    host = st.experimental_get_query_params().get('host', [''])[0] or \
           os.environ.get('HOST', '')
    return host.lower()

def main():
    host = get_host()
    
    if 'quotes.diduknow.org' in host:
        show_quote_page()
    elif 'bmi.diduknow.org' in host:
        show_bmi_calculator()
    else:
        st.write("Welcome to the main page of diduknow.org. Please use a specific subdomain.")

    # Wyświetlamy aktualny host dla celów debugowania
    st.write(f"Current host: {host}")

if __name__ == "__main__":
    main()