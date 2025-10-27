x = 2
y = 3
"""
if x>1:
    if y>3:
        y=x+y
        x+=10
    else:
        x=1
else:
    x=0

if x==0:
    print("Vale 0")
elif x==1:
    print("Vale 1")
elif x==2:
    print("Vale 2")
else:
    print("a saber que valor tendrá")

x=1
while x < 5:
    print("itero")
    x+=1
else:
    print("estoy en el else")
    
print(x)

x=input("Escribe tu nombre: ")
print(x)
y = int(input("Cuantos euros tienes? "))
y+=10
print("Ahora tienes más ")
print(y)
print("--------------")

for i in range(7,2,-2):
    if i<6:
        continue
    print("uno más")
    x+=1
else:
    print("estoy en el else")
print(x)
"""

print("uno","dos","tres", sep="-", end="****")
print("cuatro","cinco", sep="(º-º)")






    
