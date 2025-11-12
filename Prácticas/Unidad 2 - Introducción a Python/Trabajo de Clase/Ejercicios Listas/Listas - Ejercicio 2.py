# Paso 1
beatles = []
# Paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

# Paso 3

for i in range(2):
    nombre = input(str("Introduce el nombre: "))
    beatles.append(nombre)

print(beatles)

# Paso 4

del beatles[3:]

print(beatles)

# Paso 5

beatles.insert(0, "Ringo Starr")

print(beatles)

# Paso 6

print(f"Beatles: {beatles} , {len(beatles)} integrantes")
