def perm3(msg, key):
    ## Si la key tiene una volcal en mayúsculas
    ### posiciones impares primero
    ## Sino 
    ### posiciones pares primero
    condicion = False
    pares = msg[::2]
    impares = msg[1::2]
    
    
    for letra in key:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            condicion = True
    
    if condicion:
        return impares + pares
    else: 
        return pares + impares

def des_perm3(code, key):
    condicion = False
    for letra in key:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            condicion = True

    cant_impares = len(code) // 2
    cant_pares = len(code) - cant_impares

    texto_pares = ""
    texto_impares = ""

    if condicion:
        texto_impares = code[:cant_impares]
        texto_pares = code[cant_impares:]
    else:
        texto_pares = code[:cant_pares]
        texto_impares = code[cant_pares:]

    new_code = ""
    
    for i in range(cant_impares):
        new_code = new_code + texto_pares[i]
        new_code = new_code + texto_impares[i] 

    if len(texto_pares) > len(texto_impares):
        new_code = new_code + texto_pares[-1]

    return new_code
    
        
p = "hola4"
print("msg: ", p)
p1 = perm3(p, "_MasterFP.Data84Ia!")
print("encriptado: ", p1)
d1 = des_perm3(p1, "_MasterFP.Data84Ia!")
print("desencriptado: ", d1);
