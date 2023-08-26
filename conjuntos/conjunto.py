
conjunto = set()



amount = int(input("Ingresa la cantidad de elementos del conjunto: "))

for i in range(amount):
    element = input(f"Ingresa elemento {i + 1} del conjunto: ")
    conjunto.add(element)


list_proof = []
amount_list = int(input("Ingresa la cantidad de elementos de la lista: "))

for j in range(amount_list):
    element = input(f"Ingresa el lemento {j+1} de la lista: ")
    list_proof.append(element)


set_list = set(list_proof)
for x in set_list:
    if x in conjunto:
        print(f"{x} se encuentra en el conjunto")
    else:
        print(f"{x} no se encuentra en el conjunto")


