import math

def bisection(funcion, a, b, tol):

    contador = 0
    error = b - a
    fa = funcion(a)
    fb = funcion(b)

    if fa * fb > 0:
        print("No existe raiz real en la funcion")
        return None

    else:
        while error > tol:
            x = (a + b)/2
            fx = funcion(x)

            print(f"Iteración {contador}: x = {x}, error = {error}")

            if fa * fx > 0:
                a = x
                fa = fx
            else:
                b = x
            error = error / 2
            contador += 1

        print(f"Raíz encontrada en {contador} iteraciones.")
        return x  # <--- Al final, devolvemos el valor encontrado


def newton_raphson(funcion, a, b, tol):
    print(f"--> Ejecutando Newton-Raphson desde x0={x0}")
    return 0.0

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
    funcion = lambda x: x**2 - 4

    while True:
        menu()
        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            print("\n--- Configurando Bisección ---")
            a = float(input("Ingresa el punto 'a': "))
            b = float(input("Ingresa el punto 'b': "))
            tol = float(input("Ingresa la tolerancia (ej. 0.001): "))

            bisection(funcion, a, b, tol)

        elif opcion == '2':
            print("\n--- Configurando Newton-Raphson ---")
            x0 = float(input("Ingresa el valor inicial x0: "))
            tol = float(input("Ingresa la tolerancia: "))

            newton_raphson(funcion, x0, tol)

        elif opcion == '3':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    iniciar_programa()