# c) Escriba un programa que pida un número de dados y tire esa cantidad para dos jugadores. El jugador que saque el
# valor más alto, gana.

import random

numAlto1 = 0
numAlto2 = 0

try:
    numTiradas = int(input("Numero de tiradas: "))

    if numTiradas <= 0:
        raise ValueError("El numero de tiradas tiene q ser un numero entero positivo")
    elif numTiradas >5:
        raise ValueError("El numero maximo de tiradas es 5")

    for i in range(numTiradas):
        contTiradas=i+1
        numObtenido1 = random.randint(1, 6)
        numObtenido2 = random.randint(1, 6)

        print(f"Resultado tirada {contTiradas} jugador 1: {numObtenido1}")
        print(f"Resultado tirada {contTiradas} jugador 2: {numObtenido2}")

        if numObtenido1 > numObtenido2:
            print("El jugador 1 gana!")
        elif numObtenido2 > numObtenido1:
            print("El jugador 2 gana!")
        else:
            print("Empate!")

except ValueError as e:
    print(f"Error: {e}")