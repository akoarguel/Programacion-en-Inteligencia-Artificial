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
    new_code = ""
    num_impares = (len(code) // 2) + (len(code) % 2)
    print("impares: ", num_impares)
    num_pares = len(code) // 2
    print("pares: ", num_pares)
    condicion = False
    
    for letra in key:
        if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            condicion = True

    if condicion:
        impares = code[:num_pares]
        print(impares)
    
        
p = "hola4"
print("msg: ", p)
p1 = perm3(p, "_MasterFP.Data84Ia!")
print("encriptado: ", p1)
d1 = des_perm3(p1, "_MasterFP.Data84Ia!")
print("desencriptado: ", d1);
