import pandas as pd

def leer_csv(path):
    columnas_esperadas = ["Fecha", "Proveedor", "Monto", "Tipo de gasto", "Categoría"]
    try:
        df = pd.read_csv(path)
        if not all(col in df.columns for col in columnas_esperadas):
            raise ValueError("El archivo no contiene las columnas esperadas.")
        df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce", dayfirst=False)
        return df.dropna(subset=["Fecha"])
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return pd.DataFrame()
