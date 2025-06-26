from src import loader, processor, visualizer, reporter

def main():
    df = loader.leer_csv("data/gastos.csv")
    
    # FILTRAR: ejemplo de uso con rango de fechas
    desde = "2025-06-02"
    hasta = "2025-06-05"
    df_filtrado = processor.filtrar_por_fecha(df, desde, hasta)

    resumen = processor.analizar_gastos(df_filtrado)
    visualizer.graficar_categoria(resumen)
    visualizer.graficar_tipo(resumen)
    reporter.generar_reporte(resumen)

if __name__ == "__main__":
    main()
