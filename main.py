# Importaciones
from tkinter import *

# Creación de ventana
root = Tk()

# Cambio de título
root.title("Curso Programación Fácil")

# Labels
etiqueta_nombre = Label(root, text="Nombre: ").grid(row=0, column=0)
etiqueta_edad = Label(root, text="Edad: ").grid(row=1, column=0)


# Evento para el botón
def crear_etiqueta():
    etiqueta = Label(root, text=f"Nombre: {nombre.get()}\nEdad: {edad.get()}").grid(row=3, column=1)


# Entradas
nombre = Entry(root)
nombre.grid(row=0, column=1)

edad = Entry(root)
edad.grid(row=1, column=1)

# Creación de botón
boton1 = Button(root, text="Pulsar", command=crear_etiqueta).grid(row=2, column=1)


# Bucle para mantener la ventana abierta
root.mainloop()