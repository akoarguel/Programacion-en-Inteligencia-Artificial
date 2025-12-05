### Ejercicio 2

notas = {"lengua": (6.5, 4.3, 7.7),
         "matematicas": (8.5, 9.8, 9.1),
         "fisica": (7.9, 8.8, 6.9),
         "ingles": (4.2, 4.8, 5.5)
    }

def mostrar_notas(notas):
    print("-------")
    for asig, nota in sorted(notas.items()):
        print(asig, ": ", nota)

def calcular_media(notas):
    medias = {}
    for asig, nota in sorted(notas.items()):
        media = sum(nota) / len(nota)
        medias.update({asig:round(media, 2)})
    return medias

def start():
    print("\nNotas de PEDRO: ")
    mostrar_notas(notas)
    print("\nNotas medias: ")
    mostrar_notas(calcular_media(notas))

start()
