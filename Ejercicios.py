import os.path
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Programación Fácil")

carpeta_base = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_base, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")

imagenes = ["pradera.jpg", "laguna.jpg", "montaña.jpg", "nevado.jpg"]

cargaimagen1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{imagenes[0]}")).resize((400,250)))
etiqueta1 = Label(image=cargaimagen1)
etiqueta1.grid(row=0, column=0)

cargaimagen2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{imagenes[1]}")).resize((400,250)))
etiqueta2 = Label(image=cargaimagen2)
etiqueta2.grid(row=0, column=1)

cargaimagen3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{imagenes[2]}")).resize((400,250)))
etiqueta3 = Label(image=cargaimagen3)
etiqueta3.grid(row=1, column=0)

cargaimagen4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, f"{imagenes[3]}")).resize((400,250)))
etiqueta4 = Label(image=cargaimagen4)
etiqueta4.grid(row=1, column=1)


root.iconbitmap("imagenes/icono.ico")

root.mainloop()