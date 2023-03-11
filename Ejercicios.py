#Importaciones
import tkinter
from tkinter import *
import os
from PIL import ImageTk, Image
import getpass

#---Carga de directorios---
#Carpeta principal
carpeta_principal = os.path.dirname(__file__)

#Imágenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")


#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("LabelFrame")
#Icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "icono.ico"))

#Contenido de la ventana principal
# Marco
marco1 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="green"
                    ).grid(row=0, column=0)

marco2 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="deepskyblue"
                    ).grid(row=0, column=1)

marco3 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="green"
                    ).grid(row=0, column=2)

marco4 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="deepskyblue"
                    ).grid(row=1, column=0)

marco5 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="green"
                    ).grid(row=1, column=1)

marco6 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="deepskyblue"
                    ).grid(row=1, column=2)

marco7 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="green"
                    ).grid(row=2, column=0)

marco8 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="deepskyblue"
                    ).grid(row=2, column=1)

marco9 = LabelFrame(root,
                    width=50,
                    height=50,
                    border=False,
                    background="green"
                    ).grid(row=2, column=2)

#Bucle de ejecución
root.mainloop()