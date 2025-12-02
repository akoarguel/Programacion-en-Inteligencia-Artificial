
keys = [
    "ClaveSegura_2025*AI",
    "_MasterFP.Data84Ia!",
    "Permutacion$3000key#",
    "Python2025-DAM-99!",
    "simple.key.1a",
    "AAABBBCCC_Repite_Inicio!",
    "1234567_8901234_Key",
    "Z_Solo_Letras_Final_A",
    "Palindromo_omordnilaP",
    "!!!!!!!......??????",
    "aeiou_Vocales_Inicio",
    "AbCdEfGhIjKlMnOpQrSt",
    "UnaClaveMuyMuyLargaParaVerSiElBufferAguanta_2025"
]

msgs = [
    "1234567890",
    "Manel/Google_84",
    "Criptografia Simetrica",
    "Un mensaje con ñ y tildes: ópera.",
    "Ok",
    "      ",
    "user@example.com",
    "def main(): return 0",
    "¡Atención! ¿Estás ahí?",
    "123 + 456 = 579",
    "",
    "La cigüeña voló."
]

def validate(key):
    """
        Valida si una clave cumple con los requisitos mínimos.
        
        Reglas: Minimo 15 caracteres, debe tener mayúsculas, minúsculas,
        números y caracteres especiales.
    """
    if len(key) < 15:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digitos = False
    tiene_especiales = False
    
    for char in key:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_digitos = True
        elif not char.isalnum():
            tiene_especiales = True
    
    return tiene_mayuscula and tiene_minuscula and tiene_digitos and tiene_especiales


def encryption(msg, key):
    s1 = sust1(msg, key)
    print("\tsust1() -> ", s1)
    s2 = sust2(s1, key)
    print("\tsust2() -> ", s2)
    s3 = sust3(s2, key)
    print("\tsust3() -> ", s3)
    s4 = sust4(s3, key)
    print("\tsust4() -> ", s4)
    
    p1 = perm1(s4, key)
    print("\tperm1() -> ", p1)
    p2 = perm2(p1, key)
    print("\tperm2() -> ", p2)
    p3 = perm3(p2, key)
    print("\tperm3() -> ", p3)
    p4 = perm4(p3, key)
    print("\tperm4() -> ", p4)
    
    return p4

def sust1(msg, key):
    """
    Si la clave empieza por un número
        Resta 1 a cada código de cada chr
    Si no
        Sumo 1 a cada código de cada chr
    """
    
    new_msg = ""
    if key[0].isalnum():
        for letra in msg:
            new_msg += chr(ord(letra)-1)
    else:
        for letra in msg:
            new_msg += chr(ord(letra)+1)
    return new_msg

def des_sust1(code, key):
    """
    LOGICA INVERSA
    Si empieza por alfanumérico
        Sumo 1 cada chr
    Sino
        Resto 1 a cada chr
    """
    new_code = ""
    if key[0].isalnum():
        for letra in code:
            new_code += chr(ord(letra) + 1)
    else:
        for letra in code:
            new_code += chr(ord(letra) - 1)
    return new_code

def sust2(msg, key):
    """
    Si la key contiene más de 3 mayúsculas
        Se cambian las vocales de la siguiente forma:
        A = U, E = O, I = &, O = E, U = A
    Sino
        Sustituye mayúsculas y minúsculas
    """

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
            if letra in "Aa": new_msg += 'U'
            elif letra in "Ee": new_msg += 'O'
            elif letra in "Ii": new_msg += '&'
            elif letra in "Oo": new_msg += 'E'
            elif letra in "Uu": new_msg += 'A'
            else: new_msg += letra
        return new_msg
    else:
        return msg.swapcase()

def des_sust2(code, key):
    cont = 0
    tiene_mayus = False
    
    for letra in key:
        if letra.isupper():
            cont += 1
            if cont == 3:
                tiene_mayus = True
                break
    
    if tiene_mayus:
        new_code = ""
        for letra in code:
            if letra == 'U': 
                new_code += 'A'
            elif letra == 'O': 
                new_code += 'E'
            elif letra == '&': 
                new_code += 'I'
            elif letra == 'E': 
                new_code += 'O'
            elif letra == 'A': 
                new_code += 'U'
            else:
                new_code += letra
        return new_code
        
    else:
        return code.swapcase()

