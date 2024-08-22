import streamlit as st
from quote_page import show_quote_page
from bmi_calculator import show_bmi_calculator

def main():
    # Pobieramy wartość 'host' z parametrów URL
    host = st.query_params.get("host", "")
    
    if 'quotes.diduknow.org' in host:
        show_quote_page()
    elif 'bmi.diduknow.org' in host:
        show_bmi_calculator()
    else:
        st.write("Welcome to the main page of diduknow.org. Please use a specific subdomain.")

    # Opcjonalnie, możemy wyświetlić aktualny host dla celów debugowania
    st.write(f"Current host: {host}")

if __name__ == "__main__":
    main()