# 🧾 Expense Analyzer

Este proyecto es un analizador de gastos personales hecho en Python. Permite cargar un archivo CSV con tus gastos y obtener un resumen con estadísticas por categoría, visualizaciones simples y un reporte en Markdown.

Ideal para practicar estructuras, visualización de datos, modularización de código y control de versiones con Git.

---

## 🚀 Características

- 📂 Carga de gastos desde archivo CSV
- 📊 Agrupación de gastos por categoría
- 📈 Visualización de gastos en gráficos de barras
- 📝 Generación de reporte en formato Markdown
- 🧪 Pruebas unitarias básicas
- 🔧 Estructura modular y extensible

---

## 📁 Estructura del proyecto

```
gastos-analyzer/
├── data/                 # Archivos de entrada (CSV)
├── src/                  # Código fuente
│   ├── loader.py         # Carga de CSV
│   ├── processor.py      # Análisis de datos
│   ├── visualizer.py     # Gráficos
│   ├── reporter.py       # Generador de reporte
│   └── main.py           # Punto de entrada principal
├── tests/                # Pruebas
├── README.md             # Este archivo
├── requirements.txt      # Dependencias
├── .gitignore
└── LICENSE
```

---

## 🛠️ Requisitos

- Python 3.10+
- pandas
- matplotlib

Podés instalar las dependencias con:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Desde la raíz del proyecto, ejecutá:

```bash
python -m src.main
```

Esto cargará el archivo `data/gastos.csv`, procesará los datos y generará:
- Un gráfico con los gastos por categoría
- Un archivo `reporte.md` con el resumen

---

## 🧪 Tests

Desde la raíz del proyecto podés correr los tests con:

```bash
python -m unittest tests/test_processor.py
```

---

## 📌 Ejemplo de entrada (`gastos.csv`)

```csv
Fecha,Categoría,Monto
2025-06-01,Alquiler,50000
2025-06-02,Comida,12000
2025-06-03,Transporte,3000
2025-06-04,Comida,8000
2025-06-05,Entretenimiento,5000
```

---

## 📈 Futuras mejoras

- Filtros por fecha
- Exportación a Excel
- Clasificador automático de gastos
- Dashboard interactivo con Plotly/Dash o Streamlit
- Conexión con OCR y Google Sheets

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE`.

---

## 🙋‍♂️ Autor

Desarrollado por Hernán Velázquez · [GitHub](https://github.com/azhernan)

---

## 🟢 Estado del proyecto

✅ Funcional y listo para extenderse
