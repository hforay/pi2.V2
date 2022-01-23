import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
choosen_portfolio=[]

def app():
    df1=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/Perf_PM1.csv")
    df2=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/Perf_PM2.csv")
    df3=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/table_pos_PM1.csv")
    df4=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/table_pos_PM2.csv")
    df5=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/risk_PM1.csv")
    df6=pd.read_csv("C:/Users/msi/Desktop/ESILV/A4/PI2/risk_PM2.csv")
    
    df3.set_index('ID',inplace= True)
    df4.set_index('ID',inplace=True)
    df5.set_index('Date_CR',inplace=True)
    df6.set_index('ID',inplace=True)
    
    df1.dropna(inplace=True,axis=1)
    df2.dropna(inplace=True,axis=1)
    df3.dropna(inplace=True,axis=1)
    df4.dropna(inplace=True,axis=1)
    df5.dropna(inplace=True,axis=1)
    df6.dropna(inplace=True,axis=1)
    st.title('Ostrum financial Dashboard')
    options = st.multiselect(
     'What are your favorite colors',
     ['portfolio 1','portfolio 2'])

    st.write('You selected:', options)