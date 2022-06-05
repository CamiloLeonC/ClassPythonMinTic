#Creamos una lista
cars = ["Ford", "Volvo", "BMW"]
#Calculamos el tamaño de la lista
x = len(cars)
print("longitud arreglo ",x)
i=0
#Imprimimos el contenido de la lista
while (i<x):
  print(cars[i])
  i=i+1

#Agregar un elemento a la lista al final
cars.append("Honda")
print("\nAgregamos un elemento a la lista al final")
print(cars)

#remover un elemento de la lista
cars.remove("Honda")
print("\nRemover un elemento de la lista")
print(cars)

#remover un elemento de la lista con pop
print("\nAgregamos un elemento a la lista al final")
cars.append("Honda")
print(cars)
print("\nRemover un elemento de la lista con pop")
cars.pop(3)
print(cars)

x=len(cars)
i=0
#Imprimimos el contenido de la lista
print("\nImprimimos el contenido de la lista")
#Buscar un elemento en la lista
for i in range(x):
  print(cars[i])
  i=i+1