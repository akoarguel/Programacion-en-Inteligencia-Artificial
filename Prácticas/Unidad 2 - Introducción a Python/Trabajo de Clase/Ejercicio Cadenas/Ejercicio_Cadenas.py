### Ejercicio Cadenas

def validate(key):
    if len(key) < 15:
        return False
    elif key.islower() and key.isupper():
        return False
    elif key.isalnum():
        return False
    else:
        return True

def encrytion(msg, key):
    

def decoded(code, key):


def per1(msg, key):
    ## Si empieza por numero
    ### resto 1 a cada chr
    ## Sino
    ### sumo 1 a cada chr
    
    new_msg = ""
    if key[0].isalnum():
        for letra in msg:
            new_msg += chr(ord(letra)-1)
    else:
        for letra in msg:
            new_msg += chr(ord(letra)+1)
    return new_msg

def per2(msg, key):
    ## Suma del cod del chr de los impares
    ### -
    ## Suma del cod del chr de los pares
    # El resultado se lo sumo al cod de todos los caracteres
    
    list_msg = list(msg)
    pares = 0
    impares = 0
    for i in range(0, len(msg), 2):
        pares += ord(list_msg[i])
    for i in range(1, len(msg), 2):
        impares += ord(list_msg[i])
        
    new_msg = ""
    x = pares-impares
    for letra in msg:
        new_msg += chr(ord(letra)+x)
    return new_msg

def per3(msg, key):
    ## Si la suma de los chr son pares
    ### divido entre 2 y le resto eso a cada chr
    ## Sino
    ### lo sumo
    
    suma = 0
    for i in range(0, len(msg)):
        suma += ord(list_msg[i])
    new_msg = ""
    suma = suma/2

    if suma % 2 == 0:
        for letra in msg:
            new_msg += chr(ord(letra)-suma)
    else:
        for letra in msg:
            new_msg += chr(ord(letra)+suma)
    
        
    
    
