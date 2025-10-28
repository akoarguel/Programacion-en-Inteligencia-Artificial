## si el número del año no es divisible entre cuatro, es un año común. 
## de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto. 
## de lo contrario, si el número del año no es divisible entre 400, es un año común. 
## de lo contrario, es un año bisiesto. 

ano = int(input("Introduce el año: "))

if ano < 1582:
    print("Fuera del periodo del calendario gregoriano")
else:
    if ano % 4 != 0:
        print("Año común")
    elif ano % 100 != 0:
        print("Año bisiesto")
    elif ano % 400 != 0:
        print("Año común")
    else:
        print("Año bisiesto")
