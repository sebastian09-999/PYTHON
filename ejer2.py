#Ejercicio 2
# 1. Solicitamos el nombre y sexo al usuario
nombre = input("Ingrese su nombre: ").strip()
sexo = input("Ingrese su sexo (M para mujer, H para hombre): ").strip().upper()

# Convertimos el nombre a minúsculas para comparar sin importar cómo lo escriba el usuario
nombre_min = nombre.lower()

# 2. Determinamos el grupo según las condiciones
# Grupo A: Mujeres con nombre anterior a la 'm' O hombres con nombre posterior a la 'n'
if (sexo == "M" and nombre_min < "m") or (sexo == "H" and nombre_min > "n"):
    grupo = "A"
else:
    grupo = "B"

# 3. Mostramos el resultado
print(f"\nHola, {nombre.capitalize()}. Te corresponde el Grupo {grupo}.")