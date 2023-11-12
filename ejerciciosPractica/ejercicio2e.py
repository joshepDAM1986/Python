# e) Escriba un programa que pida un número de jugadores y tire un dado para cada jugador. El jugador que saque el valor
# más bajo, gana.

# NO CONSIGO HACER QUE IMPRIMA QUE JUGADORES EMPATAN

import random

try:
    numJugadores = int(input("Número de jugadores: "))

    if numJugadores < 2 or numJugadores > 5:
        raise ValueError("El número de jugadores debe estar entre 2 y 5.")

    numInicial=7

    for i in range(numJugadores):
        contJugadores=i+1
        numObtenido = random.randint(1, 6)
        print(f"Resultado del jugador {contJugadores}: {numObtenido}")

        if numObtenido < numInicial:
            numInicial = numObtenido
            jPuntos =i+1

    print(f"El jugador con el valor más bajo es el jugador {jPuntos} con {numInicial}.")

except ValueError as e:
    print(f"Error: {e}")