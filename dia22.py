def muestra_datos(**kwargs):
    claves = tuple(kwargs.keys())
    valores = tuple(kwargs.values())

    print(f"El {claves[0]} es {valores[0]}, sus {claves[1]} son {valores[1]} y tiene {valores[2]} años de {claves[2]}")

usuario1 = {"nombre": "Javier", "Apellidos": "Gomez de la Barca", "edad": "27"}

usuario2 = {"nombre": "Andrea", "Apellidos": "Pedraza Peña", "edad": "31"}

muestra_datos(**usuario1)
muestra_datos(**usuario2)