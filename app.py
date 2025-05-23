import pandas as pd
import plotly_express as px
import streamlit as st 

df_car = pd.read_csv('df_car.csv')

st.header('Dashboard de visualização de dados')
st.subheader('Gráfico de dispersão')
st.write('Esse gráfico mostra a relação entre o preço e a quilometragem dos carros.')

hist_button = st.button('Histograma')      
scatter_button = st.button('Gráfico de dispersão')

if hist_button:
    st.subheader('Histograma')
    st.write('Esse gráfico mostra a distribuição do preço dos carros.')
    fig = px.histogram(df_car, x='price', nbins=20)
    st.plotly_chart(fig, use_container_width=True)  

    

if scatter_button:
    st.subheader('Gráfico de dispersão')
    st.write('Esse gráfico mostra a relação entre o preço e a quilometragem dos carros.')
    fig = px.scatter(df_car, x='price', y='odometer', color='type')
    st.plotly_chart(fig, use_container_width=True)