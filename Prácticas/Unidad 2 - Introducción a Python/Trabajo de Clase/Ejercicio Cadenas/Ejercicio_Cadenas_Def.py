
keys = [
        "ClaveSegura_2025*AI",       
        "_MasterFP.Data84Ia!",       
        "Permutacion$3000key#",      
        "Python2025-DAM-99!",        
        "simple.key.1a"              
    ]
    
msgs = [
        "1234567890",
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
    print("sust1(): ", msg)
    msg = enc2(msg, key)
    print("sust2(): ", msg)
    msg = enc3(msg, key)
    print("sust3(): ", msg)
    code = enc4(msg, key)
    return code

def sust1(msg, key):
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

def sust2(msg, key):
    ## Si la key contiene más de 3 mayusculas
    ### Se cambian las vocales:
    ### A = U, E = O, I = &, O = E, U = A
    ## Sino
    #### sustituye mayusculas y minusculas

    cont = 0
    tiene_mayus = False
    new_msg = ""

    for letra in key:
        if letra.isupper():
            cont += 1
            if cont == 3:
                tiene_mayus = True
                break

    if tiene_mayus:
        for letra in msg:
            if letra == 'A' or letra == 'a':
                new_msg += 'U'
            elif letra == 'E' or letra == 'e':
                new_msg += 'O'
            elif letra == 'I' or letra == 'i':
                new_msg += '&'
            elif letra == 'O' or letra == 'o':
                new_msg += 'E'
            elif letra == 'U' or letra == 'u':
                new_msg += 'A'
            else:
                new_msg += letra
        return new_msg
    else:
        return msg.swapcase()

def sust3(msg, key):
    ## Si la key contiene más de 1 simbolo
    ### suma la (suma de las 2 primeras letras de la clave)
    #### a las 3 primeras
    ## Sino
    ### a las 3 últimas

    cont = 0
    tiene_simb = False
    new_msg = ""
    suma_key = ord(key[0]) + ord(key[1])

    for letra in key:
        if not letra.isalnum():
            cont += 1
            if cont >= 2:
                tiene_simb = True
                break
            
    if tiene_simb:
        for i in range(2):
            new_msg += chr(ord(key[i]+suma_key))
    # TODO terminar el cambiar las 3 primeras letras y las 3 últimas
    

def sust4(msg, key):
    ## Si ...
    ### Suma 1 a las letras en posiciones impares
    ## Sino
    ### Suma 1 a las letras en posiciones pares
    ...
    
def start():
    print("\n\t--- PRUEBAS ---\n")

    for key in keys:
        print("\n---------------")
        print("\nCLAVE --> ", key)
        
        # Validar la clave
        if not validate(key):
            print("\nClave válida --> ❌")
            continue
        else:
            print("Clave válida --> ✅\n")
        
        for msg in msgs:
            print("\nMSG --> ", msg, end="\n")
            s1 = sust1(msg, key)
            print("\tsust1 -> ", s1)
            s2 = sust2(msg, key)
            print("\tsust2 -> ", sust2(s1, key))
            
        
start()
