# f) Escriba un programa que pida un número de dados y tire esa cantidad de dados para dos jugadores. El jugador que
# saque más puntos sumando su valor más alto y su valor más bajo, gana.

#NO CONSIGO QUE SUMEN SOLO EL VALOR ALTO Y BAJO...

import  random

pJugador1 = 0
pJugador2 = 0

try:

    numTiradas = int(input("Número de tiradas: "))

    if numTiradas <= 1 or numTiradas > 5:
        raise ValueError("El número de tiradas debe estar entre 2 y 5.")


    for i in range(numTiradas):
        rJugador1 = random.randint(1, 6)
        rJugador2 = random.randint(1, 6)
        contTiradas=i+1

        print(f"Resultado del jugador 1 en la tirada {contTiradas}: {rJugador1}")
        print(f"Resultado del jugador 2 en la tirada {contTiradas}: {rJugador2}")

        pJugador1 += max(rJugador1,rJugador1)
        pJugador2 += max(rJugador2,rJugador2)

    print("Puntos totales jugador 1:", pJugador1)
    print("Puntos totales jugador 2:", pJugador2)

    if pJugador1 > pJugador2:
        print("Jugador 1 gana!!")
    elif pJugador2 > pJugador1:
        print("Jugador 2 gana!!")
    else:
        print("Empate!!")

except ValueError as e:
    print(f"Error: {e}")