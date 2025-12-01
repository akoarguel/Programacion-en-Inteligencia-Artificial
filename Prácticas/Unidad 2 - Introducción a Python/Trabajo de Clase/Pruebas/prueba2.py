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
    "La longitud es 15!",
    "@test-001.ok",
    "aBc9",
    "Un mensaje con ñ y tildes: ópera."
]

def validate(key):
    if len(key) < 15:
        return False
    
    has_lower = any(c.islower() for c in key)
    has_upper = any(c.isupper() for c in key)
    has_digit = any(c.isdigit() for c in key)
    has_symbol = any(not c.isalnum() for c in key)
    
    if has_lower and has_upper and has_digit and has_symbol:
        return True
    else: 
        return False

def encrytion(msg, key):
    msg = enc1(msg, key)
    print("enc1(): ", msg)
    msg = enc2(msg, key)
    print("enc2(): ", msg)
    msg = enc3(msg, key)
    print("enc3(): ", msg)
    code = enc4(msg, key)
    return code

def decoded(code, key):
    code1 = dec4(code, key)
    print("dec4(): ", code1)
    
    code2 = dec3(code1, key)
    print("dec3(): ", code2)
    
    code3 = dec2(code2, key)
    print("dec2(): ", code3)
    
    code4 = dec1(code3, key)
    print("dec1(): ", code4)
    
    return code4

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
    n = len(code)
    if n == 0:
        return ""

    if len(key) > 15:
        mitad = n // 2
        if n % 2 != 0:
            plano = code[mitad:] + code[:mitad]
        else:
            plano = code[mitad:] + code[:mitad]
        if n % 2 != 0:
            mitad_larga = (n // 2) + 1
            mitad_corta = n // 2 
            
            plano = code[mitad_larga:] + code[:mitad_larga]
        else:
            plano = code[mitad:] + code[:mitad]
            
    else:
        num_impares = n // 2
        
        impares_cifrado = code[:num_impares]
        pares_cifrado = code[num_impares:]
        
        plano_lista = [""] * n
        plano_lista[0::2] = list(pares_cifrado)
        plano_lista[1::2] = list(impares_cifrado)
        
        plano = "".join(plano_lista)
        
    return plano

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

    for key in keys:
        print("==========================================================")
        
        if not validate(key):
            print(f"🔑 Clave: {key} -> ❌ Clave NO VÁLIDA (No cumple requisitos de robustez).")
            continue

        print(f"🔑 Clave: {key} -> ✅ Clave VÁLIDA.")
        
        for msg in msgs:
            print("---")
            print(f"   Original: {msg}")
            
            # ENCRIPTACIÓN
            encrypted_code = encrytion(msg, key)
            print("   Enc. Final: ", encrypted_code)
            
            # DESENCRIPTACIÓN (usando la función corregida)
            decrypted_msg = decoded(encrypted_code, key)
            print("   Desc. Final: ", decrypted_msg)
            
            simetria = "✅ OK" if decrypted_msg == msg else "❌ ERROR"
            print(f"   SIMETRÍA: {simetria}")

    print("==========================================================")
    print("\n✅ Pruebas finalizadas.")

start() 