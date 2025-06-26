import matplotlib.pyplot as plt

def graficar_categoria(resumen):
    resumen.plot(kind="bar")
    plt.title("Gastos por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Monto")
    plt.tight_layout()
    plt.show()
