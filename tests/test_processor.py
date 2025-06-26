import pandas as pd
from src import processor

def test_analizar_gastos():
    data = {
        "Categoría": ["Comida", "Transporte", "Comida"],
        "Monto": [1000, 500, 1500]
    }
    df = pd.DataFrame(data)
    resumen = processor.analizar_gastos(df)
    assert resumen["Comida"] == 2500
    assert resumen["Transporte"] == 500
