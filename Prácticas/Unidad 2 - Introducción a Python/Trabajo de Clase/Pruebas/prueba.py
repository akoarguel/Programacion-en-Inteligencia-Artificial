str = "code"
l = len(str)
front = str[l-1]
medio = str[1:l-1]
back = str[0]

def front_back(str):
  l = len(str)
  front = str[l-1]
  med = str[1:l-1]
  back = str[0]
  return (front+med+back)

def front3(str):
  if len(str) <= 0:
    return str
  str2 = str[len(str)-3]
  return str2

print(front3("Chocolate"))
print(front_back("code"))