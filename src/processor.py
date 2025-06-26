def analizar_gastos(df):
    resumen = df.groupby("Categoría")["Monto"].sum().sort_values(ascending=False)
    return resumen
