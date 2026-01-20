def newton_raphson(funcion, a, tol, max_iter=100):

    h = 1e-5
    xn = a

    for i in range(max_iter):
        fxn = funcion(xn)
        dfxn = (funcion(xn + h) - funcion(xn)) / h

        if abs(dfxn) < 1e-10:
            print("la derivada es cero. (pendiente horizontal)")
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
