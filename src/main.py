from methods.bisection import bisection
from methods.newton import newton_raphson
from methods.secant import secant
from methods.visualizer import graph
import math

# verifica que el input del usuario sea un numero
def verification(message):
    while True:
        try:
            return float(input(message))
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


def start():
    print("Ingresa la función (usa 'x' y 'math.' para funciones).")
    print("Ejemplo: x**2 - 4")

    functionText = input("f(x) = ")

    #verifica la funcion dada por el usuario y la comprueba evaluandola con 0
    try:
        f = eval(f"lambda x: {functionText}", {"math": math})
        f(0)

    #Si el try de la formula da error se lo notifica al usuario
    except Exception as e:
        print(f"\n Error en la fórmula: {e}")
        print("Asegúrate de usar sintaxis Python (ej: x**2, math.sin(x))")
        return

    #en caso de cumplir con lo anterior se inicia el bucle del menu
    while True:
        menu()
        opcion = input("Elige una opción (1-4): ")

        try:
            if opcion == '1':
                print("\n--- Configurando Bisección ---")
                a = verification("Ingresa el punto 'a': ")
                b = verification("Ingresa el punto 'b': ")
                tol = verification("Ingresa la tolerancia (ej. 0.001): ")

                bisection(f, a, b, tol)

                # crea una variable resultado para poder definir si se obtuvo algo o se regreso vacia
                res = bisection(f, a, b, tol)

                if res is not None:
                    graph(f, res, a, b)

            elif opcion == '2':
                print("\n--- Configurando Newton-Raphson ---")
                x0 = verification("Ingresa el valor inicial x0: ")
                tol = verification("Ingresa la tolerancia (ej. 0.001): ")

                newton_raphson(f, x0, tol)

                res = newton_raphson(f, x0, tol)

                if res is not None:
                    graph(f, res, x0, tol)

            elif opcion == '3':
                print("\n--- Configurando Secante ---")
                x0 = verification("Ingresa el valor inicial x0: ")
                x1 = verification("Ingresa el valor inicial x1: ")
                tol = verification("Ingresa la tolerancia (ej. 0.001): ")

                secant(f, x0, x1, tol)

                res = secant(f, x0, x1, tol)

                if res is not None:
                    graph(f, res, min(x0, x1), max(x0,x1))

            elif opcion == '4':
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida, intenta de nuevo.")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")

if __name__ == "__main__":
    start()