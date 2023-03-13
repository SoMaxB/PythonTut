# Importaciones
from tkinter import *
import os
from PIL import ImageTk, Image

# Creación de ventana
root = Tk()
root.configure(background="red")

# Cambio de título
root.title("Curso Programación Fácil")

opcion = StringVar()
opcion.set("Error")


carpeta_sistema = os.path.dirname(__file__)
carpeta_perros = os.path.join(carpeta_sistema, "perros")

imagenboton = ImageTk.PhotoImage(Image.open(os.path.join("buttonpag.png")))

def actualiza_radio():
    if opcion.get() == "Error":
        Label(root, text=f"No has seleccionado ninguna cuenta", background="gray98", foreground="red2").pack()
    else:
        Label(root, text=f"Hola {opcion.get()}. Accediendo a tu cuenta...", background="gray98").pack()

marco_perros = LabelFrame(root, text="Cual eres?" ,padx=15, pady=20, background="red", border=0)
marco_perros.pack(padx=10, pady=10)

# Radiobutton
perro1 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_perros, "perro1.jpg")).resize((200, 225)))
etiqueta = Label(marco_perros, image=perro1, background="red")
etiqueta.grid(row=0, column=0)
Radiobutton(marco_perros, text="Emma", variable=opcion, value="Emma", background="green").grid(row=1, column=0)

perro2 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_perros, "perro2.jpg")).resize((200, 225)))
etiqueta = Label(marco_perros,image=perro2, background="red")
etiqueta.grid(row=0, column=1)
Radiobutton(marco_perros, text="Jacob", variable=opcion, value="Jacob", background="blue").grid(row=1, column=1)

perro3 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_perros, "perro3.jpg")).resize((200, 225)))
etiqueta = Label(marco_perros,image=perro3, background="red")
etiqueta.grid(row=3, column=0)
Radiobutton(marco_perros, text="Noah", variable=opcion, value="Noah", background="gray").grid(row=4, column=0)

perro4 = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_perros, "perro4.jpg")).resize((200, 225)))
etiqueta = Label(marco_perros,image=perro4, background="red")
etiqueta.grid(row=3, column=1)
Radiobutton(marco_perros, text="Sophia", variable=opcion, value="Sophia", background="orange").grid(row=4, column=1)

boton = Button(root, command=actualiza_radio, image=imagenboton, border=0, background="red").pack(pady=10)



#boton_envia = Button(root, text="Enviar", command=lambda : actualiza_radio(opcion.get())).pack()

# Bucle para mantener la ventana abierta
root.mainloop()

