def analizar_gastos(df):
    # Agrupar por categoría
    por_categoria = df.groupby("Categoría")["Monto"].sum().sort_values(ascending=False)
    
    # Agrupar por tipo de gasto
    por_tipo = df.groupby("Tipo de gasto")["Monto"].sum().sort_values(ascending=False)

    return {
        "por_categoria": por_categoria,
        "por_tipo": por_tipo
    }

