#Escriba un programa en java que genere aleatoriamente (Ayuda: Vea la clase Math para saberr cómo generar números aleatorios en java) un array de números reales, y lo ordene mediante un método de ordenamiento (burbuja, selección o inserción) de menor a mayor.La cantidad de números será definida por el usuario

import random
list = []
x = int(input("numero:\n"))
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

#Elabore una aplicación que permita introducir 20 elementos de tipo entero en un arreglo, el programa mostrara impreso el arreglo en orden inverso.

lista = []
print("Digite Sus 20 Numeros")
valores = 20
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Elemento")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
lista.sort(reverse=True)
print(("El Orden De Sus Elementos Esta De Mayor A Menor\n"), (lista))

#3. Hacer un programa que lea diez valores enteros en un array y los muestre en pantalla. después que los ordene de menor a mayor y los vuelva a mostrar. y finalmente que los ordene de mayor a menor y los muestre por tercera vez.

lista = []
for i in range (10):
  x = lista.append(int(input(
"Digite un numero\n")))
print(lista)
lista.sort()
print (lista)
lista.sort(reverse=True)
print(lista)

# Elabore un programa que encuentre al número mayor y menor de un arreglo y luego muestre en qué posición se encontraban estos números originalmente.

list = [34, 45, 2, 78, 6, 98,7, 0, 78, 65]

for y in list:
  mayor = max(list)
  posicion_mayor = list.index(mayor)
  menor = min(list)
  posicion_menor = list.index(menor)
  
print(mayor)
print(posicion_mayor)
print(list)

# elabore un programa que permita introducir un arreglo de 10 elementos, el programa mostrara un histograma de esos datos (el histograma se interpretara con la salida de n asteriscos donde n es el valor de cada elemento del arreglo) ej.: el arreglo es 2,3,4 el histograma será 2->** 3->*** 4->****

list = []

for asteriscos in range(10):
  list.append(int(input("Digite un numero\n")))

for x in list:
  print(x,'->', x * "*" )

# Elabore un programa que permita introducir un arreglo de 25 elementos de tipo entero. luego pedir al usuario que introduzca un número. el programa mostrara el número de veces que se repite dicho valor en el arreglo



lista = []

for x in range (25):
  num = lista.append(int(input(f"Llevas Digitado {x + 1} Numeros: ")))

rep = int(input("Digite el numero el cual quiera saber si esta repetido"))
a = lista.count(rep)
print(f"El arreglo digitados es: {lista}\nEl numero esta digitado: {a}")


#Elabore un programa que permita introducir un arreglo de 8 elementos de tipo entero. El programa mostrara un arreglo en donde muestre un 1 para los primos y un 0 para los no primos.

lista = []

par = []
impar = []
for a in range (8):
  num = lista.append(int(input(f"Llevas Digitado {a + 1} Numeros: ")))
for i in range(8):
  if lista[i] % 2 == 0:
   par.append(lista[i])
  else:
    impar.append(lista[i])
impar.sort() , par.sort()
print(f"Los Numeros digitados son: \n{lista}\nLos  impares Del arreglo son: \n{impar}\nLos numeros pares del arreglo on: \n{par}")