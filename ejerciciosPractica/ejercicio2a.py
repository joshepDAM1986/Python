# a) Escriba un programa que pida un número de dados, que pida un valor a conseguir y que tire después el número de
# dados indicado. El jugador gana si saca el valor ganador.

import random

try:

    numTiradas = int(input("Número de tiradas: "))
    if numTiradas <=0:
        raise ValueError("El numero de tiradas no puede ser menor o igual que 0")

    numBuscado = int(input("Número a conseguir: "))
    if numBuscado <1 or numBuscado >6:
        raise  ValueError("Un dado tiene 6 caras, escoge un valor entre 1 y 6")

    for i in range(numTiradas):
        contTiradas = i+1
        numObtenido = random.randint(1, 6)
        print(f"Resultado de tirada {contTiradas}: {numObtenido}")

        if numObtenido == numBuscado:
            print("¡Nais!")
            break
        elif contTiradas < numTiradas:
            print("No, inténtalo de nuevo!!")
        else:
            print("No adivinaste el número...")

except ValueError as e:
    print(f"Error: {e}")
