# INGRESAR CINCO NÚMEROS
numeros = []

while len(numeros) < 5:
    try:
        num = float(input("Ingrese un número: "))
        numeros.append(num)
    except:
        print("Entrada inválida. Intente de nuevo.")

# ORDENAR LOS NÚMEROS DE MAYOR A MENOR
numeros.sort(reverse=True)

# MOSTRAR RESULTADO
print("Números ordenados de mayor a menor:")
for n in numeros:
    print(n)
