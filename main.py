from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title("Curso Tkinter de Programación Fácil")

def muestra_info():
    showwarning("Programación Fácil", "Este es el mensaje que se muestra en la ventana")

boton = Button(root, text="Enviar", width=75, command=muestra_info).pack()

root.mainloop()