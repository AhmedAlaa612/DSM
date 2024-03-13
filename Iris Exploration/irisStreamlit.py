import streamlit as st
import pandas as pd 



iris = pd.read_csv('Iris.csv')
st.title('Iris Dataset')
n = st.slider('Number of rows to view', 1, 150, 5)
st.dataframe(iris[:n])