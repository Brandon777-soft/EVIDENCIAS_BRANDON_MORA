# INGRESAR TEXTO DESDE TECLADO
texto = input("Ingrese un texto: ")

# DIVIDIR TEXTO EN PALABRAS (separadas por espacio)
palabras = texto.split()

# CONTAR PALABRAS
cantidad_palabras = len(palabras)

# ENCONTRAR TAMAÑO DE LA PALABRA MÁS LARGA
tamaño_max = 0
for palabra in palabras:
    if len(palabra) > tamaño_max:
        tamaño_max = len(palabra)

# MOSTRAR RESULTADOS
print("Cantidad de palabras:", cantidad_palabras)
print("Tamaño de la palabra más larga:", tamaño_max)
