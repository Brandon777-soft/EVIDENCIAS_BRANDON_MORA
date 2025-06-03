import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA
print("Lista generada:")
print(lista)

# CALCULAR LA MEDIA
suma = sum(lista)               # Suma de todos los elementos
cantidad = len(lista)          # Cantidad de elementos (debería ser 20)
media = suma / cantidad        # Fórmula de la media

# MOSTRAR RESULTADO
print("La media de los números es:", media)
