#!/usr/bin/python3

import random

dic1 = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}
dic2 = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"0"}
lista = []
lista_num = []

def numero():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de caracteres de la contraceña: "))
            break
        except (ValueError, NameError):
            print("Ese caracter no es correcto")

    for i in range(cantidad):
        generador = random.randint(1,10)
        caracter = dic2[generador]
        lista_num.append(caracter)
    contracena = "".join(lista_num)
    print(contracena)

def letras():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de caracteres de la contraceña: "))
            break
        except (ValueError, NameError):
            print("Ese caracter no es correcto")

    for i in range(cantidad):
        generador = random.randint(1,26)
        caracter = dic1[generador]
        lista.append(caracter)
    contracena = "".join(lista)
    print(contracena)


print("############Generador de contarceñas##############")
print()
print("=======Menu======")
print("1_Generar contaceña de numeros")
print("2_Generar contraceña de letras")
opcion = input("Ingrese la opcion: ")
if opcion == "1":
    numero()
elif opcion == "2":
    letras()
