# AutoML - Application

## The project
The project is an AutoML solution to train Machine Learning models with little human interference. 
This is a extension of the [App](https://www.youtube.com/watch?v=xTKoyfCQiiU&t=2s) with new features.

Automated machine learning, also known as AutoML, is the process of automating the time-consuming and iterative tasks of machine learning model development. With it, data scientists, analysts, and developers can build ML models with high scale, efficiency, and productivity while supporting model quality.

## Tecnologies
* Pycaret (lib for AutoML)
* Pandas
* Streamlit
* Docker
* App Engine (Google Cloud Platform) for Cloud Deployment

## Features
* Load data for classification problems
* Analysis of dataset 
* Select predictor variabels
* Train model
* Get the best model

## How to run
´´´
git clone https://github.com/ozseniorcl13/AutoMLApp
cd AutoMLApp
python -m venv venv
source venv/bin/activate  (for linux)
venv/Scripts/activate     (for linux)
pip install -r requirements.txt
streamlit run app.py
´´´