import random  # Para generar números aleatorios

# GENERAR LISTA DE 20 NÚMEROS ALEATORIOS ENTRE 1 Y 100
lista = [random.randint(1, 100) for _ in range(20)]

# MOSTRAR LA LISTA
print("Lista generada:")
print(lista)

# LEER UN NÚMERO DEL USUARIO
while True:
    try:
        buscado = int(input("Ingrese el número que desea comparar: "))
        break
    except:
        print("Entrada inválida. Intente de nuevo.")

# BUSCAR NÚMERO MAYOR Y SUS OCURRENCIAS
mayor = max(lista)
veces_mayor = lista.count(mayor)

# CONTAR CUÁNTAS VECES APARECE EL NÚMERO INGRESADO
veces_buscado = lista.count(buscado)

# COMPARAR CANTIDADES Y MOSTRAR RESULTADO
print("El número mayor es:", mayor, "y aparece", veces_mayor, "veces.")
print("El número", buscado, "aparece", veces_buscado, "veces.")

if veces_buscado > veces_mayor:
    print("Resultado: Verdadero (el número ingresado aparece más veces que el mayor)")
else:
    print("Resultado: Falso (el número ingresado no aparece más veces que el mayor)")
