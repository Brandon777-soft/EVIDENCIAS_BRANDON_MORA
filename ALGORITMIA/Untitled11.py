import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA
print("Lista generada:")
print(lista)

# ENCONTRAR MAYOR Y MENOR
mayor = max(lista)
menor = min(lista)

# CALCULAR LA MEDIA ENTRE MAYOR Y MENOR
media = (mayor + menor) / 2

# MOSTRAR RESULTADOS
print("El número mayor es:", mayor)
print("El número menor es:", menor)
print("La media entre mayor y menor es:", media)
