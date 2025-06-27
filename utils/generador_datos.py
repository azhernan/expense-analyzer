import pandas as pd
from datetime import datetime, timedelta
import random

def generar_csv_de_prueba(ruta_salida="data/gastos_test.csv", cantidad=20):
    categorias = ["Comida", "Transporte", "Salud", "Entretenimiento", "Servicios", "Educación"]
    proveedores = {
        "Comida": ["Supermercado La Esquina", "Verdulería Central"],
        "Transporte": ["Uber", "Subte CABA"],
        "Salud": ["Farmacia Salud", "Clínica San José"],
        "Entretenimiento": ["Spotify", "Netflix"],
        "Servicios": ["Edesur", "Aysa", "Claro"],
        "Educación": ["Platzi", "Coursera"]
    }
    tipos = ["Fijo", "Variable"]
    base_date = datetime(2025, 6, 1)

    gastos = []
    for _ in range(cantidad):
        categoria = random.choice(categorias)
        proveedor = random.choice(proveedores[categoria])
        fecha = base_date + timedelta(days=random.randint(0, 15))
        monto = random.randint(2000, 20000)
        tipo = random.choice(tipos)
        gastos.append([fecha.date(), proveedor, monto, tipo, categoria])

    df = pd.DataFrame(gastos, columns=["Fecha", "Proveedor", "Monto", "Tipo de gasto", "Categoría"])
    df.to_csv(ruta_salida, index=False)
    print(f"✅ Archivo generado en {ruta_salida}")

if __name__ == "__main__":
    generar_csv_de_prueba()
