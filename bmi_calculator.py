import streamlit as st
from common_functions import calculate_bmi

def show_bmi_calculator():
    st.title("Kalkulator BMI")

    weight = st.number_input("Podaj swoją wagę (kg)", min_value=30.0, max_value=300.0, value=70.0)
    height = st.number_input("Podaj swój wzrost (m)", min_value=1.0, max_value=2.5, value=1.70)

    if st.button("Oblicz BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Twoje BMI wynosi: {bmi}")

    st.write("Ta strona korzysta z wspólnej funkcji calculate_bmi()")