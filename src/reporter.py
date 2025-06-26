def generar_reporte(resumen, path="reporte.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Reporte de Gastos\n\n")

        f.write("## Gastos por Categoría\n")
        for categoria, monto in resumen["por_categoria"].items():
            f.write(f"- {categoria}: ${monto:.2f}\n")

        f.write("\n## Gastos por Tipo de Gasto\n")
        for tipo, monto in resumen["por_tipo"].items():
            f.write(f"- {tipo}: ${monto:.2f}\n")
