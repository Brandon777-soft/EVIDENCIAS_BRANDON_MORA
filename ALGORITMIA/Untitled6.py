import random  # Importar para poder generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA GENERADA
print("Lista generada:")
print(lista)

# PEDIR UN NÚMERO AL USUARIO
while True:
    try:
        buscado = int(input("Ingrese el número que desea buscar: "))
        break
    except:
        print("Entrada inválida. Intente de nuevo.")

# BUSCAR EL NÚMERO EN LA LISTA
if buscado in lista:
    posicion = lista.index(buscado)
    print("Número encontrado en la posición:", posicion)
else:
    print("Número no encontrado")
