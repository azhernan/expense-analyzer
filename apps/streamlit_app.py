import streamlit as st
import pandas as pd
from src import loader, processor, visualizer

st.set_page_config(page_title="Dashboard de Gastos", layout="wide")
st.title("📊 Dashboard de Gastos Personales")

# Cargar datos
df = loader.leer_csv("data/gastos.csv")

if df.empty:
    st.error("No se pudieron cargar los datos.")
    st.stop()

# Rango de fechas disponibles
min_fecha = df["Fecha"].min().date()
max_fecha = df["Fecha"].max().date()

# Filtro de fechas
st.sidebar.header("📅 Filtro por fecha")
desde = st.sidebar.date_input("Desde", value=min_fecha, min_value=min_fecha, max_value=max_fecha)
hasta = st.sidebar.date_input("Hasta", value=max_fecha, min_value=min_fecha, max_value=max_fecha)

# Aplicar filtro
df_filtrado = processor.filtrar_por_fecha(df, desde, hasta)

st.write(f"Mostrando gastos desde **{desde}** hasta **{hasta}** ({len(df_filtrado)} registros)")

# Mostrar tabla
st.dataframe(df_filtrado)

# Análisis
resumen = processor.analizar_gastos(df_filtrado)

# Visualizaciones
st.subheader("Gastos por Categoría")
fig_cat = visualizer.graficar_categoria(resumen)
st.pyplot(fig_cat)

st.subheader("Distribución por Tipo de Gasto")
fig_tipo = visualizer.graficar_tipo(resumen)
st.pyplot(fig_tipo)

