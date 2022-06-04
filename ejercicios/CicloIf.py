a=3
b=11
c=4

if a>b:
  if a>c:
    if b>c:
      print("A es el mayor, B es el del medio y C es el menor")
    else:
      print("A es el mayor, C es el del medio y B es el menor")
  else:
    print("C es el mayor, A es el del medio y B es el menor")
elif b>c:
    if a>c:
      print("B es el mayor, A es el del medio y C es el menor ")
    else:
      print("B es mayor, C es el del medio y A es el menor")
else:
    print("C es el mayor, B es el del medio y A es le menor")