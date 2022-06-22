# edad = int(input('Introduce tu edad: '))

# if edad < 18:
#     print('Eres menor de edad')
# elif edad >= 18 and edad < 65:
#     print('Eres mayor de edad')

#Funciones
#usamos def nomFuncion(parametros):
#    bloque de codigo

#ejemplo:
# def suma(a, b):
#     return a + b

# Palindromo
palabra = 'oso'
tamano = len(palabra)
inicio=0
fin=tamano-1
while inicio <= tamano and fin >= 0:

    if palabra[inicio] == palabra[fin]:
        inicio += 1
        fin -= 1
        palindroo=True
    else:
        print('No es palindromo')
        palindroo=False

        break

if palindroo==True:
    print(palabra + ' Es palindromo')