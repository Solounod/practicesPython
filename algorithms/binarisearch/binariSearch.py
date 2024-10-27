
"""Dada la siguiente lista ordenada de números enteros:"""

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""Escribe una función que use búsqueda binaria para determinar si el número 14 está en la lista. Si está, retorna su índice; de lo contrario, retorna -1."""

def binari_search(numbers, objetive):
    initial = 0
    end = len(numbers) -1

    while initial <= end:
        middle = (initial + end) // 2
        value_middle = numbers[middle]

        if value_middle == objetive:
            return middle
        elif value_middle < objetive:
            initial = middle + 1
        else:
            end = middle - 1

    return -1

objetive = 14
result = binari_search(numbers, objetive)

if result != -1:
    print(f"elemento encontrado en el indice {result}")
else:
    print("Elemento no encontrado retorno -1")