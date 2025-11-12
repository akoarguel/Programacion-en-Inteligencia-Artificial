# Ejercicio 6

lista = []
lista_pares = []

for i in range(16):
    lista.append((i+1)**2)

for i in range(16):
    if (i+1) % 2 == 0:
        lista_pares.append((i+1)**2)

print(lista)
print(lista_pares)
