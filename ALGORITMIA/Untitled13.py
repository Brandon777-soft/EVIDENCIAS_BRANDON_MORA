import random

# FUNCIÓN PARA MOSTRAR EL MENÚ
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Mostrar lista")
    print("2. Buscar número en la lista")
    print("3. Contar cuántas veces aparece un número")
    print("4. Mostrar número mayor y cuántas veces aparece")
    print("5. Verificar si un número aparece más veces que el mayor")
    print("6. Calcular la media de todos los números")
    print("7. Calcular la media entre el mayor y el menor")
    print("8. Mostrar la lista invertida")
    print("9. Salir")

# INICIAR BUCLE DEL MENÚ
while True:
    # LA LISTA SE GENERA CADA VEZ QUE SE REPITE EL MENÚ
    lista = [random.randint(1, 100) for _ in range(20)]

    mostrar_menu()
    opcion = input("Seleccione una opción (1-9): ")

    if opcion == "1":
        print("Lista generada:")
        print(lista)

    elif opcion == "2":
        print("Lista generada:")
        print(lista)
        try:
            num = int(input("Ingrese el número a buscar: "))
            if num in lista:
                print("Número encontrado en la posición:", lista.index(num))
            else:
                print("Número no encontrado.")
        except:
            print("Entrada inválida.")

    elif opcion == "3":
        print("Lista generada:")
        print(lista)
        try:
            num = int(input("Ingrese el número a contar: "))
            cantidad = lista.count(num)
            print("El número", num, "aparece", cantidad, "veces.")
        except:
            print("Entrada inválida.")

    elif opcion == "4":
        print("Lista generada:")
        print(lista)
        mayor = max(lista)
        veces = lista.count(mayor)
        print("El número mayor es:", mayor)
        print("Aparece", veces, "veces.")

    elif opcion == "5":
        print("Lista generada:")
        print(lista)
        try:
            num = int(input("Ingrese el número a comparar: "))
            veces_num = lista.count(num)
            mayor = max(lista)
            veces_mayor = lista.count(mayor)
            print("El número mayor es:", mayor, "y aparece", veces_mayor, "veces.")
            print("El número", num, "aparece", veces_num, "veces.")
            if veces_num > veces_mayor:
                print("Resultado: Verdadero")
            else:
                print("Resultado: Falso")
        except:
            print("Entrada inválida.")

    elif opcion == "6":
        print("Lista generada:")
        print(lista)
        media = sum(lista) / len(lista)
        print("La media de los números es:", media)

    elif opcion == "7":
        print("Lista generada:")
        print(lista)
        mayor = max(lista)
        menor = min(lista)
        media_extremos = (mayor + menor) / 2
        print("El número mayor es:", mayor)
        print("El número menor es:", menor)
        print("La media entre ellos es:", media_extremos)

    elif opcion == "8":
        print("Lista generada:")
        print(lista)
        invertida = lista[::-1]
        print("Lista invertida:")
        print(invertida)

    elif opcion == "9":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")

