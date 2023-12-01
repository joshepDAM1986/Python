import random

numContraseñas=int(input("Ingrese el numero de contraseñas: "))
longContraseñas=int(input("Ingrese la longitud de las contraseñas"))
cadena="0123456789@ABCDEFGHIJKLMNOPQRSTUVXYZ\]_abdefghijklmnpqrstuvwxyz"
lista=list(cadena)

for i in range(numContraseñas):
    resultado=""
    for i in range(longContraseñas):
        resultado+=random.choice(lista)
    print(resultado)
