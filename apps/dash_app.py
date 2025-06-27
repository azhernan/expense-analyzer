import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import base64
import io
import dash
from dash import dcc, html, dash_table, Input, Output, State
import pandas as pd
import plotly.express as px
from src import loader, processor

app = dash.Dash(__name__)
app.title = "Gastos Personales"
server = app.server

df_default = loader.leer_csv("data/gastos.csv")

app.layout = html.Div([
    html.H1("💰 Dashboard de Gastos Personales", style={"textAlign": "center"}),

    html.Div([
        html.Label("📁 Subí tu archivo CSV"),
        dcc.Upload(
            id="upload-data",
            children=html.Div(["Arrastrá un archivo o hacé clic aquí para subirlo"]),
            style={
                "width": "100%", "height": "60px", "lineHeight": "60px",
                "borderWidth": "1px", "borderStyle": "dashed", "borderRadius": "5px",
                "textAlign": "center", "marginBottom": "20px"
            },
            multiple=False
        ),

        html.Div([
            html.Label("📅 Rango de Fechas"),
            dcc.DatePickerRange(
                id="filtro-fechas",
                min_date_allowed=df_default["Fecha"].min().date(),
                max_date_allowed=df_default["Fecha"].max().date(),
                start_date=df_default["Fecha"].min().date(),
                end_date=df_default["Fecha"].max().date(),
            )
        ], style={"display": "inline-block", "marginRight": "30px"}),

        html.Div([
            html.Label("📂 Categorías"),
            dcc.Dropdown(
                id="filtro-categorias",
                multi=True,
                placeholder="Seleccioná una o más categorías",
                options=[]  # ← se actualiza dinámicamente
            )
        ], style={"display": "inline-block", "width": "300px"})
    ]),

    html.Div([
        dcc.Graph(id="grafico-categorias"),
        dcc.Graph(id="grafico-tipos"),
    ]),

    html.H3("📋 Datos Filtrados"),
    dash_table.DataTable(
        id="tabla-datos",
        columns=[{"name": col, "id": col} for col in df_default.columns],
        page_size=10,
        style_table={"overflowX": "auto"},
        style_cell={"textAlign": "left"},
    )
])

# Callback para actualizar dinámicamente las opciones del Dropdown de categorías
@app.callback(
    Output("filtro-categorias", "options"),
    Input("upload-data", "contents"),
    Input("filtro-fechas", "start_date"),
    Input("filtro-fechas", "end_date"),
)
def actualizar_opciones_categoria(contents, desde, hasta):
    if contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), parse_dates=["Fecha"])
    else:
        df = df_default.copy()

    df = processor.filtrar_por_fecha(df, desde, hasta)
    categorias = sorted(df["Categoría"].dropna().unique())
    return [{"label": cat, "value": cat} for cat in categorias]

# Callback principal para actualizar datos y gráficos
@app.callback(
    Output("tabla-datos", "data"),
    Output("grafico-categorias", "figure"),
    Output("grafico-tipos", "figure"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    Input("filtro-fechas", "start_date"),
    Input("filtro-fechas", "end_date"),
    Input("filtro-categorias", "value")
)
def actualizar_dashboard(contents, filename, desde, hasta, categorias):
    if contents:
        try:
            content_type, content_string = contents.split(",")
            decoded = base64.b64decode(content_string)
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), parse_dates=["Fecha"])
        except Exception:
            return [], px.bar(title="Archivo inválido"), px.pie(title="Archivo inválido")
    else:
        df = df_default.copy()

    df_filtrado = processor.filtrar_por_fecha(df, desde, hasta)
    if categorias:
        df_filtrado = df_filtrado[df_filtrado["Categoría"].isin(categorias)]

    if df_filtrado.empty:
        return [], px.bar(title="Sin datos"), px.pie(title="Sin datos")

    resumen = processor.analizar_gastos(df_filtrado)

    fig_cat = px.bar(
        x=resumen["por_categoria"].index,
        y=resumen["por_categoria"].values,
        labels={"x": "Categoría", "y": "Monto"},
        title="Gastos por Categoría"
    )

    fig_tipo = px.pie(
        names=resumen["por_tipo"].index,
        values=resumen["por_tipo"].values,
        title="Distribución por Tipo de Gasto",
        hole=0.3
    )

    return df_filtrado.to_dict("records"), fig_cat, fig_tipo

if __name__ == "__main__":
    app.run(debug=True)

