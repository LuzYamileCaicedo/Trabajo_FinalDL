import streamlit as st 
import pandas as pd
import matplotlib as plt

st.title("Análisis Exploratorio de Datos -EDA #2")

data = pd.read_csv("modelos\data\12DB_6FP.csv")
st.dataframe(data)

st.subheader("Descripción de los datos")
st.dataframe(data.describe())

st.markdown("---")