# Ejercicio 2

def es_bisiesto(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def dias_del_mes(year, month):
    meses = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if es_bisiesto(year):
        meses.insert(1, 29)
    else:
        meses.insert(1,28)
    
    return meses[(month-1)]

test_data = [1900, 2000, 2016, 1987, 1872, 2020, 2003, 1999, 756]
test_months = [2, 2, 1, 11, 4, 7, 10, 8, 3]
test_results = [28, 29, 31, 30, 30, 31, 31, 31, 31]

for i in range(len(test_data)):
    dias = dias_del_mes(test_data[i],test_months[i])
    print(f"{test_months[i]}/{test_data[i]} tiene {dias_del_mes(test_data[i],test_months[i])} dias")
