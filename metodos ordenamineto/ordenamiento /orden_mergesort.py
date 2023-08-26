lista = [3, 4, 1, 9, 2, 5]

def merge(list_left, list_rigth):
    index_array_order = 0
    index_left = 0 
    index_rigth = 0
    array_order = []

    while(index_left < len(list_left) and index_rigth < len(list_rigth)):
        if list_left[index_left] < list_rigth[index_rigth]:
            array_order.append(list_left[index_left])
            index_left += 1
        else:
            array_order.append(list_rigth[index_rigth])
            index_rigth += 1

        index_array_order += 1

    while index_left < len(list_left):
        array_order.append(list_left[index_left])
        index_left += 1

    while index_rigth < len(list_rigth):
        array_order.append(list_rigth[index_rigth])
        index_rigth += 1

    return array_order


def merge_sort(lista):
    if len(lista) < 2:
        return lista

    else:
        middle = len(lista) // 2
        right = merge_sort(lista[middle:])
        left = merge_sort(lista[:middle])
        return merge(right, left)





print(merge_sort(lista))

