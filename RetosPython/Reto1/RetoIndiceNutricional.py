# ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
edad = int(𝑖𝑛𝑝𝑢𝑡("Indicar la edad del paciente:"))
peso = 𝑓𝑙𝑜𝑎𝑡(𝑖𝑛𝑝𝑢𝑡("Indicar el peso del paciente en kilogramos:"))

ac = 60.1
ap = 30.5
av = -24.4
dia = 0
pesoengramos = (peso*1000)

if(edad >= 5 and edad <= 10):
    if(peso < 16):
        estado = "A"
        dieta = ((ac*2)+(ap*1)+(av*2))
        while pesoengramos < 22001:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    elif(peso > 28):
        estado = "B"
        dieta = (ac*0.6)+(ap*1)+(av*4)
        while pesoengramos > 24000:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    else:
        estado = "C"
        dieta = (ac*0.5)+(ap*0.7)+(av*2)
        while pesoengramos < 28001:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance el peso máximo")

elif(edad > 10 and edad <= 13):
    if(peso < 30):
        estado = "A"
        dieta = (ac*2)+(ap*1)+(av*2)
        while pesoengramos < 32001:
            pesoengramos = pesoengramos+dieta
            dia = dia+1

        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    elif(peso > 50):
        estado = "B"
        dieta = (ac*0.6)+(ap*1)+(av*4)
        while pesoengramos > 43000:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    else:
        estado = "C"
        dieta = (ac*0.5)+(ap*0.7)+(av*2)
        while pesoengramos < 50001:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance el peso máximo")

elif(edad > 13 and edad <= 17):
    if(peso < 51):
        estado = "A"
        dieta = (ac*2)+(ap*1)+(av*2)
        while pesoengramos < 56001:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    elif(peso > 63):
        estado = "B"
        dieta = (ac*0.6)+(ap*1)+(av*4)
        while pesoengramos > 58000:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance un peso saludable")
    else:
        estado = "C"
        dieta = (ac*0.5)+(ap*0.7)+(av*2)
        while pesoengramos < 63000:
            pesoengramos = pesoengramos+dieta
            dia = dia+1
        print(
            f"El estado nutricional del paciente es {estado} y se requieren {dia} días de dieta para que alcance el peso máximo")

else:
    print("La edad digitada no está dentro del rango permitido")
