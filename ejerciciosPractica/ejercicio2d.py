# d) Escriba un programa que pida un número de dados y tire esa cantidad de dados. El primer jugador obtiene un punto
# por cada dado par. El segundo jugador obtiene un punto por cada dado impar. El jugador que saque más puntos, gana.

import random

numTiradas= int(input("Número de tiradas: "))

if numTiradas <=0:
    print("El numero de tiradas no puede ser igual o menor que cero")

pJugador1 = 0
pJugador2 = 0

for i in range(numTiradas):
    contTiradas=i+1
    resultado = random.randint(1, 6)
    print(f"Resultado de la tirada {contTiradas}: {resultado}")

    if resultado % 2 == 0:
        pJugador1 += 1
        print("PAR!!")
    else:
        pJugador2 += 1
        print("IMPAR!!")

print("Puntos totales jugador 1:", pJugador1)
print("Puntos totales jugador 2:", pJugador2)

if pJugador1 > pJugador2:
    print("¡Jugador 1 gana!!")
elif pJugador2 > pJugador1:
        print("¡Jugador 2 gana!!")
else:
    print("empate!!")
