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
    msg = enc1(msg, key)
    print("enc1(): ", msg)
    msg = enc2(msg, key)
    print("enc2(): ", msg)
    msg = enc3(msg, key)
    print("enc3(): ", msg)
    code = enc4(msg, key)
    return code

##def decoded(code, key):
##    


def enc1(msg, key):
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

def enc2(msg, key):
    ## Suma del cod del chr de los impares DE LA CLAVE
    ### -
    ## Suma del cod del chr de los pares DE LA CLAVE
    ### El resultado se lo sumo al cod de todos los caracteres
    
    list_key = list(key)
    pares = 0
    impares = 0
    for i in range(0, len(key), 2):
        pares += ord(list_key[i])
    for i in range(1, len(key), 2):
        impares += ord(list_key[i])

    new_msg = ""
    x = pares-impares
    for letra in msg:
        new_msg += chr(ord(letra)+x)
    return new_msg

def enc3(msg, key):
    ## Si la key contiene más de 3 números
    ### intercambiamos las mayuculas por mínusculas
    ## Sino
    ### invertimos la palabra
    cont = 0
    tiene_num = False
    new_msg = ""
    
    for letra in key:
        if letra.isdigit():
            cont += 1
            if cont == 3:
                tiene_num = True
                break
            else:
                continue
    
    if tiene_num:
        new_msg = msg.swapcase()
        return new_msg
    else:
        new_msg = []
        final_msg = ""
        for i in msg:
            new_msg.insert(0,i)
        for i in new_msg:
            final_msg += i
    return final_msg
    
def enc4(msg, key):
    ## Si contiene 2 simbolos o más
    ### resta 2 a las 3 primeras letras
    ## Sino
    ### resta 1 a todos
    cont = 0
    tiene_dig = False
    new_msg = ""
    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont > 1:
                tiene_dig = True
                break
            
    if tiene_dig:
        for i in msg[:3]:
            new_msg += chr(ord(i)-2)
        for i in msg[3:]:
            new_msg += i
        return new_msg
            
    else:
        for i in msg:
            new_msg += chr(ord(i)+1)
        return new_msg

def des1(code, key):
    ## Funciona
    cont = 0
    tiene_dig = False
    new_code = ""
    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont > 1:
                tiene_dig = True
                break
            
    if tiene_dig:
        for i in code[:3]:
            new_code += chr(ord(i)+2)
        for i in code[3:]:
            new_code += i
        return new_code
    else:
        for i in code:
            new_code += chr(ord(i)+1)
        return new_code

def des2(code, key):
    # Funciona
    cont = 0
    tiene_num = False
    new_code = ""
    
    for letra in key:
        if letra.isdigit():
            cont += 1
            if cont == 3:
                tiene_num = True
                break
            else:
                continue
    if tiene_num:
        new_code = code.swapcase()
        return new_code
    else:
        new_code = []
        final_code = ""
        for i in code:
            new_code.insert(0,i)
        for i in new_code:
            final_code += i
        return final_code

def des3(code, key):
    # No se si funciona
    list_key = list(key)
    pares = 0
    impares = 0
    for i in range(0, len(key), 2):
        pares += ord(list_key[i])
    for i in range(1, len(key), 2):
        impares += ord(list_key[i])

    new_code = ""
    x = pares-impares
    for letra in code:
        new_code += chr(ord(letra)-x)
    return new_code

def des4(code, key):
    new_code = ""
    if key[0].isalnum():
        for letra in code:
            new_code += chr(ord(letra)+1)
    else:
        for letra in code:
            new_code += chr(ord(letra)-1)
    
def start():
    key = input("Introduce una key: ")
    while (validate(key) == False):
        print("Error. No es una clave válida. ") 
        key = input("Introduce una key: ")

    msg = input("introduce el texto a encriptar: ")
    print("Encriptando...")
    code = encrytion(msg, key)
    print("Texto original: ", msg)
    print("Texto encriptado: ", code)

start()




