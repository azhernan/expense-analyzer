import pandas as pd

def analizar_gastos(df):
    # Agrupar por categoría
    por_categoria = df.groupby("Categoría")["Monto"].sum().sort_values(ascending=False)
    
    # Agrupar por tipo de gasto
    por_tipo = df.groupby("Tipo de gasto")["Monto"].sum().sort_values(ascending=False)

    return {
        "por_categoria": por_categoria,
        "por_tipo": por_tipo
    }

def filtrar_por_fecha(df, desde=None, hasta=None):
    """Filtra el DataFrame por un rango de fechas opcional (ambos inclusive)."""
    if desde:
        df = df[df["Fecha"] >= pd.to_datetime(desde)]
    if hasta:
        df = df[df["Fecha"] <= pd.to_datetime(hasta)]
    return df

