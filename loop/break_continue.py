

for n in range(2,10):
    print(n,'*******')
    for x in range(2,n):
        print("---------------------")
        print("n: ", n)
        print("x: ", x)
        if n % x == 0:
            print(n, 'es igual a', x, '*', n/x)
            break
        else:
            print(n, 'es un numero primo')


#2 *******
#3 *******
#---------------------
#n:  3
#x:  2
#3 es un numero primo
#4 *******
#---------------------
#n:  4
#x:  2
#4 es igual a 2 * 2.0
#5 *******
#---------------------
#n:  5
#x:  2
#5 es un numero primo
#---------------------
#n:  5
#x:  3
#5 es un numero primo
#---------------------
#n:  5
#x:  4
#5 es un numero primo
#6 *******
#---------------------
#n:  6
#x:  2
#6 es igual a 2 * 3.0
#7 *******
#---------------------
#n:  7
#x:  2
#7 es un numero primo
#---------------------
#n:  7
#x:  3
#7 es un numero primo
#---------------------
#n:  7
#x:  4
#7 es un numero primo
#---------------------
#n:  7
#x:  5
#7 es un numero primo
#---------------------
#n:  7
#x:  6
#7 es un numero primo
#8 *******
#---------------------
#n:  8
#x:  2
#8 es igual a 2 * 4.0
#9 *******
#---------------------
#n:  9
#x:  2
#9 es un numero primo
#---------------------
#n:  9
#x:  3
#9 es igual a 3 * 3.0