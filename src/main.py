from src import loader, processor, visualizer, reporter

def main():
    df = loader.leer_csv("data/gastos.csv")
    resumen = processor.analizar_gastos(df)
    visualizer.graficar_categoria(resumen)
    reporter.generar_reporte(resumen)

if __name__ == "__main__":
    main()
