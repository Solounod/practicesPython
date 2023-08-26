def search_binari(search_list, data):
    inf = 0
    sup = len(search_list)
    band = False
    
    while inf <= sup:
        middle = (inf + sup) // 2
        if search_list[middle] == data:
            band = True
            break
        elif search_list[middle] > data:
            sup = middle
            middle = (inf+sup) // 2
        elif search_list[middle] < data:
            inf = middle
            middle = (inf + sup) // 2

    if band == True:
        print(f"El numero esta en la posicion {middle}")
    else:
        print("El numero no a sido encontrado")

num = 8
list_new = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

search_binari(list_new, num)