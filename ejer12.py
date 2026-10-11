def contar_palabra(texto, palabra):
    return texto.split().count(palabra)

texto = input("Ingrese texto: ")
palabra = input("Ingrese palabra: ")
print(contar_palabra(texto, palabra))