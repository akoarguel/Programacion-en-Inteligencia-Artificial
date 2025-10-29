## Ejercicio 12

from random import randint
from random import *

intentos = 0
objetivo = randint(0, 100)

while(intentos != 3):
    num = int(input("Introduce el número: "))
    intentos += 1
    if intentos == 3:
        print("Más suerte la próxima vez...")
        break
    else:   
        if num < objetivo:
            print("Más alto, sube sin miedo")
        elif num > objetivo:
            print("No tan alto, es menor")
        else:
            print("Buen Trabajo")
            break
    
