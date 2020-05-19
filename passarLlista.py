import os
from datetime import date

directoriMatricula="matricula"
directoriAssistencia="assistencia"
directoriGrups="grups"

opcioMenu =0
while (opcioMenu !=5):
  print("1- Configurar sistema")
  print("2- Fer fulls de grup")
  print("3- Passa llista")
  print("4- Consultar assistència")
  print("5- Sortir")
  opcioMenu = int(input("Quina opció vols?"))
print("Adéu bon dia tinguis!")

if opcioMenu == 1:
  directoriMatricula = input("Entra directori")
  while (os.path.isdir(directori)) != True:
    directoriMatricula = input("Entra directori de matricula")
    
  print("És directori")
elif opcioMenu == 2:
  #TODO Obre'ls tots
  fitxer1 = open("ESO1.csv","w")
  fitxer2 = open("ESO2.csv","w")
  fitxer3 = open("ESO3.csv","w")
  fitxer4 = open("ESO4.csv","w")
  fitxer5 = open("BAT1.csv","w")
  fitxer6 = open("BAT2.csv","w")
  fitxer = open("matricula/alumnat.csv","r")
  fitxer.read()
  for linia in fitxer:
    #TODO convertir la línia (String) a una llista
    linia = linia.split(",")
    if linia[1] == 11 or linia[2] == 12:
      fitxer1.write(linia[0]+linia[1]+linia[2])
    elif linia[1] == 13:
      fitxer2.write(linia[0]+linia[1]+linia[2])
    elif linia[1] == 14:
      fitxer3.write(linia[0]+linia[1]+linia[2])
    elif linia[1] == 15:
      fitxer4.write(linia[0]+linia[1]+linia[2])
    elif linia[1] == 16:
      fitxer5.write(linia[0]+linia[1]+linia[2])
      # , ,
    elif linia[1] == 17 or linia[1] == 18:
      fitxer6.write(linia[0],linia[1],linia[2])
    
    
