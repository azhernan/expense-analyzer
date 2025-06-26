def generar_reporte(resumen, path="reporte.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Reporte de Gastos\n\n")
        for categoria, monto in resumen.items():
            f.write(f"- {categoria}: ${monto:.2f}\n")
