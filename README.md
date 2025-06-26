# 🧾 Expense Analyzer

Este proyecto es un analizador de gastos personales hecho en Python. Permite cargar un archivo CSV con tus gastos y obtener un resumen con estadísticas por categoría y tipo, visualizaciones simples, filtros por fecha y un reporte en Markdown.

Ideal para practicar estructuras, visualización de datos, modularización de código y control de versiones con Git.

---

## 🚀 Características

- 📂 Carga de gastos desde archivo CSV
- 🗂️ Filtrado por rango de fechas
- 📊 Agrupación de gastos por categoría
- 🧾 Agrupación por tipo de gasto (fijo/variable)
- 📈 Visualización de gastos en gráficos de barras y tortas
- 📝 Generación de reporte en formato Markdown
- 🧪 Pruebas unitarias básicas
- 🔧 Estructura modular y extensible
- 💻 Ejecución desde consola con argumentos

---

## 📁 Estructura del proyecto

```
gastos-analyzer/
├── data/                 # Archivos de entrada (CSV)
├── src/                  # Código fuente
│   ├── loader.py         # Carga de CSV
│   ├── processor.py      # Análisis de datos y filtros
│   ├── visualizer.py     # Gráficos
│   ├── reporter.py       # Generador de reporte
│   └── main.py           # Punto de entrada principal
├── tests/                # Pruebas
├── apps/                 # Dashboards interactivos
│   ├── streamlit_app.py  # (próximamente)
│   └── dash_app.py       # (opcional)
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

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución por consola

```bash
python -m src.main [--desde YYYY-MM-DD] [--hasta YYYY-MM-DD]
```

### Ejemplos:

- Sin filtro:
  ```bash
  python -m src.main
  ```

- Desde una fecha:
  ```bash
  python -m src.main --desde 2025-06-02
  ```

- Rango de fechas:
  ```bash
  python -m src.main --desde 2025-06-02 --hasta 2025-06-04
  ```

---

## 📌 Formato esperado del archivo `gastos.csv`

```csv
Fecha,Proveedor,Monto,Tipo de gasto,Categoría
2025-06-01,Alquiler S.A.,50000,Fijo,Alquiler
2025-06-02,Supermercado ABC,12000,Variable,Comida
2025-06-03,Taxi CABA,3000,Variable,Transporte
2025-06-04,Supermercado ABC,8000,Variable,Comida
2025-06-05,Netflix,5000,Fijo,Entretenimiento
```

---

## 📈 Futuras mejoras

- Dashboard interactivo con Streamlit
- Exportación a Excel
- Clasificador automático de categoría
- Conexión con OCR y Google Sheets
- Reportes por proveedor o mes

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE`.

---

## 🙋‍♂️ Autor

Desarrollado por Hernán Velázquez · [GitHub](https://github.com/azhernan)

---

## 🟢 Estado del proyecto

✅ Funcional y listo para extenderse
