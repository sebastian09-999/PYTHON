#Ejercicio 2

nombre = input("Ingrese su nombre: ").strip()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").strip().upper()

# Convertimos el nombre a minúsculas para comparar sin importar cómo lo escriba el usuario
nombre_min = nombre.lower()


# Grupo A: Mujeres con nombre anterior a la 'm' O hombres con nombre posterior a la 'n'
if (sexo == "M" and nombre_min < "m") or (sexo == "H" and nombre_min > "n"):
    grupo = "A"
else:
    grupo = "B"


print(f"\nHola, {nombre.capitalize()}. Te corresponde el Grupo {grupo}.")