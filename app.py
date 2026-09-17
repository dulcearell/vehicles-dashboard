"""Aplicación web para explorar anuncios de vehículos usados."""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).parent / "vehicles_us.csv"


@st.cache_data
def load_data():
    """Carga el conjunto de datos y prepara las columnas utilizadas."""
    data = pd.read_csv(DATA_PATH)
    data["date_posted"] = pd.to_datetime(data["date_posted"])
    return data


st.set_page_config(page_title="Anuncios de vehículos", page_icon="🚗", layout="wide")
car_data = load_data()

st.header("Análisis de anuncios de vehículos usados")
st.write(
    "Esta aplicación permite explorar la distribución del kilometraje y la "
    "relación entre el kilometraje y el precio de los vehículos anunciados."
)

col1, col2, col3 = st.columns(3)
col1.metric("Anuncios", f"{len(car_data):,}")
col2.metric("Precio mediano", f"${car_data['price'].median():,.0f}")
col3.metric("Kilometraje mediano", f"{car_data['odometer'].median():,.0f}")

st.subheader("Visualizaciones interactivas")
build_histogram = st.checkbox("Construir histograma del kilometraje")

if build_histogram:
    st.write("Distribución del kilometraje de los vehículos anunciados")
    histogram = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        labels={"odometer": "Kilometraje"},
        title="Distribución del kilometraje",
    )
    histogram.update_layout(yaxis_title="Número de anuncios")
    st.plotly_chart(histogram, use_container_width=True)

build_scatter = st.checkbox("Construir gráfico de precio vs. kilometraje")

if build_scatter:
    st.write("Relación entre el precio y el kilometraje por condición")
    scatter_data = car_data.dropna(subset=["odometer", "price", "condition"])
    scatter = px.scatter(
        scatter_data,
        x="odometer",
        y="price",
        color="condition",
        opacity=0.5,
        labels={
            "odometer": "Kilometraje",
            "price": "Precio (USD)",
            "condition": "Condición",
        },
        title="Precio y kilometraje de los vehículos",
    )
    st.plotly_chart(scatter, use_container_width=True)

with st.expander("Ver una muestra de los datos"):
    st.dataframe(car_data.head(20), use_container_width=True)
