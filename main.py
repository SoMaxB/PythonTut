print("-> Pizzería PF <-")

precio = 0

dinero = int(input("Cuanto dinero tiene para comprar pizzas?:\n"))

margarita = 9
salami = 11
bacon = 13

elecciones = input("Elige una pizza:\n1) Margarita\n2) Salami\n3) Bácon\n")

for eleccion in elecciones:
    if eleccion == 1:
        print(f"Tu pizza cuesta: {margarita}")
    elif eleccion == 2:
        print(f"Tu pizza cuesta: {salami}")
    elif eleccion == 3:
        print(f"Tu pizza cuesta: {bacon}")
print(eleccion)

respuesta = True

input("Desea añadir algún ingrediente:\n")
if respuesta == "No":
    #respuesta = False
    print(f"El valor de su pedido es: {precio}")
elif respuesta == "Si":
    input("Puede elegir entre:\n-Huevo\n-Atún\n-Jamón")
    if respuesta == "Huevo":
        precio += 1
    elif respuesta == "Atún":
        precio += 2
    elif respuesta == "Jamón":
        precio += 1

ingredientes = ["Huevo", "Atún", "Jamón"]

'''for ingrediente in ingredientes:
    ingredientes += str(1)

precio_final = eleccion + ingrediente'''

cambio = dinero - precio

print(f"El valor de su pedido es: {precio}€, usted ha pagado con {dinero}€, su cambio es: {cambio}€")