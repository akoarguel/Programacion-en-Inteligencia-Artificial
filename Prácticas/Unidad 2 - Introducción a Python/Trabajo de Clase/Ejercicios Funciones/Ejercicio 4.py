# Ejercicio 4

def es_primo(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return True

for i in range(1, 20):
    if es_primo(i):
        print(i)
