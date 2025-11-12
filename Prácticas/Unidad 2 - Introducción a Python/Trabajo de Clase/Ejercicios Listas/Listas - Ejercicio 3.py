lista = [4, 7, 8, 25, 3, 15, 5]
nueva_lista = []
"""
n = len(lista)

def ordenar(lista):
    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)
ordenar(lista)
print(lista)


"""

for pos in range(len(lista)-1):
    b = lista[pos]
    min = pos
    for i in range(pos+1, len(lista)):
        if lista[i] <= b:
            b = lista[i]
            min = i

    for j in range(min, pos, -1):
        lista[j] = lista[j-1]
    lista[pos]=b
    print(lista)
