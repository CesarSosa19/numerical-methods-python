from methods.bisection import bisection
from methods.newton import newton_raphson
from methods.secant import secant
# ocupar sympy en lugar de math
import math

def leer_num(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("entrada invalida. Por favor ingresa un numero.")


def menu():
    print("\n" + "=" * 30)
    print("numerical-methods-python")
    print("=" * 30)
    print("1. Método de Bisección")
    print("2. Método de Newton-Raphson")
    print("3. Metodo de secante")
    print("4. Salir")
    print("=" * 30)


def iniciar_programa():
    print("Ingresa la función (usa 'x' y 'math.' para funciones).")
    print("Ejemplo: x**2 - 4")

    funcion_texto = input("f(x) = ")

    try:
        f = eval(f"lambda x: {funcion_texto}", {"math": math})
        f(0)

    except Exception as e:
        print(f"\n Error en la fórmula: {e}")
        print("Asegúrate de usar sintaxis Python (ej: x**2, math.sin(x))")
        return

    while True:
        menu()
        opcion = input("Elige una opción (1-4): ")

        try:
            if opcion == '1':
                print("\n--- Configurando Bisección ---")
                a = leer_num("Ingresa el punto 'a': ")
                b = leer_num("Ingresa el punto 'b': ")
                tol = leer_num("Ingresa la tolerancia (ej. 0.001): ")

                bisection(f, a, b, tol)

            elif opcion == '2':
                print("\n--- Configurando Newton-Raphson ---")
                x0 = leer_num("Ingresa el valor inicial x0: ")
                tol = leer_num("Ingresa la tolerancia (ej. 0.001): ")

                newton_raphson(f, x0, tol)

            elif opcion == '3':
                print("\n--- Configurando Secante ---")
                x0 = leer_num("Ingresa el valor inicial x0: ")
                x1 = leer_num("Ingresa el valor inicial x1: ")
                tol = leer_num("Ingresa la tolerancia (ej. 0.001): ")

                secant(f, x0, x1, tol)

            elif opcion == '4':
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida, intenta de nuevo.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    iniciar_programa()