# e) Escriba un programa que pida un número de jugadores y tire un dado para cada jugador. El jugador que saque el valor
# más bajo, gana.

# NO CONSIGO HACER QUE IMPRIMA QUE JUGADORES EMPATAN

import random

numLimite=7
pJugador=0

numJugadores = int(input("Número de jugadores: "))

if numJugadores < 2:
    print("El número de jugadores debe 2 o mas.")
else:
    for i in range(numJugadores):
        contJugadores=i+1
        numObtenido = random.randint(1, 6)
        print(f"Resultado del jugador {contJugadores}: {numObtenido}")

        if numObtenido < numLimite:
            numLimite = numObtenido
            pJugador =i+1

print(f"El jugador con el valor más bajo es el jugador {pJugador} con {numLimite}.")
