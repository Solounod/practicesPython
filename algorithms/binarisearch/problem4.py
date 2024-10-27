"""Implementa una búsqueda binaria que funcione con una lista de cadenas ordenadas alfabéticamente. Por ejemplo, busca la palabra "manzana" en la siguiente lista:"""

fruit = ["banana", "cereza", "fresa", "manzana", "naranja", "pera"]


def binari_search(string_list, objetive_word):
    initial = 0
    end = len(string_list) - 1

    while initial <= end:
        middle = (initial + end) // 2
        value_middle = string_list[middle]

        if value_middle == objetive_word:
            return middle
        elif value_middle < objetive_word:
            initial = middle + 1
        else:
            end = middle - 1

    return print("Nose encuentra la palabra objetivo")

objetive = "manzana"
result = binari_search(fruit, objetive)

print(f"La palabra objetivo se envuentra en el indice {result}")
        
