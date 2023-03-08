class Motocicleta():
    estado = "Nueva"
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    def arrancar(self):
        if self.motor == False:
            self.motor = True
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba arrancado")

    def detener(self):
        if self.motor:
            self.motor = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")

    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} {self.modelo}, es de {self.precio}")

motito = Motocicleta("Rojo", "2342jkj", 10, 2, "Yamaha", "XZ8", 2021, 100, 350)
motito.precio = "3500€"

motito2 = Motocicleta(
    matricula="23423-erw",
    combustible_litros=0,
    color= "Negro",
    marca="Harley",
    modelo="Fat",
    numero_ruedas=2,
    peso=304,
    fecha_fabricacion=2022,
    velocidad_punta=160
)

motito.consulta_precio()
motito2.consulta_precio()