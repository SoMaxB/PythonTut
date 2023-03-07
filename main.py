colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}

colores[5] = "blanco"

for color in colores:
    print(f"{color} - {colores[color].capitalize()}")