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
    n = len(msg)
    
    if len(key) > 15:
        mitad = n // 2
        msg_permutado = msg[mitad:] + msg[:mitad]
    else:
        chr_impares = msg[1::2]
        chr_pares = msg[0::2]
        msg_permutado = chr_impares + chr_pares
        
    return msg_permutado

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
    cont = 0
    
    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont >= 2:
                break
    
    temp_msg = ""
    n = len(msg)

    if cont >= 2:
        for i in range(n):
            letra = msg[i]
            
            if i < 3:
                temp_msg += chr(ord(letra) - 1)
            else:
                temp_msg += letra
            
    else:
        punto_inicio = max(0, n - 3)
        
        for i in range(n):
            letra = msg[i]

            if i >= punto_inicio:
                temp_msg += chr(ord(letra) + 1)
            else:
                temp_msg += letra
    
    new_msg = temp_msg[::-1]
    return new_msg

def dec1(encrypted_msg, key):
    new_msg = ""
    if key[0].isalnum():
        for letra in encrypted_msg:
            new_msg += chr(ord(letra) + 1)
    else:
        for letra in encrypted_msg:
            new_msg += chr(ord(letra) - 1)
    return new_msg

def dec2(encrypted_msg, key):
    n = len(encrypted_msg)
    if n == 0:
        return ""
        
    if len(key) > 15:
        mitad = n // 2
        plano = encrypted_msg[mitad:] + encrypted_msg[:mitad]
        
    else:
        num_impares = n // 2
        
        impares_cifrado = encrypted_msg[:num_impares]
        pares_cifrado = encrypted_msg[num_impares:]
        
        plano_lista = [""] * n
        
        plano_lista[0::2] = list(pares_cifrado)
        plano_lista[1::2] = list(impares_cifrado)
        
        plano = "".join(plano_lista)
        
    return plano

def dec3(encrypted_msg, key):
    cont = 0
    tiene_num = False
    
    for letra in key:
        if letra.isdigit():
            cont += 1
            if cont == 3:
                tiene_num = True
                break
    
    if tiene_num:
        plano = encrypted_msg.swapcase()
        return plano
    else:
        return encrypted_msg[::-1]
    
def dec4(encrypted_msg, key):
    cont = 0
    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont >= 2:
                break
                
    n = len(encrypted_msg)

    temp_msg = encrypted_msg[::-1]
    
    plano_msg = ""
    
    if cont >= 2:
        for i in range(n):
            letra = temp_msg[i]
        
            if i < 3:
                plano_msg += chr(ord(letra) + 1)
            else:
                plano_msg += letra
                
        return plano_msg
            
    else:
        punto_inicio = max(0, n - 3)
        for i in range(n):
            letra = temp_msg[i]
            
            if i >= punto_inicio:
                plano_msg += chr(ord(letra) - 1)
            else:
                plano_msg += letra
                
        return plano_msg
    
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




