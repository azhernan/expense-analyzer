import matplotlib.pyplot as plt

def graficar_categoria(resumen):
    fig, ax = plt.subplots()
    resumen["por_categoria"].plot(kind="bar", ax=ax, title="Gastos por Categoría")
    ax.set_xlabel("Categoría")
    ax.set_ylabel("Monto")
    plt.tight_layout()
    return fig

def graficar_tipo(resumen):
    fig, ax = plt.subplots()
    resumen["por_tipo"].plot(
        kind="pie", autopct="%1.1f%%", ax=ax, title="Distribución por Tipo de Gasto"
    )
    ax.set_ylabel("")
    plt.tight_layout()
    return fig
