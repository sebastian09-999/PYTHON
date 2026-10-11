def es_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def es_rectangulo(a, b, c):
    lados = sorted([a, b, c])
    return lados[0] ** 2 + lados[1] ** 2 == lados[2] ** 2

a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

if es_triangulo(a, b, c):
    print("Pueden formar un triángulo")
    if es_rectangulo(a, b, c):
        print("Es un triángulo rectángulo")
    else:
        print("No es un triángulo rectángulo")
else:
    print("No pueden formar un triángulo")