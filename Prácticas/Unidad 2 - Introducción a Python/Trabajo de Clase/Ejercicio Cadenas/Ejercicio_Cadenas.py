### Ejercicio Cadenas

keys = [
        "ClaveSegura_2025*AI",       
        "_MasterFP.Data84Ia!",       
        "Permutacion$3000key#",      
        "Python2025-DAM-99!",        
        "simple.key.1a"              
    ]
    
msgs = [
        "Manel/Google_84",
        "Criptografia Simetrica",
        "Un mensaje con ñ y tildes: ópera."
    ]

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
    ## Si la key es mayor que 15
    ### se intercambian las mitades
    ## Si no
    ### Junta los impares y pares
    
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
    ## Si la key contiene más de 1 simbolo
    ### Se reta uno a las 3 primeras y se invierte
    ## Sino
    ### Se resta uno a las 3 ultimas y se invierte
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

def dec1(code, key):
    new_msg = ""
    if key[0].isalnum():
        for letra in code:
            new_msg += chr(ord(letra) + 1)
    else:
        for letra in code:
            new_msg += chr(ord(letra) - 1)
    return new_msg

def dec2(code, key):
    ...

def dec3(code, key):
    cont = 0
    tiene_num = False
    
    for letra in key:
        if letra.isdigit():
            cont += 1
            if cont == 3:
                tiene_num = True
                break
    
    if tiene_num:
        plano = code.swapcase()
        return plano
    else:
        return code[::-1]
    
def dec4(code, key):
    cont = 0
    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont >= 2:
                break
                
    n = len(code)

    temp_msg = code[::-1]
    
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




