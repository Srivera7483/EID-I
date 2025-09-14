import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

def detectar_asintotas_y_huecos(funcion):
    """
    Detecta asíntotas verticales y huecos en la función.
    Retorna dos listas: asintotas, huecos.
    """
    asintotas = []
    huecos = []

    # Denominador (si es racional)
    if funcion.is_rational_function(x):
        numerador, denominador = sp.fraction(funcion)

        # Posibles discontinuidades: raíces del denominador
        raices_den = sp.solve(sp.Eq(denominador, 0), x)
        for r in raices_den:
            if r.is_real:
                # Verificamos si se cancela con el numerador (hueco)
                if numerador.subs(x, r) == 0:
                    huecos.append((float(r), float(sp.limit(funcion, x, r))))
                else:
                    asintotas.append(float(r))

    # Logaritmos → asíntota en x=0
    if funcion.has(sp.log):
        asintotas.append(0.0)

    # Tangente → asíntotas en π/2 + kπ
    if funcion.has(sp.tan):
        for k in range(-5, 6):  # hasta 5 periodos
            valor = sp.pi/2 + k*sp.pi
            asintotas.append(float(valor))

    return sorted(set(asintotas)), huecos


def graficar_funcion(funcion, intersecciones_x, interseccion_y, punto_eval=None):
    """
    Genera una gráfica de la función, marcando intersecciones,
    huecos y asíntotas verticales.
    """
    f_lambd = sp.lambdify(x, funcion, "math")
    xs = [a/50.0 for a in range(-500, 501)]  # Equivalente a linspace(-10, 10, 1001)

    ys = []
    for val in xs:
        try:
            ys.append(f_lambd(val))
        except:
            ys.append(float('nan'))

    # Detectar huecos y asíntotas
    asintotas, huecos = detectar_asintotas_y_huecos(funcion)

    plt.figure(figsize=(7, 5))
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    # Graficar curva principal
    plt.plot(xs, ys, label=f"f(x) = {funcion}", color="blue")

    # Intersecciones con X
    for r in intersecciones_x:
        if r.is_real:
            plt.scatter(float(r), 0, color="red", zorder=5)
            plt.text(float(r), 0, f"({float(r):.2f},0)", fontsize=8, color="red")

    # Intersección con Y
    plt.scatter(0, float(interseccion_y), color="green", zorder=5)
    plt.text(0, float(interseccion_y), f"(0,{float(interseccion_y):.2f})", fontsize=8, color="green")

    # Punto evaluado
    if punto_eval:
        plt.scatter(punto_eval[0], float(punto_eval[1]), color="purple", zorder=5)
        plt.text(punto_eval[0], float(punto_eval[1]), f"{punto_eval}", fontsize=8, color="purple")

    # Dibujar huecos
    for hx, hy in huecos:
        plt.scatter(hx, hy, facecolors="none", edgecolors="orange", s=100, zorder=6, label="Hueco")

    # Dibujar asíntotas verticales
    for a in asintotas:
        plt.axvline(a, color="gray", linestyle="--", linewidth=1, label="Asíntota")

    plt.title("Gráfica de la función")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()