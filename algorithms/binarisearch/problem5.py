"""Dada una lista ordenada, escribe una función que determine la posición donde se puede insertar un nuevo elemento 
de manera que la lista permanezca ordenada. Por ejemplo, inserta el número 5 en la siguiente lista:"""

list_1 = [1, 3, 4, 7, 9]

"""La función debe retornar el índice donde 5 debería ser insertado."""

def binari_search(list_numbers, objetive):
    initial = 0
    end = len(list_numbers) - 1
    
    while initial <= end:
        middle = (initial + end) // 2
        value_middle = list_numbers[middle]

        if value_middle == objetive:
            return middle
        elif value_middle < objetive:
            initial = middle + 1
        else:
            end = middle - 1
    #index = middle + 1

    return print(f"El numero no se encuentra deberia insertarce en el indice {middle}")

number_objetive = 2
result = binari_search(list_1, number_objetive)

