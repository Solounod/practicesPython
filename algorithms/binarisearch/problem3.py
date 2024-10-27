"""Usa búsqueda binaria para buscar el número 7 en la siguiente lista ordenada:"""

list_1 = [1, 3, 5, 9, 11, 13]

"""¿Qué valor retorna la función? Explica por qué."""

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

    return print(f"El numero no se encuentra {middle}")

number_objetive = 7
result = binari_search(list_1, number_objetive)

