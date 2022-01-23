
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 
import time 

import collections
from numpy.core.defchararray import lower
import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import os

def app():
    
    if 'main_data.csv' not in os.listdir('data') or 'main_data1.csv' not in os.listdir('data') or 'main_data2.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:

        df_performance = pd.read_csv('data/main_data.csv')
        df_risk = pd.read_csv('data/main_data1.csv')
        df_pos = pd.read_csv('data/main_data2.csv')
     
        
        df=df_performance
        df1=df_risk
        df2=df_pos
        df.dropna(inplace=True,axis=1)
        df1.dropna(inplace=True,axis=1)
        df2.dropna(inplace=True,axis=1)
        st.write(df1)
        st.title('Lit financial Dashboard')
        def graph_portfolio():
       
            tickers=df.columns[1:]
            dropdown=st.multiselect('Pick your asset',tickers)
            start = st.date_input('Start1', value= pd.to_datetime(df.iloc[1,0]))
            end= st.date_input('End1', value =pd.to_datetime(df.iloc[len(df)-1,0]))
            
            
            #convertie les dates en datetime puis les mets en indices
            
            a=pd.to_datetime(df[df.columns[0]])
            df[df.columns[0]]=a
            df.set_index(df.columns[0],inplace=True)
            liste=list(df.index)
            
            if len(dropdown)>0:
                d=df[dropdown][liste.index(start):liste.index(end)]
                st.line_chart(d)
                
            st.write("\n")
          
            
            b=pd.to_datetime(df1[df1.columns[0]])
            df1[df1.columns[0]]=b
            df1.set_index(df1.columns[0],inplace=True)
           
            st.bar_chart(df1,use_container_width=True)
        
          
                
        
        graph_portfolio()
        
    
    

    
