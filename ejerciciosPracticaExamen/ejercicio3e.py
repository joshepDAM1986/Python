import random


valorFinal=0
puntos=0
numJugadores=int(input("Ingrese el numero de jugadores: "))
if numJugadores<2:
    print("El numero de tiradas no puede ser menor de 2")
else:
    for i in range(numJugadores):
        conJugadores=i+1
        numObtenido=random.randint(1,6)
        print(f"Jugador {conJugadores} a sacado {numObtenido}")

        if numObtenido>valorFinal:
            valorFinal=numObtenido
            puntos+=1

    print(f"El jugador {puntos} gana pues saco {valorFinal}")