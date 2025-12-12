### Ejercicio 5

registro = {
        'Lunes': (5, 11),
        'Martes': (7, 14),
        'Miércoles': (6, 13),
        'Jueves': (9, 16),
        'Viernes': (1, 11),
        'Sábado': (4, 12),
        'Domingo': (5, 15)
    }

def comprobar_datos(registro):
    for key in sorted(registro.keys()):
        if (registro[key][0] > registro[key][1]):
            return False
    return True

def temp_media(registro):
    temp_media = []
    for key in sorted(registro.keys()):
        temp_media.append(sum(registro[key])/2)
    return temp_media

def alertas(registro):
    alertas = []
    dif = 0
    for key in sorted(registro.keys()):
        dif = registro[key][1] - registro[key][0]
        if dif > 15:
            alertas.append("ALERTA")
        else:
            alertas.append("...")
    return alertas

if comprobar_datos(registro):
    print("Todo correcto. ")
else:
    print("ERROR. Los datos no son correctos. ")


print("Temperaturas médias: ")
print(temp_media(registro))
print("Amplitud térmica: ")
print(alertas(registro))
