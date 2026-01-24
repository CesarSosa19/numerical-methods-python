from methods.errors import errors
def newton_raphson(funcion, a, tol, max_iter=100):

    h = 1e-5
    xn = a

    for i in range(max_iter):
        fxn = funcion(xn)
        dfxn = (funcion(xn + h) - funcion(xn)) / h

        if abs(dfxn) < 1e-10:
            print("la derivada es cero. (pendiente horizontal)")
            return None

        xnSiguiente = xn - (fxn / dfxn)
        e_Abs, e_Rel = errors(xnSiguiente, xn)

        print(f"iteracion {i}: x = {xnSiguiente}")

        if e_Rel < tol:
            print(f"Raiz encontrada en {i + 1} iteraciones.")
            print(xnSiguiente)
            return xnSiguiente

        xn = xnSiguiente

    print("se alcanzo el maximo de iteraciones sin converger")
    return xn
