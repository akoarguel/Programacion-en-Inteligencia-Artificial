import random

temps = []
for i in range(31):
    day = []
    for j in range(24):
        day.append(0.0)
    temps.append(day)


for i in range(31):
    for j in range(23):
        temps[i][j] = round(random.uniform(0,50),1)
print(temps)

mediodia = 12
media = round(sum(temps[day][mediodia] for dia in range(day) / day,2))
print("Temperatura promedio al mediodia: " + str(media)
