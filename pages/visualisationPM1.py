import streamlit as st
import pyodbc
import plotly.express as plt
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px
import matplotlib.pyplot as plt
import os

def app():

    try:
        
        first_string='Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
        second_string=os.getcwd()
        third_string ='\Base_Start.accdb;'
       
        con_string = r''+first_string+second_string+third_string
        
        print('opening...')
        
        connection = pyodbc.connect(con_string)
       
        cursor = connection.cursor()
        st.markdown("# Choose a portfolio")
        menuPM = st.selectbox(' ', ['Portfolio 1', 'Portfolio 2'])
       
        if menuPM == 'Portfolio 1' :
            #Données Pos_PM1 
            Pos_PM1='table_pos_PM1'
            requete_Pos_PM1 = 'SELECT * FROM {}'.format(Pos_PM1)
            rows_Pos_PM1 = cursor.execute(requete_Pos_PM1).fetchall()
    
            #Données Perf_PM1 
            Perf_PM1 = 'Perf_PM1'
            requete_Perf_PM1 = 'SELECT * FROM {}'.format(Perf_PM1)
            rows_Perf_PM1 = cursor.execute(requete_Perf_PM1).fetchall()
    
            #Données Risk_PM1 
            Risk_PM1 = 'risk_PM1'
            requete_Risk_PM1 = 'SELECT * FROM {}'.format(Risk_PM1)
            rows_Risk_PM1 = cursor.execute(requete_Risk_PM1).fetchall()
     
            #Conversion pyodbc en dataFrame PM1
            
           
       
            
            data_perf_PM1 = cursor.execute(requete_Perf_PM1)
            champs_perf_PM1  = list()
            for column in data_perf_PM1.description:
                champs_perf_PM1.append(column[0])
            
          
            
            data_pos_PM1 = cursor.execute(requete_Pos_PM1)
            champs_pos_PM1  = list()
            for column in data_pos_PM1.description:
                champs_pos_PM1.append(column[0])
            
            
        
            data_risk_PM1 = cursor.execute(requete_Risk_PM1)
            champs_risk_PM1  = list()
            
            for column in data_risk_PM1.description:
                champs_risk_PM1.append(column[0])
            
           
            
            df_Pos_PM1 = pd.DataFrame((tuple(t) for t in rows_Pos_PM1))
            df_Perf_PM1 = pd.DataFrame((tuple(t) for t in rows_Perf_PM1))
            df_Risk_PM1 = pd.DataFrame((tuple(t) for t in rows_Risk_PM1))
            df_Pos_PM1 = pd.DataFrame((tuple(t) for t in rows_Pos_PM1))
            df_Perf_PM1 = pd.DataFrame((tuple(t) for t in rows_Perf_PM1))
            df_Risk_PM1 = pd.DataFrame((tuple(t) for t in rows_Risk_PM1))
            
            #Renommer colonnes PM1
            
            
            df_Pos_PM1 = df_Pos_PM1.rename(columns={i:champs_pos_PM1[i] for i in range(len(champs_pos_PM1))})
            df_Perf_PM1= df_Perf_PM1.rename(columns={i:champs_perf_PM1[i] for i in range(len(champs_perf_PM1)) })
            df_Risk_PM1 = df_Risk_PM1.rename(columns={i:champs_risk_PM1[i] for i in range(len(champs_risk_PM1)) })
            
            
            #datetime en indice
           
            st.write("\n")
            st.markdown("# Performance")
            st.write("\n")
            
            tickers=df_Perf_PM1.columns[1:]
            dropdown=st.multiselect('Pick your asset',tickers)
            start = st.date_input('Start1', value= pd.to_datetime(df_Perf_PM1.iloc[1,0]))
            end= st.date_input('End1', value =pd.to_datetime(df_Perf_PM1.iloc[len(df_Perf_PM1)-1,0]))
            
            
            a=pd.to_datetime(df_Perf_PM1[df_Perf_PM1.columns[0]])
            df_Perf_PM1[df_Perf_PM1.columns[0]]=a
            df_Perf_PM1.set_index(df_Perf_PM1.columns[0],inplace=True)
            
            
            liste=list(df_Perf_PM1.index)
            
            if len(dropdown)>0:
                d=df_Perf_PM1[dropdown][liste.index(start):liste.index(end)]
                st.line_chart(d)
                
            st.write("\n")
            
            a=pd.to_datetime(df_Risk_PM1[df_Risk_PM1.columns[0]])
            df_Risk_PM1[df_Risk_PM1.columns[0]]=a
            df_Risk_PM1.set_index(df_Risk_PM1.columns[0],inplace=True)
            df_Risk_PM1["Active RISK"] = pd.to_numeric(df_Risk_PM1["Active RISK"], downcast="float")
            
            st.markdown("# Risk")
            st.write("\n")
            st.bar_chart(df_Risk_PM1,use_container_width=True)
            
            st.write("\n")
            st.markdown("# Position")
            st.write("\n")
            st.write(df_Pos_PM1)
            
        if menuPM == 'Portfolio 2' :
            
        
             #Données Pos_PM2 
            Pos_PM2='table_pos_PM2'
            requete_Pos_PM2 = 'SELECT * FROM {}'.format(Pos_PM2)
            
            rows_Pos_PM2 = cursor.execute(requete_Pos_PM2).fetchall()
            
            #Données Perf_PM1 
            Perf_PM2 = 'Perf_PM2'
            requete_Perf_PM2 = 'SELECT * FROM {}'.format(Perf_PM2)
            rows_Perf_PM2 = cursor.execute(requete_Perf_PM2).fetchall()
            
            #Données Risk_PM1 
            Risk_PM2 = 'risk_PM2'
            requete_Risk_PM2 = 'SELECT * FROM {}'.format(Risk_PM2)
            rows_Risk_PM2 = cursor.execute(requete_Risk_PM2).fetchall()
           
            #Conversion pyodbc en dataFrame PM1
            
      
            
            data_perf_PM2 = cursor.execute(requete_Perf_PM2)
          
            champs_perf_PM2  = list()
            for column in data_perf_PM2.description:
                champs_perf_PM2.append(column[0])
            
          
            
            data_pos_PM2 = cursor.execute(requete_Pos_PM2)
            champs_pos_PM2 = list()
            for column in data_pos_PM2.description:
                champs_pos_PM2.append(column[0])
            
            
        
            data_risk_PM2 = cursor.execute(requete_Risk_PM2)
            champs_risk_PM2 = list()
            
            for column in data_risk_PM2.description:
                champs_risk_PM2.append(column[0])
            
           
            
            df_Pos_PM2 = pd.DataFrame((tuple(t) for t in rows_Pos_PM2))
            df_Perf_PM2 = pd.DataFrame((tuple(t) for t in rows_Perf_PM2))
            df_Risk_PM2 = pd.DataFrame((tuple(t) for t in rows_Risk_PM2))
            df_Pos_PM2 = pd.DataFrame((tuple(t) for t in rows_Pos_PM2))
            df_Perf_PM2 = pd.DataFrame((tuple(t) for t in rows_Perf_PM2))
            df_Risk_PM2= pd.DataFrame((tuple(t) for t in rows_Risk_PM2))
            
            #Renommer colonnes PM1
            
            
            df_Pos_PM2 = df_Pos_PM2.rename(columns={i:champs_pos_PM2[i] for i in range(len(champs_pos_PM2))})
            df_Perf_PM2= df_Perf_PM2.rename(columns={i:champs_perf_PM2[i] for i in range(len(champs_perf_PM2)) })
            df_Risk_PM2 = df_Risk_PM2.rename(columns={i:champs_risk_PM2[i] for i in range(len(champs_risk_PM2)) })
            
            
            #datetime en indice
           
            st.write("\n")
            st.markdown("# Performance")
            st.write("\n")
            
            tickers=df_Perf_PM2.columns[1:]
            dropdown=st.multiselect('Pick your asset',tickers)
            start = st.date_input('Start1', value= pd.to_datetime(df_Perf_PM2.iloc[1,0]))
            end= st.date_input('End1', value =pd.to_datetime(df_Perf_PM2.iloc[len(df_Perf_PM2)-1,0]))
            
            
            a=pd.to_datetime(df_Perf_PM2[df_Perf_PM2.columns[0]])
            df_Perf_PM2[df_Perf_PM2.columns[0]]=a
            df_Perf_PM2.set_index(df_Perf_PM2.columns[0],inplace=True)
            
            
            liste=list(df_Perf_PM2.index)
            
            if len(dropdown)>0:
                d=df_Perf_PM2[dropdown][liste.index(start):liste.index(end)]
                st.line_chart(d)
                
            st.write("\n")
            
            a=pd.to_datetime(df_Risk_PM2[df_Risk_PM2.columns[0]])
            df_Risk_PM2[df_Risk_PM2.columns[0]]=a
            df_Risk_PM2.set_index(df_Risk_PM2.columns[0],inplace=True)
            df_Risk_PM2["Active RISK"] = pd.to_numeric(df_Risk_PM2["Active RISK"], downcast="float")
            
            st.markdown("# Risk")
            st.write("\n")
            st.bar_chart(df_Risk_PM2,use_container_width=True)
            
            st.write("\n")
            st.markdown("# Position")
            st.write("\n")
            st.write(df_Pos_PM2)
           
        
    
    

    


    except Exception as e:
        print (e)

    print("success.........")
    cursor.close()
    connection.close()
    print("connection closed.")