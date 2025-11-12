lista = [4, 7, 8, 25, 3, 15]
num = 0

# Procedimiento 1
for i in range(len(lista)):
    if lista[i] > num:
        num = lista[i]
print(num)

# Procedimiento 2
for i in lista:
    if i > num:
        num = i
print(num)
