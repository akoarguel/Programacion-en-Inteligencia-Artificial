### Ejercicio 1

def clasificar_persona(edad, estado_civil):
    if edad < 18:
        return "Menor de edad"
    elif edad >= 18 and edad <= 65:
        if estado_civil == "soltero":
            return "Adulto soltero"
        elif estado_civil == "casado":
            return "Adulto casado"
        else:
            return "Estado civil desconocido"
    else:
        return "Persona mayor"

edades = [16, 25, 30, 28, 20, 36, 39, 68, 70, 40, 55]
estados = ["soltero", "soltero", "casado",
           "casado", "soltero", "casado",
           "casado", "casado", "soltero",
           "casado", ""]

def start():
    for i in range(len(edades)):
        print("\nedad: ", edades[i], " | estado civil: ", estados[i])
        print("\t ---", clasificar_persona(edades[i], estados[i]), "---")

start()
