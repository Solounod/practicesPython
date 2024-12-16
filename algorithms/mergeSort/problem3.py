""" Dada la siguiente lista que contiene elementos duplicados:
lista = [4, 2, 5, 2, 3, 4, 1]
Usa Merge Sort para ordenar la lista y verifica que los elementos duplicados mantengan su orden relativo."""

numbers = [4, 2, 5, 2, 3, 4, 1]

def merge_sort(list_numbers):
    if len(list_numbers) > 1:
        middle = len(list_numbers) // 2
        left_list = list_numbers[middle:]
        right_list = list_numbers[:middle]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_numbers[k] = left_list[i]
                i += 1
            else:
                list_numbers[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            list_numbers[k] =  left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list_numbers[k] = right_list[j]
            j += 1
            k += 1
        print(f'Meszclado: {list_numbers}')

print('Lista original: ', numbers)
print()
merge_sort(numbers)
print('Lista ordenada: ', numbers)   