def sust3(msg, key):
    """
    Si la key contiene más de 1 simbolo
        Suma la [suma de las 2 primeras letras de la clave]
        a las 3 primeras
    Sino
        a las 3 últimas
    """

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
        rango = min(3, len(msg)) 
        for i in range(rango):
            new_msg += chr(ord(msg[i]) + suma_key)
        new_msg += msg[rango:]
    else:
        new_msg += msg[:-3]
        for letra in msg[-3:]:
            new_msg += chr(ord(letra) + suma_key)
    return new_msg

def sust4(msg, key):
    ## Si la longitud de la key es par
    ### Suma 1 a las letras en posiciones impares (1, 3, 5...)
    ## Sino
    ### Suma 1 a las letras en posiciones pares (0, 2, 4...)
    
    new_msg = ""
    es_key_par = len(key) % 2 == 0
    
    for i in range(len(msg)):
        if es_key_par:
            if i % 2 != 0: 
                new_msg += chr(ord(msg[i]) + 1)
            else:
                new_msg += msg[i]
        else:
            if i % 2 == 0:
                new_msg += chr(ord(msg[i]) + 1)
            else:
                new_msg += msg[i]
    return new_msg

def perm1(msg, key):
    ## Si la segunda mitad de la key es más larga de la primera
    ### Invierte la palabra
    ## Sino
    ### Intercambia las 2 primeras letras por las 2 última
    mitad = len(key) // 2
    primera_parte = key[:mitad]
    segunda_parte = key[mitad:]
    
    if len(primera_parte) > len(segunda_parte):
        return msg[::-1]
    else:
        if len(msg) < 4:
            return msg[::-1]
        return msg[-2:] + msg[2:-2] + msg[:2]
    
def perm2(msg, key):
    ## Si la key no repite ningun chr en las 10 primeras letras
    ### intercambia la primera letra por la tercera y la ultima
    #### por la antepenúltima
    ## Sino
    ### intercambia la primera letra por la segunda y la ultima
    #### por la penúltima
    
    repite_letra = False
    fragmento = key[:10]
    new_msg = ""
    
    for letra in fragmento:
        if fragmento.count(letra) > 1:
            repite_letra = True
            break
    
    # No se que hacer si es menor así que invertiré la palabra
    if len(msg) < 6:
        return msg[::-1]
    
    if repite_letra:
        ### Primera por tercera y penúltima por antepenúltima
        inicio = msg[2] + msg[1] + msg[0]
        centro = msg[3:-3]
        final = msg[-1] + msg[-2] + msg[-3]
        
        new_msg = inicio + centro + final
    else:
        inicio = msg[1] + msg[0]
        centro = msg[2:-2]
        final  = msg[-1] + msg[-2]
        
        new_msg = inicio + centro + final
        
    return new_msg

def perm3(msg, key):
    ## Si la key tiene una volcal en mayúsculas
    ### posiciones pares primero
    ## Sino 
    ### posiciones impares primero
    condicion = False
    pares = msg[::2]
    impares = msg[1::2]
    
    for letra in key:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            condicion = True
    
    if condicion:
        return pares + impares
    else: 
        return impares + pares
    
def perm4(msg, key):
    ## Si la clave tiene más de 8 caracteres únicos
    ### intercambiamos las las dos primera por las dos últimas
    ## Sino
    ### invierte la palabra
    new_msg = ""
    caracteres_unicos = []
    for letra in key:
        if letra not in caracteres_unicos:
            caracteres_unicos.append(letra)
    
    if len(caracteres_unicos) > 8:
        # basicamente nos vamos de 2 en 2 y si sobra uno lo metemos al final
        for i in range(0, len(msg) - 1, 2):
            new_msg += msg[i+1] + msg[i]
        
        if len(msg) % 2 != 0:
            new_msg += msg[-1]
        
        return new_msg
    else:
        return msg[::-1]
            
        
    
def start():
    print("\n\t--- PRUEBAS ---\n")

    for key in keys:
        print("\n---------------")
        print("\nCLAVE --> ", key)
        
        if not validate(key):
            print("Clave válida --> FALSE")
            continue
        else:
            print("Clave válida --> TRUE\n")
        
        for msg in msgs:
            print("\nMSG --> ", msg)
            
            final_res = encryption(msg, key)
            print("RESULTADO --> ", final_res)


start()
