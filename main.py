# Importaciones
from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

# Carga de directorios
# Directorio principal
carpeta_principal = os.path.dirname(__file__)

# Directorio imagenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")


# Creación de ventana
root = Tk()

# Cambio de título
root.title("Curso Programación Fácil")

# Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "icono.ico"))

# Carga de imagen
paisaje1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "cascada.png")).resize((350,200)))
etiqueta1 = Label(image=paisaje1)
etiqueta1.pack()

# Bucle para mantener la ventana abierta
root.mainloop()

