class Usuario:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def describe(self):
        print(f"Nombre: {self.nombre}.")
        print(f"Apellidos: {self.apellidos}.")
        print(f"Edad : {self.edad}.")

usuario1 = Usuario("Paula", "Cabello Prados", "30")
usuario1.describe()