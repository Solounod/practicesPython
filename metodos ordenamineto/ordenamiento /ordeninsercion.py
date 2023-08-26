"""Ejercicio de ordenamineto por insercion 
referencia curso de Programacion ats de youtube curso de programacion en c++"""


lista = [3, 4, 1, 9, 2, 5]

def orden_incert(lista):
    for i in range(len(lista)):
        pos = i
        aux = lista[i]

        while (pos >  0) and (lista[pos-1] > aux):
            lista[pos] = lista[pos-1]
            pos -= 1
            lista[pos] = aux

    return lista

orden_incert(lista)
print("Orden ascendente")
for i in range(len(lista)):
    print(lista[i], end=" ")
print("\n")
print("orden descendente")
for i in range(-1,-len(lista)-1,-1):
    print(lista[i],end=" ")
print("\n")
    