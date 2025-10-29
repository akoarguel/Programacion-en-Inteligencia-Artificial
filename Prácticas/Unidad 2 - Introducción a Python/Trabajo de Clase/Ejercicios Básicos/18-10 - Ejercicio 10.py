## Ejercicio 10

num = int(input("Ingrese un número: "))
resul = 0.0

for i in range(num):
    resul += 1/(i+1)

print(round(resul, 2))
