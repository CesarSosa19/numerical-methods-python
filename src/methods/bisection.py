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
        print(f"La raiz real es {a}")
        contador = 0
