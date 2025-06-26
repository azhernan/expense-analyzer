import matplotlib.pyplot as plt

def graficar_categoria(resumen):
    resumen["por_categoria"].plot(kind="bar", title="Gastos por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()

def graficar_tipo(resumen):
    resumen["por_tipo"].plot(kind="pie", autopct="%1.1f%%", title="Distribución por Tipo de Gasto")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
