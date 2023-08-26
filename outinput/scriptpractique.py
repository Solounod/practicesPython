import sys

if len(sys.argv) == 2:
    if int(sys.argv[1]) <= 127:
        try:
            character =chr(int(sys.argv[1]))
            print(character)

        except ValueError:
            print("Deve ingresar un numero entero")
    else:
        print("El numero supera la nomenclatura ascci")
else:
    print("introduce solo 1 numero")
