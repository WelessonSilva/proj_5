import pandas as pd
import plotly_express as px
import streamlit as st 

df_car = pd.read_csv('df_car.csv')
fig = px.histogram(df_car, x="odometer", y="price", color="blue", marginal="box",)
fig.show()