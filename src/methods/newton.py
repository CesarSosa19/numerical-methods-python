def newton_raphson(funcion, derivada, a, tol, max_iter=100):

    xn = a

    for i in range(max_iter):
        fxn = funcion(xn)

        ## cambiar esto por una derivada hecha por la computadora
        dfxn = derivada(xn)

        if dfxn == 0:
            print("la derivada es cero. No se puede continuar.")
            return None

        xn_siguiente = xn - (fxn / dfxn)
        print(f"iteracion {i}: x = {xn_siguiente}")

        if abs(xn_siguiente - xn) < tol:
            print(f"Raiz encontrada en {i + 1} iteraciones.")
            print(xn_siguiente)
            return xn_siguiente

        xn = xn_siguiente

    print("se alcanzo el maximo de iteraciones sin converger")
    return xn
