import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pyodbc

def app():

    st.title('Decision')
    
    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\33761\Desktop\ESILV-A4\S7\PI2_OSTRUM_AM\Base_Start.accdb;'
        print("opening.....")
        connection = pyodbc.connect(con_string)
        cursor = connection.cursor()
        Perf_PM1 = 'Perf_PM1'
        requete = 'SELECT * FROM {}'.format(Perf_PM1)
        data_perf_PM1 = cursor.execute(requete)
        champs_Perf_PM1  = list()
        for column in data_perf_PM1.description:
            champs_Perf_PM1.append(column[0])
        champs_Perf_PM1.remove('ID')
        print("successed.........")
        cursor.close()
        connection.close()
        print("connection closed.")

    except pyodbc.Error as e:
        print("Error in connection")

    dropdown=st.multiselect('Pick your asset',champs_Perf_PM1)

    col1, col2, col3 = st.columns(3)
    with col1:
        acheter = st.button("Acheter")
    with col2:
        conserver = st.button("Conserver")
    with col3:
        vendre = st.button("Vendre")
    
    user_input = st.text_area("Ajouter un commentaire : ")
