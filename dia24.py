# Funciones decoradoras
def a(b):
    def c():
        print(f"El resultado de la operacion es: ")
        b()
        print("Operación realizada con éxito.")
    return c

@a
def sumar():
    print(10 + 10)

@a
def restar():
    print(10 - 20)

@a
def multiplicar():
    print(45 * 2)

@a
def dividir():
    print(4 / 87)

dividir()