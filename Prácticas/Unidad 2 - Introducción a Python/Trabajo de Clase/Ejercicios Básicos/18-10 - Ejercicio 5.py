##Escribir un programa que realice un juego que consiste en adivinar un número (puedes inicializar una 
##variable con ese valor). Para ello se pedirá al usuario que ingrese un número entero; comprobará si el 
##número ingresado por el usuario es el mismo que el número elegido. Si los números son diferentes, el 
##usuario debería ver el mensaje "¡Frío, frío!" y se le solicitará que ingrese un número nuevamente. Si el 
##número ingresado por el usuario coincide con el número elegido, el número debe imprimirse en la 
##pantalla, junto con las palabras: "¡Bien hecho!" 

numero = 8

n_usuario = int(input("Introduce el número: "))
while(n_usuario != numero):
    print("¡Frío, frío!")
    n_usuario = int(input("Introduce otra vez el número: "))
else:
    print("¡Bien hecho!")
