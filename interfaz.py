import tkinter as tk
from tkinter import messagebox
from Analisis import analizar_funcion
from Graficas import graficar_funcion

def iniciar_interfaz():
    """
    Lanza la ventana principal de la aplicación.
    """
    def ejecutar_analisis():
        expr_str = entry_funcion.get()
        valor_x_str = entry_x.get()

        try:
            valor_x = float(valor_x_str) if valor_x_str else None
        except ValueError:
            messagebox.showerror("Error", "El valor de x debe ser numérico.")
            return

        try:
            resultado = analizar_funcion(expr_str, valor_x)

            salida = (
                f"Función: f(x) = {resultado['funcion']}\n"
                f"Dominio: {resultado['dominio']}\n"
                f"Recorrido: {resultado['recorrido']}\n"
                f"Intersecciones con X: {resultado['intersecciones_x']}\n"
                f"Intersección con Y: {resultado['interseccion_y']}\n"
            )

            if resultado["resultado_punto"]:
                salida += (
                    f"\nEvaluación en x = {resultado['resultado_punto'][0]}:\n"
                    f"{resultado['pasos']}"
                )

            text_salida.delete("1.0", tk.END)
            text_salida.insert(tk.END, salida)

            graficar_funcion(
                resultado["funcion"],
                resultado["intersecciones_x"],
                resultado["interseccion_y"],
                resultado["resultado_punto"]
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    ventana = tk.Tk()
    ventana.title("Analizador de Funciones")

    tk.Label(ventana, text="Ingrese función f(x):").pack()
    entry_funcion = tk.Entry(ventana, width=40)
    entry_funcion.pack()

    tk.Label(ventana, text="Ingrese un valor de x (opcional):").pack()
    entry_x = tk.Entry(ventana, width=20)
    entry_x.pack()

    tk.Button(ventana, text="Analizar", command=ejecutar_analisis).pack()

    global text_salida
    text_salida = tk.Text(ventana, height=15, width=70)
    text_salida.pack()

    ventana.mainloop()