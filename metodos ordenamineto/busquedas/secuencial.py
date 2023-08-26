
def sequential_search(date, list_search):
    band = False
    index = 0

    while band == False and index < len(list_search):
        if list_search[index] == date:
            band = True
        
        index += 1

    if band == False:
        print("El numero a buscar no existe en la lista")
    elif band == True:
        print(f"El numero encontrado esta el la posicion {index - 1}")


list_new = [2, 5, 6, 3, 9, 12, 8]
date = 3

sequential_search(date, list_new)
