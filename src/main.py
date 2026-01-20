from methods.bisection import bisection
from methods.newton import newton_raphson
import math

def menu():
    print("\n" + "="*30)
    print("numerical-methods-python")
    print("=" * 30)
    print("1. Método de Bisección")
    print("2. Método de Newton-Raphson")
    print("3. Salir")
    print("=" * 30)


def iniciar_programa():
    # f(x) = x^2 - 4
    ## cambiar esto por una derivada dada por el usuario
    funcion = lambda x: x**2 - 4
    derivada = lambda x: 2*x

    while True:
        menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            print("\n--- Configurando Bisección ---")
            a: float = float(input("Ingresa el punto 'a': "))
            b = float(input("Ingresa el punto 'b': "))
            tol = float(input("Ingresa la tolerancia (ej. 0.001): "))

            bisection(funcion, a, b, tol)

        elif opcion == '2':
            print("\n--- Configurando Newton-Raphson ---")
            x0 = float(input("Ingresa el valor inicial x0: "))
            tol = float(input("Ingresa la tolerancia (ej. 0.001): "))

            newton_raphson(funcion, derivada, x0, tol)

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    iniciar_programa()