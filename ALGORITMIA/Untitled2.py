# INGRESAR NÚMERO
while True:
    try:
        N = int(input("Ingrese un número: "))
        if N > 0:
            break
        else:
            print("Debe ser un número mayor que cero.")
    except:
        print("Numero Equivocado, Ingrese otro numero")

# CALCULAR LA SUMA 1 + 2 + ... + N
suma = 0
for i in range(1, N + 1):
    suma += i

# MOSTRAR RESULTADO
print("La suma de 1 hasta", N, "es:", suma)
