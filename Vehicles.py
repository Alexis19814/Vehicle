import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Anuncio de coches en venta')

car_data = pd.read_csv(r'C:\Users\ALEXI\Downloads\vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfica de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

bar_button = st.button('Construir gráfica de barras')

if bar_button:
    st.write('Creación de un gráfico de barras para el conjunto de datos de anuncios de venta de coches')
    fig = px.bar(car_data, x="condition",y="price")
    st.plotly_chart(fig, use_container_width=True)