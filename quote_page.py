import streamlit as st
from common_functions import get_random_quote

st.title("Inspirujący cytat dnia")

if st.button("Pokaż mi cytat"):
    quote = get_random_quote()
    st.write(quote)

st.write("Ta strona korzysta z wspólnej funkcji get_random_quote()")