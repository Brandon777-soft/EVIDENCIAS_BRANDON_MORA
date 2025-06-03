import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA ORIGINAL
print("Lista original:")
print(lista)

# CREAR LA LISTA INVERSA
lista_invertida = lista[::-1]  # Esta sintaxis invierte la lista

# MOSTRAR LA LISTA INVERSA
print("Lista invertida:")
print(lista_invertida)
