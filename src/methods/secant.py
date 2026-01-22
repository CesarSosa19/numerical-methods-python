from src.methods.errors import errors
def secant(funcion, a, b, tol, max_iter=100):

    fa = funcion(a)
    fb = funcion(b)

    for i in range(max_iter):
        denominador = fb - fa

        if denominador == 0:
            print("Error division entre 0")
            return None

        xnuevo = b - (fb * (b - a))/denominador

        e_abs, e_rel = errors(xnuevo, b)
        print(f"Iteración {i+1}: x = {xnuevo}")

        if e_rel < tol:
            print(f"¡Raíz encontrada! en {i + 1} iteraciones.")
            return xnuevo

        a = b
        fa = fb
        b = xnuevo
        fb = funcion(xnuevo)

    print("Se alcanzó el máximo de iteraciones sin converger.")
    return b
