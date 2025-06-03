# INGRESAR LOS DOS NÚMEROS
while True:
    try:
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        break
    except:
        print("Entrada inválida. Intente de nuevo.")

# DETERMINAR EL RANGO CORRECTO
inicio = min(a, b)
fin = max(a, b)

# CALCULAR LA SUMA DE LOS PARES ENTRE 'inicio' Y 'fin'
suma = 0
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        suma += num

# MOSTRAR RESULTADO
print("La suma de los números pares entre", inicio, "y", fin, "es:", suma)
