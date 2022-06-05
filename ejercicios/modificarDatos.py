#Eliminar espacios en blanco al comienzo y al final de la cadena
a = "  Today is a beautiful day "
print(a.strip()) #Elimina espacios en blanco al comienzo y al final de la cadena

#remplazar caracteres en blanco por una cadena vacía
b = "  Today is a beautiful day "
print(b.replace(" ","")) #remplaza espacios en blanco por una cadena vacía
print(b.replace("T","t")) #remplaza T por una t 

#Separar cadesa en una lista
c = "Today is a beautiful day"
print(c.split()) #Separa la cadena en una lista

#Concatenar cadenas
d = "Today"
e = " is a "
f = "beautiful"
g = d+e+f
print(d+e+f) #Concatena cadenas
print(g) #Concatena cadenas

#Convertir una cadena a mayúsculas
h = "today is a beautiful day"
print(h.upper()) #Convierte la cadena a mayúsculas

#Convertir una cadena a minúsculas
i = "TODAY IS A BEAUTIFUL DAY"
print(i.lower()) #Convierte la cadena a minúsculas

#Calcular tamaño de una cadena
j = "Today is a beautiful day"
print("El tamaño es de la cadena es", len(j)) #Calcula el tamaño de la cadena

#Comprobar si un objeto es entero o no
x = 5
print(isinstance(x, int)) #Comprueba si x es entero

