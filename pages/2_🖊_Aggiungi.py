import streamlit as st
from utils.utils import *


def get_list(attributo):
    query = f"SELECT DISTINCT {attributo} FROM PRODUCTS;"
    result = execute_query(st.session_state["connection"], query)
    st.write(result)
    








def create_form():
    with st.form("Nuovo Prodotto"):
        st.header(":blue[Aggiungi prodotto]")
        st.text_input("Codice", placeholder="S**_****")
        st.text_input("Nome", placeholder="Inserisci nome prodotto")




        categoria = st.selectbox("Categoria", categorie)
        scala = st.selectbox("Scala", scale)
        venditore = st.selectbox("Venditore", venditori)



if __name__ == "__main__":
    st.title("🖊 Aggiungi")
    if(check_connection()):
        create_form()
