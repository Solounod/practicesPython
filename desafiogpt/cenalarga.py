"""Escribir una función que tome una lista de cadenas de caracteres 
como entrada y devuelva la cadena más larga de la lista."""

list_strings = ["mama", "rodolfo", "puerto", "escenario"]


def large_string(enter_list):
    string_elderly = ""
    for i in range(len(enter_list)):
        for j in range(len(enter_list)):
            if len(enter_list[i]) > len(enter_list[j]):
                string_elderly = enter_list[i]
            else:
                string_elderly = enter_list[j]
    return string_elderly

print(large_string(list_strings))


"""codigo chat gpt: 
def large_string(enter_list):
    string_elderly = enter_list[0]
    for i in range(1, len(enter_list)):
        if len(enter_list[i]) > len(string_elderly):
            string_elderly = enter_list[i]
    return string_elderly

list_strings = ["mama", "rodolfo", "puerto", "escenario"]
print(large_string(list_strings))"""
