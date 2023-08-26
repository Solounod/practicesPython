"""Crea 2 conjuntos con numeracion ascii y los transforma a caracteres evaluando
los caracteres repetidos en cada conjunto"""

import random

set_major = set()
list_set1 = []
list_set2 = []

amount_list1 = int(input("Ingresa la cantidad de elementos del conjunto 1: "))
amount_list2 = int(input("Ingresa la cantidad de elementos del conjunto 2: "))


for  i in range(amount_list1):
    num_rand = random.randint(97,122)
    str_rand = chr(num_rand)
    list_set1.append(str_rand)

for  i in range(amount_list2):
    num_rand = random.randint(97,122)
    str_rand = chr(num_rand)
    list_set2.append(str_rand)

set_1 = set(list_set1)
set_2 = set(list_set2)

for x in set_2:
    if x in set_1:
        print(f"{x} se encuentra en el conjunto")
        set_major.add(x) 
    else:
        print(f"{x} no se encuentra en el conjunto")

print(set_major)
