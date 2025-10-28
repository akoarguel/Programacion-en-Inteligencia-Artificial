##El impuesto en País se evalúa u lizando la siguiente regla: 
## si el ingreso del ciudadano no es superior a 85.528 €, el impuesto es igual al 18% del ingreso 
##menos 556,20 € (la llamada exención fiscal). 
## si el ingreso es superior a esta can dad, el impuesto es igual a 14.839,20 €, más el 32% del 
##excedente sobre 85.528 €. 
##Tu tarea es escribir una calculadora de impuestos. 
## Debe aceptar un valor de punto flotante: el ingreso. 
## A con nuación, debe imprimir el impuesto calculado, redondeado a € totales. U liza la función 
##round() para redondear el valor. 
##Si el impuesto calculado es menor que cero, solo significa que no hay impuesto .

def calcular_impuesto(ingreso):
    if ingreso < 85528:
        impuesto_calculado = (ingreso*0.18)-556.20
        if impuesto_calculado < 0:
            return 0.0
        return impuesto_calculado
    else:
        impuesto_calculado = ((ingreso-85528)*0.32)+ 14839.20
        return impuesto_calculado

ingreso = float(input("Introduce el ingreso: "))
impuesto = round(calcular_impuesto(ingreso),0)
print(f"El impuesto es: {impuesto} €")
