import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

print("Lista original:", lista)
lista.sort()
print("Lista ordenada:", lista)