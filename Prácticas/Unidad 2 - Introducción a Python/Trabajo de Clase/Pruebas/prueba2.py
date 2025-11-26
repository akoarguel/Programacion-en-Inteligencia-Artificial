key = "Hola_12345Mundo0o_"
msg = "manel/google_84"
code = "«¬¥¬O§¯¯§¬¥XT"

"""
enc1():  l`mdk.fnnfkd^73
enc2():  ­¡®¥¬o§¯¯§¬¥xt
enc3():  ­¡®¥¬O§¯¯§¬¥XT

Texto original:  manel/google_84
Texto encriptado:  «¬¥¬O§¯¯§¬¥XT

"""


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
    return new_code

def start():
    code1 = des1(code, key)
    print(code1)
    code2 = des2(code1, key)
    print(code2)
    code3 = des3(code2, key)
    print(code3)
    code_final = des4(code3, key)
    print(code_final)
    

start()
