import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
from PIL import Image

# @st.cache
def app():
    
    
    st.markdown("## Data Upload")

    # Upload the dataset and save as csv
    st.markdown("### Upload a portfolio csv file ") 
    st.write("\n")
    

    # Code to read a single file 
    uploaded_file = st.file_uploader("First file", type = ['csv', 'xlsx'])
    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
  

    # Upload the dataset and save as csv
    st.markdown("### Upload a risk csv file ") 
    st.write("\n")
    

    # Code to read a single file 
    uploaded_file1 = st.file_uploader("Second file", type = ['csv', 'xlsx'])
    global data1
    if uploaded_file1 is not None:
        try:
            data1 = pd.read_csv(uploaded_file1)
        except Exception as e:
            print(e)
            data1 = pd.read_excel(uploaded_file1)
    
    

    # Upload the dataset and save as csv
    st.markdown("### Upload a position csv file ") 
    st.write("\n")
    

    # Code to read a single file 
    uploaded_file2 = st.file_uploader("Third file", type = ['csv', 'xlsx'])
    global data2
    if uploaded_file2 is not None:
        try:
            data2 = pd.read_csv(uploaded_file2)
        except Exception as e:
            print(e)
            data2 = pd.read_excel(uploaded_file2)
    
    
    
    
    # uploaded_files = st.file_uploader("Upload your CSV file here.", type='csv', accept_multiple_files=False)
    # # Check if file exists 
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)
    
    # uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    # print(uploaded_files, type(uploaded_files))
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)
    
    # read temp data 
    # data = pd.read_csv('data/2015.csv')


    ''' Load the data and save the columns with categories as a dataframe. 
    This section also allows changes in the numerical and categorical columns. '''
    if st.button("Load Data"):
        
        # Raw data 
        st.dataframe(data)
        st.dataframe(data1)
        st.dataframe(data2)
        #utils.getProfile(data)
        #st.markdown("<a href='output.html' download target='_blank' > Download profiling report </a>",unsafe_allow_html=True)
        #HtmlFile = open("data/output.html", 'r', encoding='utf-8')
        #source_code = HtmlFile.read() 
        #components.iframe("data/output.html")# Save the data to a new file 
        data.to_csv('data/main_data.csv', index=False)
        data1.to_csv('data/main_data1.csv', index=False)
        data2.to_csv('data/main_data2.csv', index=False)