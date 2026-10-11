palabras = []
cantidad = int(input("¿Cuántas palabras desea ingresar? "))
for i in range(cantidad):
    palabras.append(input("Ingrese palabra: "))
buscar = input("Ingrese palabra a buscar: ")
print(palabras.count(buscar))