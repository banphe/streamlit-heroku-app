import streamlit as st
from quote_page import show_quote_page
from bmi_calculator import show_bmi_calculator

def main():
    host = st.experimental_get_query_params().get('host', [''])[0]
    
    if 'quotes' in host:
        show_quote_page()
    elif 'bmi' in host:
        show_bmi_calculator()
    else:
        st.write("Welcome to the main page. Please use a specific subdomain.")

if __name__ == "__main__":
    main()