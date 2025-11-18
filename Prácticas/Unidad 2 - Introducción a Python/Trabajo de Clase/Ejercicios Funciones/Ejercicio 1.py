# Ejercicio 1

def es_bisiesto(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987, 1872, 2020, 2003, 1999, 756]
test_results = [True, True, True, False, True, True, False, False, True]

for i in test_data:
    print(f"{i} es bisiesto? {es_bisiesto(i)}")
    test_results.append(es_bisiesto(i))

