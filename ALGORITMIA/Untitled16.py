# INGRESAR VALORES
while True:
    try:
        valor = int(input("Ingrese el valor a cobrar: "))
        pagado = int(input("Ingrese el monto entregado: "))
        if pagado < valor:
            print("El monto entregado es insuficiente.")
            continue
        break
    except:
        print("Entrada inválida. Ingrese números enteros.")

# CALCULAR CAMBIO
cambio = pagado - valor
print("Cambio a devolver:", cambio)

# MONEDAS DISPONIBLES
monedas = [1000, 500, 200, 100, 50]

# DETERMINAR MONEDAS PARA DEVOLVER
for moneda in monedas:
    cantidad = cambio // moneda
    if cantidad > 0:
        print("Monedas de", moneda, ":", cantidad)
        cambio = cambio % moneda  # Reducir el cambio restante
