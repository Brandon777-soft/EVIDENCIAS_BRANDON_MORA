# INGRESAR NÚMERO ENTERO
while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        break
    except:
        print("Entrada inválida. Intente nuevamente.")

# CONVERTIR A POSITIVO (por si es negativo)
numero = abs(numero)

# CONTAR CIFRAS
cifras = len(str(numero))

# MOSTRAR RESULTADO
print("El número tiene", cifras, "cifras.")
