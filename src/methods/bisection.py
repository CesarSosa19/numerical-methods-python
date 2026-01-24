from methods.errors import errors
def bisection(funcion, a, b, tol, max_iter=100):
    xActual = a
    fa = funcion(a)
    fb = funcion(b)

    for i in range(max_iter):
        xNueva = (a + b) / 2

        if i > 1:
            e_abs, e_rel = errors(xNueva, xActual)

            if e_rel < tol:
                print(f"raiz encontrada: {xNueva}")
                return xNueva
        else:
            print(f"{i:<5} | {xNueva:<12.8f} | {'----------':<15}")


        if fa * funcion(xNueva) < 0:
            b = xNueva
        else:
            a = xNueva

        xActual = xNueva

    return xNueva