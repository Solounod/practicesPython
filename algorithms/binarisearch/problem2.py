"""Dada una lista ordenada que puede contener elementos duplicados:"""
"""Modifica la función de búsqueda binaria para que retorne el índice de la primera aparición del número 2."""

list_1 = [1, 2, 2, 2, 3, 4, 5]
list_2 = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9]


def binari_search(numbers, objetive):
    initial = 0
    end = len(numbers) -1

    while initial <= end:
        middle = (initial + end) // 2
        value_middle = numbers[middle]

        if value_middle == objetive:
            end = middle
            initial = 0
            if value_middle > numbers[middle -1]:
                return end
            
            else:
                end = middle - 1   
            #if value_middle == numbers[middle -1]:
                    
            
        elif value_middle < objetive:
            initial = middle + 1
        else:
            end = middle - 1

        

    return -1

objetive = 6
result = binari_search(list_2, objetive)

if result != -1:
    print(f"elemento encontrado en el indice {result}")
else:
    print("Elemento no encontrado retorno -1")