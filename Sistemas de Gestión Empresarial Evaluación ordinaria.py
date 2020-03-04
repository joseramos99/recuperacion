def ej1():
	lista = [] 
	salir = False
	while(not salir):
	    numero = int(input("Dame un numero: "))
	    if(numero == 0):
	        salir=True
	    else:
	        lista.append(numero)

	lista.sort()
	 
	print(lista)

def ej2():
	lista = []
 
	salir = False
	 
	while(not salir):
	    numero = int(input("Dame un numero: "))
	    if(numero == 0):
	        salir=True
	    else:
	        lista.append(numero)
	
	lista.sort(reverse=True)
	 
	print(lista)

def ej3():
	numeros = (5,4,3,-2,1,6,455,3,6,6,6,6,6)
 
	maximo = numeros[0]
	minimo = numeros[0]
	 
	for i in numeros:
	    if i > maximo:
	        maximo = i
	 
	    if i < minimo:
	        minimo = i
	 
	print("El maximo es ",maximo)
	print("El minimo es ",minimo)

def ej4():
	lista = []
 
	suma = 0
	media = 0
	numero = 0
	 
	for i in range(10):
	    numero = int(input("Dame un numero: "))
	    lista.append(numero)
	    suma += numero
	 
	for i in lista:
	    print(i)
	 
	media = suma / len(lista)
	 
	print("La suma es ",suma)
	print("La media es ",media)

def ej5():
	numeros = (1,2,3,4,5)

	lista = list(numeros)

	lista[3] = 20

	numeros = tuple(lista)

#EJERCICIO 6

def cargar(cant):
lista=[]
for x in range(cant):
    string=input("Ingrese un string: ")
    lista.append(string)
return lista

def comprobar(lista):
    for x in range(len(lista)):
         if len(lista[x])>5:
             print(lista[x],"",sep=" - ",end="")

lista=cargar(5)

comprobar(lista)