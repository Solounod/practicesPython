
"""Ejercicio de ordenamineto por seleccion
 curso de Programacion ats de youtube curso de programacion en c++"""


lista = [3, 4, 1, 9, 2, 5]

def order_select(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i + 1,len(lista)):
            
            if lista[j] < lista[min]:
                min = j
            
        
        aux = lista[i]
        lista[i] = lista[min]
        lista[min] = aux
    
    return lista

print(order_select(lista))