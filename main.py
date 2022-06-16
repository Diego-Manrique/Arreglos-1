#Escriba un programa en java que genere aleatoriamente (Ayuda: Vea la clase Math para saberr cómo generar números aleatorios en java) un array de números reales, y lo ordene mediante un método de ordenamiento (burbuja, selección o inserción) de menor a mayor.La cantidad de números será definida por el usuario

import random
list = []
x = int(input("sedgsfghd\n"))
for uwu in range(x):
  list.append(random.randint(1,100))

def fck (list):
  f = len(list)
  for x in range (f -1):
   for y in range (0, f -x -1):
      if list [y] > list [y + 1]:
        list[y], list [y + 1 ] = list [y+1 ], list [y]
print (fck(list))
      
print(list)