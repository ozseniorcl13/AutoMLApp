import streamlit as st
import pandas as pd

with st.sidebar:
    st.title('Auto ML App')
    choice = st.radio('Navigation', ['Upload dataset', 'Explore and Analysis your data', 'Train moodel', 'Get model'])
    st.info('Load your dataset, explore your data and train model automated')
    
if choice == 'Upload dataset':
    st.title('Upload your data for AutoML')
    file = st.file_uploader("Upload your dataset here")
    if file:
        df = pd.read_csv(file, index_col = None)
        df.to_csv("source_data.csv", index = None)
        st.dataframe(df)