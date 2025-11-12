# Ejercicio 5

lista = [5, 10, 9, 3, 1, 10, 9]

def eliminiar_repetidos(lista):
    nueva_lista = []
    for i in lista:
        if i not in nueva_lista:
            nueva_lista.append(i)
    return nueva_lista

print(lista)
print(eliminiar_repetidos(lista))
