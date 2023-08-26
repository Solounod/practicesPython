lista = [3, 4, 1, 9, 2, 5]
def orden_burbuja(lista):
    listaOrdenada = []
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1]= aux
    return lista

print(orden_burbuja(lista))