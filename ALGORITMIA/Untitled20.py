# INGRESO DE DATOS
while True:
    try:
        capital = float(input("Ingrese el capital del préstamo: "))
        interes_anual = float(input("Ingrese el interés anual (en %): "))
        años = int(input("Ingrese el número de años del préstamo: "))
        break
    except:
        print("Entrada inválida. Intente nuevamente.")

# CÁLCULOS
interes_mensual = interes_anual / 100 / 12
numero_pagos = años * 12

# FORMULA DE CUOTA MENSUAL
if interes_mensual == 0:
    cuota_mensual = capital / numero_pagos
else:
    cuota_mensual = (capital * interes_mensual * (1 + interes_mensual) ** numero_pagos) / \
                    ((1 + interes_mensual) ** numero_pagos - 1)

# TOTAL A PAGAR
total_pagar = cuota_mensual * numero_pagos

# RESULTADOS
print("\n--- RESULTADOS ---")
print("Cuota mensual: $", round(cuota_mensual, 2))
print("Total a pagar al final del préstamo: $", round(total_pagar, 2))
