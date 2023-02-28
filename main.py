print("##############################")
print("###- Calculadora mejorada -###")
print("##############################")

operacion = input("Hola, elija una opción:\n1 - Suma\n2 - Resta\n3 - Multiplicación\n4 - División\n5 - Módulo\n6 - Exponente\nTeclee un número y pulse ENTER\n")


print(f"Ha elegido la opción {operacion}")

primero = int(input("Especifique el primer operador:\n"))
segundo = int(input("Especifique el segundo operador:\n"))

match operacion:
    case "1":
        print("Ha seleccionado suma")
        print(f"La suma es {primero + segundo}")
    case "2":
        print("Ha seleccionado resta")
        print(f"La resta es {primero - segundo}")
    case "3":
        print(f"La multiplicacion es {primero * segundo}")
    case "4":
        print(f"La división es {primero / segundo}")
    case "5":
        print(f"El módulo es {primero % segundo}")
    case "6":
        print(f"El exponente es {primero ** segundo}")
    case _:
        print("Opción incorrecta")
