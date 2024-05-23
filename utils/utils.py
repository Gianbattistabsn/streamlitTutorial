import streamlit as st
from sqlalchemy import create_engine,text

"""Raccoglie le principali funzioni condivise dalle varie pagine"""

# Creiamo la funzione per connetterci al DB

def connect_db(dialect, username, password, host, dbname):
    try:
        engine = create_engine(f'{dialect}://{username}:{password}@{host}/{dbname}')
        conn = engine.connect() # restituisce la connessione
        return conn
    except:
        return False


def execute_query(conn, query):
    return conn.execute(text(query)) #ritorna il risultato della query


def check_connection():
    if "connection" not in st.session_state.keys():
        st.session_state["connection"] = False
        # I pulsanti ritornano di default il valore True se cliccato (di default zero)
    if(st.sidebar.button("Connettiti al DB")):    #porta nella sidebar il bottone
        myconnection = connect_db(dialect="mysql+pymysql",username="student",password="user_pwd",host="localhost",dbname="classicmodels")
        if(myconnection is not False):
            st.session_state["connection"] = myconnection
        else:
            st.session_state["connection"] = False
            st.sidebar.error("Errore nella connessione") 
    if(st.session_state["connection"]):
        st.sidebar.success("Connessione effettuata")
        return True
        

#Mostrare i numeri in una forma più compatta
def compact_format(num):
    num=float(num)
    if abs(num) >= 1e9:
        return "{:.2f}B".format(num / 1e9)
    elif abs(num) >= 1e6:
        return "{:.2f}M".format(num / 1e6)
    elif abs(num) >= 1e3:
        return "{:.2f}K".format(num / 1e3)
    else:
        return "{:.0f}".format(num)
    