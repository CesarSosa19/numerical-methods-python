import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def graph(f, raiz, x_min, x_max):
    x = np.linspace(x_min - 1, x_max + 1, 500)

    try:
        y = [f(i) for i in x]
    except:
        x = np.linspace(raiz - 0.5, raiz + 0.5, 500)
        y = [f(i) for i in x]

    plt.figure(figsize=(10, 6))

    plt.plot(x, y, label='f(x)', color='#1f77b4', linewidth=2)
    plt.axhline(0, color='black', linestyle='-', linewidth=1)

    plt.scatter([raiz], [f(raiz)], color='red', s=100, label=f'Raíz aproximada: {raiz:.6f}', zorder=5)

    plt.title('Representación Gráfica del Resultado')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()