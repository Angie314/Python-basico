''' 
EJERCICIO NO.1
Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
triángulo rectángulo como el de 
 abajo, de altura el número introducido.
'''
n= int(input("Introduce la altura del Triangulo:"))  

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

'''
EJERCICIO NO.2
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas
'''
n=int(input("Introduce un numero entero positivo:"))

for i in range(n, -1, -1):
    print(i, end=", ")
print("\n")

'''
EJERCICIO NO.3
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
número primo o no.
'''
n=int(input("Introduce un numero entero positivo mayor que 2:"))

i=2
while n% i!=0:
    i += 1
if i==n:
    print(str(n)+" es un numero primo")
else:
    print(str(n)+" no es un numero Primo")