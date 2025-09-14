import sympy as sp

x = sp.Symbol('x')

def analizar_funcion(expr_str, valor_x=None):
    """
    Analiza una función matemática ingresada por el usuario.
    Devuelve un diccionario con dominio, recorrido, intersecciones y evaluación de punto.
    """
    try:
        funcion = sp.sympify(expr_str)

        dominio = sp.calculus.util.continuous_domain(funcion, x, sp.S.Reals)

        try:
            recorrido = sp.calculus.util.function_range(funcion, x, sp.S.Reals)
        except Exception:
            recorrido = "No se pudo calcular simbólicamente"

        intersecciones_x = sp.solve(sp.Eq(funcion, 0), x)
        interseccion_y = funcion.subs(x, 0)

        resultado_punto, pasos_evaluacion = None, ""
        if valor_x is not None:
            sustitucion = funcion.subs(x, valor_x)
            pasos_evaluacion = (
                f"1. Sustituir x = {valor_x}\n"
                f"2. Expresión: {funcion}\n"
                f"3. Resultado: {sustitucion}"
            )
            resultado_punto = (valor_x, sustitucion)

        return {
            "funcion": funcion,
            "dominio": dominio,
            "recorrido": recorrido,
            "intersecciones_x": intersecciones_x,
            "interseccion_y": interseccion_y,
            "resultado_punto": resultado_punto,
            "pasos": pasos_evaluacion
        }

    except Exception as e:
        raise ValueError(f"Error al analizar la función: {e}")
