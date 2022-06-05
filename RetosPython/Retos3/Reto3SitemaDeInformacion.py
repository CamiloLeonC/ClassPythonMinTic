import numpy as np
import random

def encriptado(texto):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL ENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DE LOS
    #RETORNOS PUESTOS AL FINAL DE ESTA FUNCIÓN
    
    lista = list(texto)
    tamaño_lista = np.sqrt(len(lista))
    codigo_unicode = []
    array_aleatorio = []  
    array_final = []
    
    if tamaño_lista.is_integer() == False: #para saber si la raiz del tamaño de la  lista es entero, si es False agrega underscore '_' 
      while tamaño_lista.is_integer() == False: #mientras la raiz del tamaño de la lista no sea entero agregará espacios en blanco underscore '_'
        lista.append('_')
        tamaño_lista = np.sqrt(len(lista))
      tamaño_lista = int(tamaño_lista)
      
      for i in range(len(lista)): #para convertir letras a código ascii, aquí tovadía están en orden
        x= [ord(lista[i])]
        codigo_unicode.append(x)

      numeros = range(len(lista)) # (0,tamaño de la lista)
      indice = list(numeros) # crea la lista de números que serán los índices
      random.shuffle(indice) # desordena la lista de números
      clave = indice #guarda los índices en la variable clave
      

      for j in range(len(clave)):
        aux = clave[j]
        array_aleatorio.append(codigo_unicode[aux]) #ubica según la clave cada letra en la lista array_aleatorio
      array_final = np.array(array_aleatorio).reshape(tamaño_lista,tamaño_lista) #ubica las letras en codigo ascii en matriz de dimensiones iguales 

      return array_final, clave

    else: #si la raiz del tamaño lista es entero entonces no agrega espacios en blanco, continua con el proceso de convertir a ascii
      tamaño_lista = int(tamaño_lista)
      for i in range(len(lista)):
        x= [ord(lista[i])]
        codigo_unicode.append(x)
      
      numeros = range(len(lista))
      indice = list(numeros)
      random.shuffle(indice)
      clave = indice

      for j in range(len(clave)):
        aux = clave[j]
        array_aleatorio.append(codigo_unicode[aux])
      array_final = np.array(array_aleatorio).reshape(tamaño_lista,tamaño_lista)


    return array_final, clave


def desencriptado(array_encriptado, clave):
    
    #ESCRIBA EN ESTA REGIÓN SU PROPUESTA DE SOLUCIÓN PARA EL DESENCRIPTADO
    #USANDO EL MÉTODO EXPUESTO EN EL ENUNCIADO. ATÉNGASE AL USO DEL
    #RETORNO PUESTO AL FINAL DE ESTA FUNCIÓN
    
    codigo_unicode = array_encriptado.flatten().tolist() #conviete la matriz en una dimensión flatten(), tolist() en una lista
    caracter_unicode = []
    caracter_ordenado = []
    texto_sin_blancks = []
    texto = []
    
    for i in range(len(codigo_unicode)): #para convertir código ascii a caracter, aquí tovadía están en el orden que llegaron
        x= [chr(codigo_unicode[i])]
        caracter_unicode.append(x)

    for i in range(len(codigo_unicode)):#ordena caracteres según la clave
      aux = clave.index(i)
      caracter_ordenado.append(caracter_unicode[aux])
    
    caracter_ordenado = np.array(caracter_ordenado) # convierte en array para comparar en el condicional si posee el caracter '_'
   
    for i in range(len(caracter_ordenado)): 
      if caracter_ordenado[i] == '_':
        break
      else:
        texto_sin_blancks.append(caracter_ordenado[i]) # va guardando caracteres diferentes a '_' en otra variable, esto con el fin de eliminar los underscore
        
    for i in range(len(texto_sin_blancks)):
      texto.extend(texto_sin_blancks[i]) # sin esta linea se imprime [T],[o],[d] (como si fueran varias listas)..... pero con esta linea queda [T,o,d,a,y....] 
      
    texto = "".join(texto) # convierte la lista a cadena 'Today is....'
    
    
    return texto