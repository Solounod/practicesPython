
"""Escribir una función que reciba un número entero n como entrada 
y devuelva una lista con los primeros n números de la serie de Fibonacci."""


def fibonacci(n):
    a, b = 0, 1
    aux = 0
    list_fib = []
    for i in range(n):
        aux = a + b
        list_fib.append(aux)
        a = b
        b = aux
    return list_fib

number_input = int(input("Ingresa un numero: "))
print(fibonacci(10))

