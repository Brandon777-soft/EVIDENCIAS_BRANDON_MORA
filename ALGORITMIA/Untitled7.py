import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA
print("Lista generada:")
print(lista)

# PEDIR UN NÚMERO AL USUARIO
while True:
    try:
        buscado = int(input("Ingrese el número que desea buscar: "))
        break
    except:
        print("Entrada inválida. Intente de nuevo.")

# CONTAR CUÁNTAS VECES APARECE EL NÚMERO
cantidad = lista.count(buscado)

# MOSTRAR RESULTADO
if cantidad > 0:
    print("El número", buscado, "aparece", cantidad, "veces en la lista.")
else:
    print("Número no encontrado.")
