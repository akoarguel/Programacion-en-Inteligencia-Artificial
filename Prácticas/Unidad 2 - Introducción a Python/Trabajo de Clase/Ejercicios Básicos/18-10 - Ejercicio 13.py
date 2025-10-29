## Ejercicio 13
c0 = int(input("Introduce un número: "))

if c0 <= 0:
    print("Error: Intruduce un número mayor que 0. ")

pasos = 0

while(c0!=1):
    if (c0 % 2 == 0):
        c0 = c0/2
        pasos += 1
        print(f"{int(c0)} - " , end="")
    else:
        c0 = 3*c0+1
        pasos += 1
        print(f"{int(c0)} - " , end="")

print(f"Pasos: {pasos}")
    
