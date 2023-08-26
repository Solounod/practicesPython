"""Escribe una función que tome una cadena como entrada y devuelva un diccionario que contenga 
el número de veces que aparece cada palabra en la cadena."""

def count_word(stringsword):
    wordscount = {}
    wordlist = stringsword.split()
    for word in wordlist:
        num = stringsword.count(word)
        wordscount[word] = num
    return wordscount

    


charinput = input("Ingrese cadena de caracteres: \n")

print(count_word(charinput))

