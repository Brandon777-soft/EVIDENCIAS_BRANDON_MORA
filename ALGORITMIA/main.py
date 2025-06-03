#INGRESAR NUMERO
while True:
    try:
        num = int(input("Ingrese Numero:"))
        break
    except:
        print("Numero Equivocado")
#VERIFICAR SI EL NUMERO ES PAR O IMPAR

if num % 2 == 0:
    print("Este Numero Es Par")
else:
    print("Este Numero Es Impar")