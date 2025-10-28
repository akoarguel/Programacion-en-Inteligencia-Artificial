## Diseña un programa que convierta de millas a kilometros y viceversa

def conversion_millas(millas):
    m_conv = millas*1.61
    return m_conv

def conversion_kilometros(kilometros):
    k_conv = kilometros/1.61
    return k_conv

millas = float(input("Introduce las millas: "))
kilometros = float(input("Introduce los kilometros: "))
m_conv = round(conversion_millas(millas), 2)
k_conv = round(conversion_kilometros(kilometros),2)

print(f"{millas} millas son {m_conv} kilómetros")
print(f"{kilometros} kilometros son {k_conv} millas")
