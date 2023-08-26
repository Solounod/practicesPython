def return_values():
    list_p = [1, 2, 3, 3, 5, 6]
    str_n = "Hola mundo"
    date = 34
    return list_p, str_n, date

lista, cadena, edad = return_values()

lista.append(edad)
lista.append(cadena)

print(lista)