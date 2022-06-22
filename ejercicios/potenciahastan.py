def potencia(num):
    cont = 1
    if num :
        print("No sea bobo socio, ponga un numero")
    else:    
        while (cont <10):
            resul = num ** cont
            print('Potencia de {} elevado a la {} es {}'.format(num, cont, resul))
            cont += 1

def run():
    num = int(input('Escribe el numero al cual quieres averiguarle la potencia: '))
    potencia(num)

if __name__ == "__main__":
    run()

