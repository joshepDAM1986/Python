# g) Escriba un programa que pida un número de dados y tire esa cantidad de dados. Si no salen dos dados iguales seguidos,
# el jugador gana. Si salen, pierde.

import random
rAnterior = None

numTiradas = int(input("Número de tiradas: "))

if numTiradas <= 1:
    print("El número de tiradas debe ser mayor a 2")
else:


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


