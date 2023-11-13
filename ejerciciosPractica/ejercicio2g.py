# g) Escriba un programa que pida un número de dados y tire esa cantidad de dados. Si no salen dos dados iguales seguidos,
# el jugador gana. Si salen, pierde.

import random

try:
    numTiradas = int(input("Número de tiradas: "))

    if numTiradas <= 0 or numTiradas > 5:
        raise ValueError("El número de tiradas debe estar entre 2 y 5.")

    rAnterior = None

    for i in range(numTiradas):

        contTirada=i+1
        numObtenido = random.randint(1, 6)
        print(f"Resultado de la tirada {contTirada}: {numObtenido}")

        if numObtenido == rAnterior:
            print("Perdiste, salieron dos dados iguales seguidos.")
            break

        rAnterior = numObtenido

    else:
        print("Ganaste, no salieron dos dados iguales seguidos.")

except ValueError as e:
    print(f"Error: {e}")