""" Dada una lista de cadenas desordenadas: 
frutas = ["naranja", "manzana", "banana", "kiwi", "cereza"]
Modifica la función de Merge Sort para ordenar la lista alfabéticamente."""

fruit = ["naranja", "manzana", "banana", "kiwi", "cereza"]

def merge_sort(list_string):
    if len(list_string) > 1:
        middle = len(list_string) // 2
        left_list = list_string[middle:]
        right_list = list_string[:middle]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_string[k] = left_list[i]
                i += 1
            else:
                list_string[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list_string[k] =  left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list_string[k] = right_list[j]
            j += 1
            k += 1
        print(f'Meszclado: {list_string}')

print('Lista original: ', fruit)
print()
merge_sort(fruit)
print('Lista ordenada: ', fruit)   