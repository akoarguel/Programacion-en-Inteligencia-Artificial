# Ejercicio 3

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

def numero_dia(year, month, day):
##    meses = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##    dias_totales = 0
##    if es_bisiesto(year):
##        meses.insert(1, 29)
##    else:
##        meses.insert(1,28)
##        
##    for i in meses[:(month-1)]:
##        dias_totales += i
##    return (dias_totales+day)
    
    dias_totales = 0
    for i in range(month-1):
        dias_totales += dias_del_mes(year, (i+1))
    return dias_totales + day

test_years = [1900, 2000, 2016, 1987, 1872, 2020, 2003, 1999, 756]
test_months = [2, 2, 1, 11, 4, 7, 10, 8, 3]
test_days = [6, 8, 30, 31, 10, 26, 9, 22, 31]
test_results = [37, 39, 30, 335, 101, 208, 282, 234, 91]

for i in range(len(test_years)):
    dias = numero_dia(test_years[i], test_months[i], test_days[i])
    print(f"{test_days[i]}/{test_months[i]}/{test_years[i]} es el día {dias} del año")
