import streamlit as st
import pandas as pd

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

import os

from pycaret.classification import setup, compare_models, pull, save_model

if os.path.exists('source_data.csv'):
    df = pd.read_csv('source_data.csv', index_col = None)

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
        
if choice == 'Explore and Analysis your data':
    st.title('Explore your data and get insights')
    
    if st.button('Start analysis'):
        profile_report = df.profile_report()
        st_profile_report(profile_report)
    
if choice == 'Train moodel':
    st.title('AutoML Training')
    target = st.selectbox("Select your target", df.columns)

    st.caption('Select features for training')    
    columns = df.columns.difference([target])
    
    features = {}
    for c in columns:
        features[c] = st.checkbox(c, value = True)   
    
    columns_train = [k for k, v in features.items() if features[k]]
    
    columns_train.append(target)
    
    st.caption('Features and target')
    if len(columns_train) != 1:
        st.dataframe(df[columns_train].head())
    
    if st.button('Start train'):
        
        setup(df[columns_train], target=target, silent=True)
        setup_df = pull()
        st.caption('Settings for the AutoML experiment')
        st.dataframe(setup_df)
        best_model = compare_models()
        compare_df = pull()
        st.caption("Results")
        st.dataframe(compare_df)
        st.caption('The best model')
        best_model
        save_model(best_model, 'best_model')
    
if choice == 'Get model':
    st.title('Download the model trained')
    with open('best_model.pkl', 'rb') as f:
        st.download_button('Download model', f, file_name = 'best_model.pkl')