class Vehiculo():
    def __init__(self, ruedas="4", puertas="5", color="negro", asientos="5"):
        self.ruedas = ruedas
        self.puertas = puertas
        self.color = color
        self.asientos = asientos

    def describe(self):
        print(f"Ruedas: {self.ruedas}.")
        print(f"Puertas: {self.puertas}.")
        print(f"Color: {self.color}.")
        print(f"Asientos: {self.asientos}.")

coche = Vehiculo()
coche.describe()

coche2 = Vehiculo(4, 3, "rojo", 4)
coche2.describe()