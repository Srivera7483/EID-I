# EID-I
Analizador de Funciones en Python
📌 Descripción

Este proyecto corresponde a la Parte B del EID – Unidad 2 (Funciones).
Se trata de un analizador de funciones matemáticas con interfaz gráfica, desarrollado en Python, que permite:

Ingresar una función 
𝑓
(
𝑥
)
f(x).

Calcular y mostrar:

Dominio.

Recorrido.

Intersecciones con los ejes.

Evaluar un punto 
𝑥
x mostrando el cálculo paso a paso.

Generar una gráfica profesional con Matplotlib.

Manejar errores de entrada de manera robusta.

El programa utiliza Sympy para el análisis simbólico, Matplotlib para las gráficas y Tkinter para la interfaz.

🛠 Tecnologías utilizadas

Python 3.10+

Sympy
 – álgebra simbólica.

Matplotlib
 – gráficos.

Tkinter
 – interfaz gráfica.

NumPy
 – soporte en cálculos numéricos (solo usado internamente por sympy/matplotlib).

📂 Estructura del proyecto
analizador_funciones/
│── main.py          # Punto de entrada
│── analisis.py      # Lógica matemática (dominio, recorrido, etc.)
│── graficas.py      # Generación de gráficos
│── interfaz.py      # Interfaz gráfica Tkinter
│── README.md        # Documentación

🚀 Instalación y ejecución

Clonar el repositorio

git clone https://github.com/usuario/analizador-funciones.git
cd analizador-funciones


Crear entorno virtual (opcional pero recomendado)

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows


Instalar dependencias

pip install sympy matplotlib


Ejecutar el programa

python main.py

📖 Uso

Ingresar la función en el campo de texto, por ejemplo:

x**2 - 4

(x**2 - 1)/(x + 2)

(Opcional) Ingresar un valor de x para evaluar.

Hacer clic en Analizar.

El programa mostrará:

Dominio.

Recorrido.

Intersecciones con los ejes.

Evaluación paso a paso (si se ingresó un valor de x).
Además abrirá una ventana con la gráfica de la función.
