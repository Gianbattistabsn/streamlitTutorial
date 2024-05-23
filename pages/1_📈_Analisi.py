import streamlit as st
from utils.utils import *
import pandas as pd

#ogni tab ha una funzione separata
def create_tab_prodotti(tab_prodotti):
    col1,col2,col3 = tab_prodotti.columns(3)
    # creazione query
    payment_info = execute_query(st.session_state["connection"], "SELECT SUM(amount) AS 'Total Amount', MAX(amount) as 'Max Payment', AVG(amount) as 'Average Payment' FROM payments")
    # zip in python, funzione per rielaborare i risultati restituiti da mysql
    payment_info_dict = [dict(zip(payment_info.keys(), result)) for result in payment_info]
    # Come vedere i numeri in maniera decente PD
    col1.metric('Importo Totale',f"$ {compact_format(payment_info_dict[0]['Total Amount'])}")
    col2.metric('Pagamento Massimo',f"$ {compact_format(payment_info_dict[0]['Max Payment'])}")
    col3.metric('Pagamento Medio',f"$ {compact_format(payment_info_dict[0]['Average Payment'])}")

    with tab_prodotti.expander("Panoramica Prodotti", True):
        prod_col1,prod_col2,prod_col3 = st.columns(3)
        sort_param = prod_col1.radio("Ordina per: ", ["code", "name", "quantity", "price"]) # restituisce il valore selezionato dall'utente
        sort_choice = prod_col2.selectbox("Ordine: ", ["Crescente", "Decrescente"])
        sort_dict = {"Crescente": "ASC", "Decrescente":"DESC"}
        # TASTO MOSTRA-> Query personalizzata
        if(prod_col1.button("Mostra", type = "primary")):
            query_base = "SELECT productCode AS 'code', productName AS 'name', quantityInStock AS quantity, buyPrice AS price, MSRP FROM products"
            query_sort = f"ORDER BY {sort_param} {sort_dict[sort_choice]};"
            prodotti = execute_query(st.session_state["connection"], query_base + ' ' + query_sort)
            # Porto in pandas...
            df_prodotti = pd.DataFrame(prodotti)
            # Visualizzare il data frame 
            st.dataframe(df_prodotti, use_container_width=True)

if __name__ == "__main__":
    st.title("📈 Analisi")

    #creazione dei tab distinti
    tab_prodotti,tab_staff,tab_clienti=st.tabs(["Prodotti","Staff","Clienti"]) # Passiamo una lista di stringhe


    if(check_connection()):
        create_tab_prodotti(tab_prodotti)

    