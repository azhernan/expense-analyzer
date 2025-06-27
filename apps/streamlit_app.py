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

st.sidebar.header("📁 Cargar archivo CSV")

archivo_cargado = st.sidebar.file_uploader("Subí tu archivo de gastos (formato CSV)", type=["csv"])

if archivo_cargado is not None:
    df = pd.read_csv(archivo_cargado, parse_dates=["Fecha"])
    st.success("✅ Archivo cargado correctamente.")
else:
    st.info("ℹ️ Usando archivo por defecto: `data/gastos.csv`")
    df = loader.leer_csv("data/gastos.csv")


# 📅 Filtro de fechas
st.sidebar.header("📅 Filtro por fecha")
desde = st.sidebar.date_input("Desde", value=min_fecha, min_value=min_fecha, max_value=max_fecha)
hasta = st.sidebar.date_input("Hasta", value=max_fecha, min_value=min_fecha, max_value=max_fecha)

# Aplicar filtro por fecha
df_filtrado = processor.filtrar_por_fecha(df, desde, hasta)

# 📂 Filtro por categoría
st.sidebar.header("📂 Filtro por categoría")
categorias = sorted(df_filtrado["Categoría"].dropna().unique())
categorias_seleccionadas = st.sidebar.multiselect("Seleccioná una o más categorías:", categorias)

# Si no se selecciona ninguna, indica que no hay filtros y no muestra nada
df_filtrado = df_filtrado[df_filtrado["Categoría"].isin(categorias_seleccionadas)]

if df_filtrado.empty:
    st.warning("⚠️ No hay datos para mostrar con los filtros seleccionados.")
    st.stop()

df_filtrado = df_filtrado[df_filtrado["Categoría"].isin(categorias_seleccionadas)]

# Mostrar resumen
st.write(f"📆 Gastos desde **{desde}** hasta **{hasta}** · Categorías: {', '.join(categorias_seleccionadas)}")
st.write(f"📌 Total de registros: **{len(df_filtrado)}**")

# Mostrar datos y gráficos
if df_filtrado.empty:
    st.warning("No hay datos para mostrar con los filtros seleccionados.")
    st.stop()

st.dataframe(df_filtrado)

resumen = processor.analizar_gastos(df_filtrado)

st.subheader("Gastos por Categoría")
fig_cat = visualizer.graficar_categoria(resumen)
st.pyplot(fig_cat)

st.subheader("Distribución por Tipo de Gasto")
fig_tipo = visualizer.graficar_tipo(resumen)
st.pyplot(fig_tipo)
