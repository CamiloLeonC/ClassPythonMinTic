estudiante1 = {"Cédula" : "00014301503", "Nombre" : "Pepito", "Nota_Fundamentos" : 4.3} 
estudiante2 = {"Cédula" : "1037678471", "Nombre" : "Fulanito", "Nota_Fundamentos" : 3.2}
estudiante3 = {"Cédula" : "71023567", "Nombre" : "Pancho", "Nota_Fundamentos" : 5}
estudiante4 = {"Cédula" : "32276123", "Nombre" : "Rita", "Nota_Fundamentos" : 4.7}
estudiante5 = {"Cédula" : "1036765245", "Nombre" : "Anita", "Nota_Fundamentos" : 4.7}
estudiante6 = {"Cédula" : "89122456", "Nombre" : "Pedrito", "Nota_Fundamentos" : 4.7}
estudiante7 = {"Cédula" : "289765345", "Nombre" : "Mat", "Nota_Fundamentos" : 4.8}
estudiante8 = {"Cédula" : "4576890", "Nombre" : "Dan", "Nota_Fundamentos" : 4.8}

estu1 = {"Cédula" : "0032145678", "Nombre" : "Valen", "Nota_Fundamentos" : 3}
estu2 = {"Cédula" : "1067678654", "Nombre" : "Cris", "Nota_Fundamentos" : 4.5}
estu3 = {"Cédula" : "45677890", "Nombre" : "John", "Nota_Fundamentos" : 4.5}
estu4 = {"Cédula" : "72033405", "Nombre" : "Carmen", "Nota_Fundamentos" : 4.5}
estu5 = {"Cédula" : "89245678", "Nombre" : "Jordan", "Nota_Fundamentos" : 4.5}
estu6 = {"Cédula" : "89766345", "Nombre" : "Pedro", "Nota_Fundamentos" : 2.3}
estu7 = {"Cédula" : "1045789098", "Nombre" : "Camilo", "Nota_Fundamentos" : 3.7}

grupo = [estudiante1,estudiante2,estudiante3,estudiante4,estudiante5,estudiante6,estudiante7,estudiante8] 

grup = [estu1,estu2,estu3,estu4,estu5,estu6,estu7] 
sum_notas = 0
for i in range (0,len(grupo)):
  sum_notas += grupo[i]["Nota_Fundamentos"]
promedio = sum_notas/len(grupo) 
print (promedio) 

uno = [] 
dos = [] 
tres = [] 
notas = []

for j in grupo:
  notas.append(j["Nota_Fundamentos"]) 
  notas = sorted(notas, reverse=True)


auxiliar = set(notas) 
auxiliar = sorted(auxiliar, reverse=True) 


a = [] 

for k in range (0,len(auxiliar)-1): 
  a.append(notas.count(auxiliar[k]))
if a[0] == 1: 
  uno.append(auxiliar[0])
elif 1 < a[0]:
  for q in range (0,a[0]):
    uno.append(auxiliar[0])

if a[1] == 1: 
  dos.append(auxiliar[1])
elif 1 < a[1]:
  for w in range (0,a[1]):
    dos.append(auxiliar[1])

if a[2] == 1: 
  tres.append(auxiliar[2])
elif 1 < a[2]:
  for w in range (0,a[2]):
    tres.append(auxiliar[2])

cc_uno=[] 
cc_dos=[] 
cc_tres=[]  

cuadro_honor = {1 : cc_uno, 
          2 : cc_dos, 
          3 : cc_tres} 

for e in range (0, len(grupo)): 
  if grupo[e]["Nota_Fundamentos"] == auxiliar[0]:
    cc_uno.append(grupo[e]["Cédula"])
  elif grupo[e]["Nota_Fundamentos"] == auxiliar[1]:
    cc_dos.append(grupo[e]["Cédula"])
  elif grupo[e]["Nota_Fundamentos"] == auxiliar[2]:
    cc_tres.append(grupo[e]["Cédula"])
      
print (cuadro_honor)


estu1 = {"Cédula" : "0032145678", "Nombre" : "Valen", "Nota_Fundamentos" : 3}
estu2 = {"Cédula" : "1067678654", "Nombre" : "Cris", "Nota_Fundamentos" : 4.5}
estu3 = {"Cédula" : "45677890", "Nombre" : "John", "Nota_Fundamentos" : 4.5}
estu4 = {"Cédula" : "72033405", "Nombre" : "Carmen", "Nota_Fundamentos" : 4.5}
estu5 = {"Cédula" : "89245678", "Nombre" : "Jordan", "Nota_Fundamentos" : 4.5}
estu6 = {"Cédula" : "89766345", "Nombre" : "Pedro", "Nota_Fundamentos" : 2.3}
estu7 = {"Cédula" : "1045789098", "Nombre" : "Camilo", "Nota_Fundamentos" : 3.7}


grup = [estu1,estu2,estu3,estu4,estu5,estu6,estu7] 
sum_notas = 0
for i in range (0,len(grup)):
  sum_notas += grup[i]["Nota_Fundamentos"]
promedio = sum_notas/len(grup) 
print (promedio) 

uno = [] 
dos = [] 
tres = [] 
notas = []

for j in grup:
  notas.append(j["Nota_Fundamentos"]) 
  notas = sorted(notas, reverse=True)


auxiliar = set(notas) 
auxiliar = sorted(auxiliar, reverse=True) 


a = [] 

for k in range (0,len(auxiliar)-1): 
  a.append(notas.count(auxiliar[k]))
if a[0] == 1: 
  uno.append(auxiliar[0])
elif 1 < a[0]:
  for q in range (0,a[0]):
    uno.append(auxiliar[0])

if a[1] == 1: 
  dos.append(auxiliar[1])
elif 1 < a[1]:
  for w in range (0,a[1]):
    dos.append(auxiliar[1])

if a[2] == 1: 
  tres.append(auxiliar[2])
elif 1 < a[2]:
  for w in range (0,a[2]):
    tres.append(auxiliar[2])

cc_uno=[] 
cc_dos=[] 
cc_tres=[]  

cuadro_honor = {1 : cc_uno, 
          2 : cc_dos, 
          3 : cc_tres} 

for e in range (0, len(grup)): 
  if grup[e]["Nota_Fundamentos"] == auxiliar[0]:
    cc_uno.append(grup[e]["Cédula"])
  elif grup[e]["Nota_Fundamentos"] == auxiliar[1]:
    cc_dos.append(grup[e]["Cédula"])
  elif grup[e]["Nota_Fundamentos"] == auxiliar[2]:
    cc_tres.append(grup[e]["Cédula"])
      
print (cuadro_honor)
