def leer_csv(path):
    import pandas as pd

    columnas_esperadas = ["Fecha", "Proveedor", "Monto", "Tipo de gasto", "Categoría"]
    try:
        df = pd.read_csv(path)
        if not all(col in df.columns for col in columnas_esperadas):
            raise ValueError("El archivo no contiene las columnas esperadas.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return pd.DataFrame()
