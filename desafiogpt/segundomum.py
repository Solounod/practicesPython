"""Escribir una función que tome una lista de 
números como entrada y devuelva el segundo número más grande de la lista."""

list_enter = [2, 5, 8, 9]

def second_number(enter_list):
    list_aux = enter_list
    num_max = max(list_aux)
    list_aux.pop(list_aux.index(num_max))
    return max(list_aux)

print(second_number(list_enter))


