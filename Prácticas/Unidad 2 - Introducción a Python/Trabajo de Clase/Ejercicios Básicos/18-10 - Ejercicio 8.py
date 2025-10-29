## Ejercicio 8

user_word = str(input("Introduce una palabra: "))

user_word = user_word.upper()
for letra in user_word:
    if letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
        print(letra, end="")
