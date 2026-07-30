#Ejercicio3
edad = int(input("Ingrese la edad del cliente: "))


if edad < 5:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 10000

if precio == 0:
    print("El cliente es menor de 5 años: ¡Entrada GRATIS!")
else:
    print(f"El precio de la entrada es: ${precio:,} pesos.")