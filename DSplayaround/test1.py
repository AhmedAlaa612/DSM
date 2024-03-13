import streamlit as st
import pandas as pd
st.title('Hello World!')
st.subheader('Fist Streamlit App')
st.header('This is a header')
st.text('This is a text')
st.markdown('This is a markdown')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.markdown('---')
st.caption('This is a caption')

st.write('### this is a write ')
st.write('print("hello world")')
st.metric('Wind speed', value = '120ms⁻¹', delta = '-10ms⁻¹')
table = pd.read_csv('Iris.csv')
st.table(table.head())
st.dataframe(table.head())
