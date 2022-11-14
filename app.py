import streamlit as st

with st.sidebar:
    st.title('Auto ML App')
    choice = st.radio('Navigation', ['Upload', 'Data Analysis', 'Train model', 'Download model'])
    st.info('Load your dataset, explore your data and train model automated')