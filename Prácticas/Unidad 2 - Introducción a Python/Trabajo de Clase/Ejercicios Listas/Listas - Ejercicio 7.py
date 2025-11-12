# Ejercicio 7

import random

lista = []

for dia in range(1, 32):
    lista_dia = []
    for hora in range(24):
        dato = round(random.uniform(0, 50), 2)
        lista_dia.append(dato)
    lista.append(lista_dia)
        

for f in lista:
    for e in fila:
        print(e, end=" ")
    print()
