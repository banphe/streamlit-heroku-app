import streamlit as st
from quote_page import show_quote_page
from bmi_calculator import show_bmi_calculator

def main():
    # Pobieramy parametr 'page' z URL
    page = st.query_params.get("page", "")
    
    if page == "quotes":
        show_quote_page()
    elif page == "bmi":
        show_bmi_calculator()
    else:
        st.write("Welcome to the main page of diduknow.org.")
        st.write("Use '?page=quotes' for the quotes page or '?page=bmi' for the BMI calculator.")

    # Dla celów debugowania
    st.write(f"Current page: {page}")

if __name__ == "__main__":
    main()