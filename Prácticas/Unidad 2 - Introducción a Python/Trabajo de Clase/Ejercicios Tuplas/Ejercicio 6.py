### Ejercicio 6

datos = {
    "Manel": [("matematicas", True, "regular"), ("lengua", True, "bueno"), ("historia", False, "regular"), ("inglés", True, "malo")],
    "Hada": [("matematicas", False, "regular"), ("lengua", True, "malo"), ("historia", True, "malo"), ("inglés", False, "malo")],
    "Zeta": [("matematicas", True, "bueno"), ("lengua", True, "bueno"), ("historia", True, "regular"), ("inglés", True, "bueno")],
    "Raúl": [("matematicas", True, "malo"), ("lengua", False, "regular"), ("historia", True, "bueno"), ("inglés", False, "malo")],
    "Samuel": [("matematicas", False, "malo"), ("lengua", True, "malo"), ("historia", False, "malo"), ("inglés", True, "regular")]
    }
"""
manel = {"asistencia": xx%, "comportamiento": "xxx"}
"""
manel = {}
hada = {}
zeta = {}
raul = {}
samuel = {}

def asistencia(datos_alumno):
    asist = 0
    for i in datos_alumno:
        if i[1]:
            asist += 1
            
    porc = str((asist/4)*100)+"%"
    return porc
    
def comportamiento(datos_alumno):
    cont = 0
    for i in datos_alumno:
        if i[2] == "malo":
            cont += 1
            if cont > 1:
                return "malo"
    return "aceptable"

manel["Asistencia"] = asistencia(datos["Manel"])
hada["Asistencia"] = asistencia(datos["Hada"])
zeta["Asistencia"] = asistencia(datos["Zeta"])
raul["Asistencia"] = asistencia(datos["Raúl"])
samuel["Asistencia"] = asistencia(datos["Samuel"])

manel["Comportamiento"] = comportamiento(datos["Manel"])
hada["Comportamiento"] = comportamiento(datos["Hada"])
zeta["Comportamiento"] = comportamiento(datos["Zeta"])
raul["Comportamiento"] = comportamiento(datos["Raúl"])
samuel["Comportamiento"] = comportamiento(datos["Samuel"])

print("MANEL -> ", manel)
print("HADA -> ", hada)
print("ZETA -> ", zeta)
print("RAÚL -> ", raul)
print("SAMUEL -> ", samuel)

