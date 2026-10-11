for i in range(5):
    edad = int(input("Ingrese la edad: "))
    if edad >= 80:
        print("Fase 1")
    elif edad >= 70:
        print("Fase 2")
    elif edad >= 60:
        print("Fase 3")
    elif edad >= 30:
        print("Fase 4")
    elif edad >= 18:
        print("Fase 5")
    else:
        print("En espera de Autorización")