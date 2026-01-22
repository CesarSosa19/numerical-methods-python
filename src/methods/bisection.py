from src.methods.errors import errors
def bisection(funcion, a, b, tol, max_iter=100):
    xanterior = a
    fa = funcion(a)
    fb = funcion(b)

    for i in range(max_iter):
        xnueva = (a + b) / 2

        if i > 1:
            e_abs, e_rel = errors(xnueva, xanterior)

            if e_rel < tol:
                print(f"raiz encontrada: {xnueva}")
                return xnueva
        else:
            print(f"{i:<5} | {xnueva:<12.8f} | {'----------':<15}")


        if fa * funcion(xnueva) < 0:
            b = xnueva
        else:
            a = xnueva

        xanterior = xnueva

    return xnueva