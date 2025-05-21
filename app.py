import pandas as pd
import plotly_express as px
import streamlit as st 

car_data = pd.read_csv("vehicles.csv")
fig = px.histogram(car_data, x="year", y="price", color="make", tittle="Preço dos carros por ano")
st.tittle("histograma de preços dos carros")
fig.show()