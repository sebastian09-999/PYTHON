def separar_pares_impares(lista):
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    pares.sort()
    impares.sort()
    return pares, impares

numeros = [5, 2, 8, 1, 4, 7]
print(separar_pares_impares(numeros))