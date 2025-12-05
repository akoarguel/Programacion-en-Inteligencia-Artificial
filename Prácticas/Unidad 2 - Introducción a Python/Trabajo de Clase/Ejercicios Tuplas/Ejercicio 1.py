### Ejercicio 1

agenda = {}

def leer_diccionario(nombre, edad):
    agenda.update({nombre: edad})

def oldest(agenda):
    edad_mayor = max(agenda.values())
    
    for nombre, edad in sorted(agenda.items()):
        if edad == edad_mayor:
            return nombre


def youngest(agenda):
    edad_menor = min(agenda.values())
    
    for nombre, edad in sorted(agenda.items()):
        if edad == edad_menor:
            return nombre

def start():
    nombre = input("Introduce el NOMBRE: ")
    while nombre != "0":        
        edad = input("Introduce la EDAD: ")
        leer_diccionario(nombre, int(edad))
        nombre = input("Introduce el NOMBRE: ")
    print("Mayor -> ", oldest(agenda), agenda[oldest(agenda)], "años")
    print("Menor ->", youngest(agenda), agenda[youngest(agenda)], "años")


start()
