import argparse
from src import loader, processor, visualizer, reporter

def main():
    parser = argparse.ArgumentParser(description="Analizador de gastos personales")
    parser.add_argument("--desde", help="Fecha de inicio en formato YYYY-MM-DD", required=False)
    parser.add_argument("--hasta", help="Fecha de fin en formato YYYY-MM-DD", required=False)
    args = parser.parse_args()

    df = loader.leer_csv("data/gastos.csv")

    # Aplicar filtro si se pasan argumentos
    df_filtrado = processor.filtrar_por_fecha(df, desde=args.desde, hasta=args.hasta)

    print(f"\n➡️ Filtro aplicado: desde {args.desde or 'inicio'} hasta {args.hasta or 'fin'}")
    print("📊 Gastos filtrados:")
    print(df_filtrado)

    resumen = processor.analizar_gastos(df_filtrado)
    visualizer.graficar_categoria(resumen)
    visualizer.graficar_tipo(resumen)
    reporter.generar_reporte(resumen)

if __name__ == "__main__":
    main()

