### Ejercicio 2

def gestion_inventario(accion, inventario, producto=None, cantidad=0):
    if accion == "agregar":
        if producto in inventario:
            inventario[producto] += cantidad
            print("Cantidad actualizada")
        else:
            inventario[producto] = cantidad
            print( f"Producto {producto} agregado. Cantidad total: {inventario[producto]}")
    
    elif accion == "eliminar":
        if producto in inventario:
            if inventario[producto] >= cantidad:
                inventario[producto] -= cantidad
                if inventario[producto] == 0:
                    del inventario[producto]
                print( f"Producto {producto} eliminado. Cantidad restante: {inventario.get(producto, 0)}")
            else:
                print( "Cantidad a eliminar excede la cantidad en inventario.")
        else:
            print( "Producto no encontrado en inventario.")
    
    elif accion == "buscar":
        if producto in inventario:
            print( f"Producto {producto} encontrado. Cantidad: {inventario[producto]}")
        else:
            print( "Producto no encontrado en inventario.")
    
    else:
        print( "Acción no válida. Use 'agregar', 'eliminar' o 'buscar'.")

inventario = {"Monitor AOC": 5, "Raton AS": 3, "Teclado AKKO": 1,
              "Alfombrilla WL": 10, "Mando MambaOne": 0}

# gestion_inventario(accion, inventario, producto=None, cantidad=0)

def pruebas():
    """ Agregar productos """
    # Agregar producto que no existe
    gestion_inventario("agregar", inventario, "Mando PS3", 1)
    # Agregar producto que existe. 
    gestion_inventario("agregar", inventario, "Monitor AOC", 1)

    """ Eliminar productos """
    # Eliminar producto que NO existe
    gestion_inventario("eliminar", inventario, "xxx", 2)
    # Eliminar produto que existe (cantidad > inventario)
    gestion_inventario("eliminar", inventario, "Raton AS", 5)
    # Eliminar producto que existe (inentario == 0)
    gestion_inventario("eliminar", inventario, "Mando MambaOne", 1)
    # Eliminar pruedo que existe
    gestion_inventario("eliminar", inventario, "Alfombrilla WL", 4)

    """ Buscar producto """
    # Buscar producto que NO existe
    gestion_inventario("buscar", inventario)
    # Buscar producto que existe
    gestion_inventario("buscar", inventario, "Raton AS")

    """ Opcion no válida """
    

    
pruebas()






    
