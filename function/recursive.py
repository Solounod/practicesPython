def bomb(num):
    num -= 1
    if num > 0:
        print(num)
        bomb(num)
    else:
        print("BOOOOOOM!!!!!!!!")
    print("fin de la funcion", num)


bomb(10)