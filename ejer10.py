dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
minimas = []
maximas = []

for dia in dias:
    minima = float(input("Temperatura mínima del " + dia + ": "))
    maxima = float(input("Temperatura máxima del " + dia + ": "))
    minimas.append(minima)
    maximas.append(maxima)

for i in range(7):
    media = (minimas[i] + maximas[i]) / 2
    print("Temperatura media de", dias[i] + ":", media)

menor = min(minimas)
print("Días con menos temperatura:")
for i in range(7):
    if minimas[i] == menor:
        print(dias[i])

temp = float(input("Ingrese una temperatura máxima: "))
encontrado = False
for i in range(7):
    if maximas[i] == temp:
        print(dias[i])
        encontrado = True

if not encontrado:
    print("No existe ningún día con esa temperatura máxima")