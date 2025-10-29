## Ejercicio 11

bloques = int(input("Número de bloques: "))
capas = 0

for i in range(bloques):
    if bloques < capas:
        break
    capas += 1
    bloques -= (i+1)

print(f"La altura de la pirámide es: {capas}")
