### Ejercicio 7

inventario = {
    "Monitor AOC 27'": [(219.95, 10, 2), (209.95, 1, 2), (220.90, 15, 1)],
    "Teclado EPOMAKER": [(85.95, 15, 1), (97.99, 17, 1), (90.00, 0, 1)],
    "Ratón ATACKSHARK": [(50.00, 19, 2), (60.00, 5, 2), (55.95, 1, 2)]
    }

def valor_total(inventario):
    vt = {}
    for key in inventario.keys():
        valor = []
        for i in inventario[key]:
            valor.append(i[0]*i[1])
        vt[key] = valor
    return vt

def valor_total_inventario(inventario):
    vti = {}
    for key in inventario.keys():
        vti[key] = sum(inventario[key])
    return vti

def add_producto(inventario, nombre, lista):
    inventario[nombre] = lista

def control(inventario):
    informe = {}
    for key in inventario.keys():
        control = []
        for i in inventario[key]:
            if i[1] < i[2]:
                control.append("ERROR EXISTENCIAS")
        informe[key] = control
    return informe
                

def start():     
    # Valor total de cada producto
    print("\nValor total de cada producto")
    vtp = valor_total(inventario)
    for i in vtp.keys():
        print("\t", i, " -> ", vtp[i])
        
    # Valor total del inventario
    print("\nValor total del inventario")
    vti = valor_total_inventario(vtp)
    for i in vti.keys():
        print("\t", i, " -> ", vti[i])

    # Añadir nuevos productos
    nombre = input("Introduce el nombre del producto: ")
    lista = []
    for i in range(3):
        print("Tienda ", (i+1))
        precio = float(input("Introduce el precio : "))
        cant_dis = int(input("Introduce la cantidad disponible: "))
        cant_min = int(input("Introduce la cantidad mínima: "))
        tupla = (precio, cant_dis, cant_min)
        lista.append(tupla)
    print("nombre: ", nombre, "lista: ", lista)
    add_producto(inventario, nombre, lista)
    for key in inventario.keys():
        print(key, " -> ", inventario[key])

    # Control de existencias
    print("\nControl de existencias")
    informe = control(inventario)
    for i in informe.keys():
        print("- ", i, " -> ", informe[i])

start()
