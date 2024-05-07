import tkinter as tk
from PIL import ImageTk, Image

# Función para realizar cálculos
def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("Error")

# Función para agregar números y operadores
def agregar(valor):
    entrada.config(state="normal")
    expresion.append(valor)
    if len(expresion) >= 2 and expresion[-1] in ['+', '-', '*', '/'] and expresion[-2] in ['+', '-', '*', '/']:
        entrada.delete(len(entrada.get()) - 1)
        entrada.insert(tk.END, valor)
        expresion[-1] = valor
    else:
        entrada.insert(tk.END, valor)
    entrada.config(state="readonly")

# Función para borrar el último número ingresado
def borrar_ultimo():
    if len(expresion) > 0:
        entrada.config(state="normal")
        entrada.delete(len(entrada.get()) - 1)
        expresion.pop()
        entrada.config(state="readonly")

# Función para borrar toda la entrada
def borrar_todo():
    entrada.config(state="normal")
    entrada.delete(0, tk.END)
    del expresion[:]
    entrada.config(state="readonly")

# Función para agregar números desde el teclado
def agregar_desde_teclado(event):
    if event.char.isdigit() or event.char in ['+', '-', '*', '/', '.', '=']:
        agregar(event.char)
    elif event.keysym == 'Return':
        calcular()

def obtener_dimensiones_ventana(root):
    ancho = root.winfo_width()
    largo = root.winfo_height()
    return ancho, largo
# Configuración de la ventana principal
root = tk.Tk()
root.title("CalcuMay ❤️🌻❤️")
root.configure(bg="#EF77FB")
root.resizable(width=False, height=False)  # Deshabilitar la redimensión
root.iconbitmap("./images/icono.ico")

# Cargar la imagen PNG
ancho, largo = obtener_dimensiones_ventana(root)
ancho = ancho * 2
largo = largo * 2
imagen_fondo = Image.open("./images/Fondo.png")
imagen_fondo = imagen_fondo.resize((ancho, largo), Image.NEAREST)  # Ajustar tamaño de la imagen si es necesario

# Convertir la imagen a un formato compatible con tkinter
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget Label para mostrar la imagen de fondo
label_fondo = tk.Label(root, image=imagen_fondo_tk, bg="#EF77FB")
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Variable para mostrar el resultado
resultado = tk.StringVar()

# Lista para almacenar la expresión ingresada
expresion = []

# Entrada para ingresar expresiones
entrada = tk.Entry(root, textvariable=resultado, bg="#DCDCDC", justify=tk.RIGHT, font=('Arial 24'), state="readonly")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Borrar', 5, 1), ('C', 5, 0)
]

# Crear botones y agregarlos a la ventana
for valor, fila, columna in botones:
    if valor == 'Borrar':
        btn = tk.Button(root, text=valor, command=borrar_ultimo, width=12, height=2, bg="#ED9AE1")
    elif valor == 'C':
        btn = tk.Button(root, text=valor, command=borrar_todo, width=12, height=2, bg="#ED9AE1")
    elif valor == '=':
        btn = tk.Button(root, text=valor, command=calcular, width=12, height=2, bg="#ED9AE1")
    else:
        btn = tk.Button(root, text=valor, command=lambda v=valor: agregar(v), width=12, height=2, bg="#ED9AE1")
    btn.grid(row=fila, column=columna, padx=5, pady=5)

# Vincular función para agregar desde el teclado
root.bind('<Key>', agregar_desde_teclado)

root.mainloop()