# 1. Solicitamos la edad al cliente y la convertimos a un número entero
edad = int(input("Ingrese la edad del cliente: "))

# 2. Determinamos la tarifa según la edad
if edad < 5:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 10000

# 3. Mostramos el resultado final
if precio == 0:
    print("El cliente es menor de 5 años: ¡Entrada GRATIS!")
else:
    print(f"El precio de la entrada es: ${precio:,} pesos.")