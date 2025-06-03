# LISTA DE 10 APRENDICES ORDENADA ALFABÉTICAMENTE POR APELLIDO
aprendices = [
    "Aguilar", "Barrera", "Cardona", "Díaz", "Fernández",
    "Gómez", "López", "Morales", "Ramírez", "Zapata"
]

# MOSTRAR LISTA ORIGINAL
print("Lista original de aprendices:")
for apellido in aprendices:
    print(apellido)

# INGRESAR NUEVO APELLIDO
nuevo = input("\nIngrese el apellido del nuevo aprendiz: ")

# AGREGAR A LA LISTA Y ORDENAR
aprendices.append(nuevo)
aprendices.sort()

# MOSTRAR LISTA ACTUALIZADA
print("\nLista actualizada de aprendices:")
for apellido in aprendices:
    print(apellido)
