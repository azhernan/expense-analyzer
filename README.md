# 🧾 Expense Analyzer

Este proyecto es un analizador de gastos personales hecho en Python. Permite cargar un archivo CSV con tus gastos y obtener un resumen con estadísticas por categoría y tipo, visualizaciones simples, filtros por fecha y un reporte en Markdown.

Ideal para practicar estructuras, visualización de datos, modularización de código y control de versiones con Git.

---

## 🚀 Características

- 📂 Carga de gastos desde archivo CSV local o subida vía interfaz Streamlit o Dash
- 📅 Filtrado por rango de fechas
- 📂 Filtro interactivo por categoría (con actualización dinámica)
- 📊 Agrupación de gastos por categoría
- 🧾 Agrupación por tipo de gasto (fijo/variable)
- 📈 Visualización de gastos en gráficos de barras y tortas
- 📝 Generación de reporte en formato Markdown
- 🧪 Pruebas unitarias básicas
- 🔧 Estructura modular y extensible
- 💻 Dos interfaces: consola, Streamlit y Dash

---

## 📁 Estructura del proyecto

```
expense-analyzer/
├── data/                     # Archivos de entrada (CSV)
│   └── gastos.csv            # Archivo principal
├── src/                      # Código fuente
│   ├── loader.py
│   ├── processor.py
│   ├── visualizer.py
│   ├── reporter.py
│   └── main.py
├── apps/                     # Dashboards interactivos
│   ├── streamlit_app.py
│   └── dash_app.py
├── utils/                    # Herramientas de prueba
│   └── generador_datos.py   # Genera datos de ejemplo en CSV
├── tests/                    # Pruebas unitarias
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🛠️ Requisitos

- Python 3.10+
- pandas
- matplotlib
- streamlit
- dash

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

```bash
python -m src.main
python -m src.main --desde 2025-06-02
python -m src.main --desde 2025-06-02 --hasta 2025-06-04
```

---

## 🖥️ Dashboard Streamlit

```bash
streamlit run apps/streamlit_app.py
```

Funciones:

- Filtros por fecha y categoría
- Visualización de datos desde archivo local o CSV subido
- Gráficos y tabla filtrada

---

## 📊 Dashboard Plotly Dash

```bash
python apps/dash_app.py
```

Funciones:

- Carga de CSV dinámica (drag & drop)
- Filtros actualizables por fecha y categoría
- Visualización en gráfico de barras y torta
- Tabla con datos filtrados

---

## 🧪 Generar archivo de prueba

Podés crear un archivo CSV ficticio con 20 registros aleatorios:

```bash
python utils/generador_datos.py
```

Esto genera `data/gastos_test.csv` para probar sin datos reales.

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

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo `LICENSE`.

---

## 🙋‍♂️ Autor

Desarrollado por Hernán Velázquez · [GitHub](https://github.com/azhernan)

---

## 🟢 Estado del proyecto

✅ Funcional, con dashboards integrados y en evolución activa.
