## Ejercicio 9

palabra_sin_vocales = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable palabra_usuario
palabra_usuario = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
palabra_usuario = palabra_usuario.upper()

for letter in palabra_usuario:
    # Completa el cuerpo del bucle
    
    # Comprobar si la letra es una vocal
    if letter == 'A':
        continue  # Devorar 'A'
    elif letter == 'E':
        continue  # Devorar 'E'
    elif letter == 'I':
        continue  # Devorar 'I'
    elif letter == 'O':
        continue  # Devorar 'O'
    elif letter == 'U':
        continue  # Devorar 'U'
    else:
        # Si no es una vocal, asignarla a la nueva cadena
        palabra_sin_vocales += letter

# Imprimir la palabra asignada a palabra_sin_vocales
print(palabra_sin_vocales)
