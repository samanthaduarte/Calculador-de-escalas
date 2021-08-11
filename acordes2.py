
notaInput = input("Por favor ingrese la nota:\n")
notaIndex = 0
escala = []
escala1 = []
escala2 = []
notasEscala = []
contador = 5
notas = ["do","do#","re","re#","mi","fa","fa#","sol","sol#","la","la#","si"]

#Sacar escala
print("Escala: ")

for i in range(len(notas)):
    if(notaInput == notas[i]):
      sl1 = slice(0,i)

escala1 = notas[sl1]

notas.reverse()

for i in range(len(notas)):
    if(notaInput == notas[i]):
      sl2 = slice(0,i+1)

escala2 = notas[sl2]

escala2.reverse()

notasEscala = escala2 + escala1

escala.append(notasEscala[0])
escala.append(notasEscala[2])
escala.append(notasEscala[4])
escala.append(notasEscala[5])
escala.append(notasEscala[7])
escala.append(notasEscala[9])
escala.append(notasEscala[11])
escala.append(notasEscala[0])

print(escala)

#Sacar acordes
escala.pop()

print("Acordes: ")

acordes = []
  
for i in range(7):
  acorde = []
  acorde.append(escala[i%7])
  acorde.append(escala[(i+2)%7])
  acorde.append(escala[(i+4)%7])
  acordes.append(acorde)
  i+=1

for i in range(len(acordes)):
  if(i == 0 or i == 3 or i == 4):
    print(acordes[i][0],"mayor:")
  elif(i == 1 or i == 2 or i == 5):
    print(acordes[i][0],"menor:")
  elif(i == 6):
    print(acordes[i][0],"disminuido:")
  print(acordes[i])
