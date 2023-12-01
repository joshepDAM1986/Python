import random

pJ1=0
pJ2=0
numTiradas=int(input("Ingrese el numero de tiradas: "))
if numTiradas<=0:
    print("El numero de tiradas no puede ser 0 o negativo")
else:
    for i in range(numTiradas):
        conTiradas=i+1
        numObtenido=random.randint(1,6)
        print(f"Resultado tirada {conTiradas}: {numObtenido}")
        if numObtenido % 2 == 0:
            print("PAR")
            pJ1=i+1
        else:
            print("IMPAR")
            pJ2=i+1

    print(f"Puntos del Jugador 1: {pJ1}\n"
          f"Puntos del Jugador 2: {pJ2} ")

    if pJ1>pJ2:

        print("Jugador 1 gana")
    elif pJ2>pJ1:
        print("Jugador 2 gana")
    else:
        print("Empate!!")


