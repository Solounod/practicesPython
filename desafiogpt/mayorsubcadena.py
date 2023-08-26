"""Escribe una función que tome dos cadenas como entrada y devuelva la subcadena común más larga."""


def count_substring(string1, string2):
    liststring1 = string1.split()
    liststring2 = string2.split()
    resultado = ""
    for i in liststring1:
        for j in liststring2:
            if i == j:
                if len(i) > len(resultado):
                    resultado = i
    return resultado

string1 = "esto es una prueba de palabras largas para comparar"
string2 = "esta es otra prueba de palabras ultra largas como  esternomastocleido"

print(count_substring(string1, string2))


"""def subcadena_comun(cadena1, cadena2):
    m = len(cadena1)
    n = len(cadena2)
    # Creamos una matriz para almacenar los resultados
    matriz = [[0] * (n + 1) for i in range(m + 1)]
    resultado = ""
    # Recorremos las dos cadenas y llenamos la matriz
    for i in range(m):
        for j in range(n):
            if cadena1[i] == cadena2[j]:
                matriz[i + 1][j + 1] = matriz[i][j] + 1
                if matriz[i + 1][j + 1] > len(resultado):
                    resultado = cadena1[i - matriz[i + 1][j + 1] + 1:i + 1]
            else:
                matriz[i + 1][j + 1] = 0
    return matriz


string1 = "esto es una prueba de palabras largas para comparar"
string2 = "esta es otra prueba de palabras ultra largas como  esternomastocleido"


print(subcadena_comun(string1, string2))"""

    
