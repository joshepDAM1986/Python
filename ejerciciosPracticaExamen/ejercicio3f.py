import random

minMax=7
maxMin=0
sumTotalJ1=0
sumTotalJ2=0

numTiradas=int(input("Ingrese el numero de tiradas: "))
if numTiradas<=0:
    print("El numero de tiradas no puede ser menor o igual a 0")
else:
    for i in range(numTiradas):
        conTiradas=i+1
        numObtenidoJ1=random.randint(1,6)
        print(f"Jugador 1 en su tirada {conTiradas} a sacado {numObtenidoJ1}")

        if numObtenidoJ1<minMax:
            minMax=numObtenidoJ1
        if numObtenidoJ1>maxMin:
            maxMin=numObtenidoJ1
        sumTotalJ1 = minMax + maxMin

    print(f"Valor mas bajo del jugador 1: {minMax}")
    print(f"Valor mas alto del jugador 1: {maxMin}")
    print(f"Puntos totales del jugador 1: {sumTotalJ1}")


    for i in range(numTiradas):
        conTiradas = i + 1
        numObtenidoJ2 = random.randint(1, 6)
        print(f"Jugador 2 en su tirada {conTiradas} a sacado {numObtenidoJ2}")

        if numObtenidoJ2 < minMax:
            minMax = numObtenidoJ2
        if numObtenidoJ2 > maxMin:
            maxMin = numObtenidoJ2
        sumTotalJ2 = minMax + maxMin

    print(f"Valor mas bajo del jugador 2: {minMax}")
    print(f"Valor mas alto del jugador 2: {maxMin}")
    print(f"Puntos totales del jugador 2: {sumTotalJ2}")

    if sumTotalJ1 > sumTotalJ2:
        print("Jugador 1 gana")
    elif sumTotalJ2 > sumTotalJ1:
        print("Jugador 2 gana")
    else:
        print("Empate!!")