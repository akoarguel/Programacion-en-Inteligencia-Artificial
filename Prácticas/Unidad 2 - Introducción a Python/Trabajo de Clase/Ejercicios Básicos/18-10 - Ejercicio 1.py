## Diseña un programa para que, a partir de un número x ingresado, calcule el valor de
## la fnción y. La expresión de la función es:

# Calculamos la función
def calcular_funcion(x):
    resul = 1/x
    for i in range(4):
        resul /= 1/x
    return resul

# Solicitar un número
x = int(input("Introduce un número"))

print(calcular_funcion(x))

