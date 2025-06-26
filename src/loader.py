import pandas as pd

def leer_csv(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
        return pd.DataFrame()
