import sys

list_string = []
lista_args = sys.argv
lista_args.pop(0)

for i in lista_args:
    if int(i) <= 127:
        try:
            character =chr(int(i))
            list_string.append(character)    
        except ValueError:
            print("Deve ingresar un numero entero")
    else:
        print("El numero supera la nomenclatura ascci")
    


new_lis = "".join(list_string)
print(new_lis)
