key = "5hola4_"
msg = "contraseña"

##def per2(msg, key):
##    new_msg = ""
##    if key[0].isalnum():
##        for letra in msg:
##            new_msg += chr(ord(letra)-1)
##    else:
##        for letra in msg:
##            new_msg += chr(ord(letra)+1)
##    return new_msg
##
##def per1(msg, key):
##    ## Suma del cod del chr de los impares
##    ### -
##    ## Suma del cod del chr de los pares
##    # El resultado se lo sumo al cod de todos los caracteres
##    
##    list_msg = list(msg)
##    pares = 0
##    impares = 0
##    for i in range(0, len(msg), 2):
##        pares += ord(list_msg[i])
##    for i in range(1, len(msg), 2):
##        impares += ord(list_msg[i])
##        
##    new_msg = ""
##    x = pares-impares
##    for letra in msg:
##        new_msg += chr(ord(letra)+x)
##    return new_msg


def per3(msg, key):
    ## Si la suma de los chr son pares
    ### divido entre 2 y le resto eso a cada chr
    ## Sino
    ### lo resto sin dividir

    list_msg = list(msg)
    suma = 0
    for i in range(0, len(msg)):
        suma += ord(list_msg[i])

    
    new_msg = ""
    

    if suma % 2 == 0:
        suma = suma/2
        for letra in msg:
            new_msg += chr(ord(letra)-suma)
    else:
        for letra in msg:
            new_msg += chr(ord(letra)-suma)
    return new_msg

print(per3(msg, key))
