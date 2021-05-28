'''
EJERCICIO 1:
Escribir un programa que almacene una cadena de caracteres de  contraseña en una variable, 
ingresada por el usuario, pregunte al usuario por la contraseña e imprima por pantalla si 
la contraseña introducida por el usuario coincide con la guardada en la variable sin tener 
en cuenta mayúsculas y minúsculas.
'''
print("Ejercicio No. 1")

llave= "contraseña"
password=input("Introduce la Contraseña: ")
if llave== password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")
print("\n")

'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''
print("Ejercicio No. 2 ")

nombre= input("¿Como te llamas?")
genero= input("¿Cual es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower()< "m":
        grupo= " A"
    else:
        grupo= " B"
else:
    if nombre.lower()>"n":
        grupo= " A"
    else:
        grupo= " B"
print("Tu grupo es: "+ grupo)
