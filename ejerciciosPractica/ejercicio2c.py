# c) Escriba un programa que pida un número de dados y tire esa cantidad para dos jugadores. El jugador que saque el
# valor más alto, gana.

import random
puntosJ1=0
puntosJ2=0

numTiradas=int(input("Ingerese el numero de tiradas: "))

if numTiradas <= 0:
       print("El numero de tiradas no puede ser negativo ni 0")
else:
    for i in range(numTiradas):
        contTiradas=i+1
        numObtenido1 = random.randint(1, 6)
        numObtenido2 = random.randint(1, 6)

        print(f"Resultado tirada {contTiradas} jugador 1: {numObtenido1}")
        print(f"Resultado tirada {contTiradas} jugador 2: {numObtenido2}")

        if numObtenido1 > numObtenido2:
            print("El jugador 1 gana!")
            puntosJ1+=1
        elif numObtenido2 > numObtenido1:
            print("El jugador 2 gana!")
            puntosJ2+=1
        else:
            print("Empate!")

    print(f"El jugador 1 gano un total de {puntosJ1} veces")
    print(f"El jugador 2 gano un total de {puntosJ2} puntos")




