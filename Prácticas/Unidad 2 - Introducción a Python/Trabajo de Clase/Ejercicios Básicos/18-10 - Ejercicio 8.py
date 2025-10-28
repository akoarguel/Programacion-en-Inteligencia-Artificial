## Ejercicio 8

user_word = str(input("Introduce una palabra: "))

def devorar_vocales(user_word):
    user_word = user_word.upper()
    palabra_def = ""

    for letra in user_word:
        if letra == 'A':
            continue
        elif letra == 'E':
            continue
        elif letra == 'I':
            continue
        elif letra == 'O':
            continue
        elif letra == 'U':
            continue
        else:
            palabra_def += letra
    return palabra_def

print(devorar_vocales(user_word))
