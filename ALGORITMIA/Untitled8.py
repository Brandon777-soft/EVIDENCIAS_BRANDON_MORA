import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA
print("Lista generada:")
print(lista)

# ENCONTRAR EL NÚMERO MAYOR
mayor = max(lista)

# CONTAR CUÁNTAS VECES APARECE
cantidad = lista.count(mayor)

# MOSTRAR RESULTADO
print("El número mayor es:", mayor)
print("Aparece", cantidad, "veces en la lista.")
